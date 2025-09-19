defmodule Consumer do
  @moduledoc """
  Módulo para recibir mensajes de RabbitMQ.
  """
  use AMQP

  def start do
    url = case System.get_env("AMQP_URL") do
      nil -> ""
      url -> url
    end

    # Conectar al servidor RabbitMQ
    {:ok, connection} = Connection.open(url, ssl_options: [verify: :verify_none])
    {:ok, channel} = Channel.open(connection)

    # Declarar una cola
    queue_name = "test_queue"
    Queue.declare(channel, queue_name, durable: true)

    # Configurar el consumidor
    Basic.consume(channel, queue_name, nil, no_ack: true)

    # Iniciar el loop para recibir mensajes
    receive_messages(channel)
  end

  defp receive_messages(channel) do
    receive do
      {:basic_deliver, payload, _meta} ->
        IO.puts("Mensaje recibido: #{payload}")
        receive_messages(channel)
    end
  end
end
