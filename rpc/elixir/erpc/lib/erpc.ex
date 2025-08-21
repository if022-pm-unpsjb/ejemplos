defmodule Erpc do
  @moduledoc """
  Documentation for `Erpc`.
  """

  @doc """
  Hello world.

  ## Examples

      iex> Erpc.hello()
      :world

  """
  def hello(name) do
    IO.puts("Hello #{name}")
  end

  def send_hello do
    receive do 
      {name, from} -> send(from, "hello #{name}")
    end
    send_hello()
  end
end
