defmodule Consumer do
  @moduledoc """
  Módulo para recibir mensajes de RabbitMQ.
  """
  use AMQP

  # nombre de la cola de mensajes
  @queue_name "test_queue"

  def start do
    {:ok, channel} = AMQP.Application.get_channel(:channel)

    # Declarar la cola de mensajes
    Queue.declare(channel, @queue_name, durable: true)

    # Configurar el consumidor
    Basic.consume(channel, @queue_name, nil, no_ack: true)

    # Iniciar el loop para recibir mensajes
    receive_messages(channel)
  end

  defp receive_messages(channel) do
    receive do
      {:basic_deliver, payload, _meta} ->
        IO.puts("Msj: #{payload}")
        receive_messages(channel)
    end
  end
end
