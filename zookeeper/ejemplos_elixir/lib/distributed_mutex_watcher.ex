defmodule DistMutex do
  use GenServer

  @zookeeper_address ~c"127.0.0.1"  # Cambia esto a tu servidor ZooKeeper
  @lock_path "/mutex"

  ## Cliente

  def start_link(opts \\ %{}) do
    GenServer.start_link(__MODULE__, opts, name: __MODULE__)
  end

  ## Callbacks de GenServer

  def init(_) do
    # Conectar a ZooKeeper usando erlzk
    {:ok, pid} = :erlzk.connect([{@zookeeper_address, 2181}], 3000)
    Process.flag(:trap_exit, true)

    {:ok, %{zk_pid: pid, waiting: false}}
  end

  def terminate(_, state) do
    :erlzk.close(state.zk_pid)
  end

  ## Funciones de Exclusión Mutua

  def acquire_lock(pid \\ __MODULE__) do
    GenServer.call(pid, :acquire_lock)
  end

  def release_lock(pid \\ __MODULE__) do
    GenServer.call(pid, :release_lock)
  end

  def handle_call(:acquire_lock, _from, state) do
    case try_create_lock(state.zk_pid) do
      :ok ->
        IO.puts("mutex adquirido.")
        {:reply, :ok, state}

      :error ->
        IO.puts("mutex no disponible.")
        {:reply, :error, set_watch(state)}
    end
  end

  def handle_call(:release_lock, _from, state) do
    :erlzk.delete(state.zk_pid, @lock_path)
    IO.puts("mutex liberado.")
    {:reply, :ok, state}
  end

  def handle_info({:node_deleted, @lock_path}, state) do
    IO.puts("Notificación recibida: mutex liberado.")
    {:noreply, state}
    case try_create_lock(state.zk_pid) do
      :ok ->
        IO.puts("mutex adquirido.")
        {:noreply, state}

      :error ->
        IO.puts("mutex no disponible.")
        {:noreply, set_watch(state)}
    end
  end

  ## Funciones Auxiliares

  defp try_create_lock(zk_pid) do
    case :erlzk.create(zk_pid, @lock_path, :ephemeral) do
      {:ok, _} -> :ok
      {:error, _} -> :error
    end
  end

  defp set_watch(state) do
    # Registrar un watcher para monitorear la liberación del bloqueo
    :erlzk.exists(state.zk_pid, @lock_path, self())
    %{state | waiting: true}
  end

end
