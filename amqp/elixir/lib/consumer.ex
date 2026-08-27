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

  def get(queue_name) do
    {:ok, channel} = AMQP.Application.get_channel(:channel)

    # Declarar la cola de mensajes
    Queue.declare(channel, queue_name, durable: true)

    # Este proceso sera el consumidor.
    Basic.consume(channel, queue_name, nil, no_ack: true)

    receive do
      {:basic_deliver, payload, _meta} -> IO.puts("Msj: #{payload}")
    end
  end

  def subscribe do
    {:ok, channel} = AMQP.Application.get_channel(:channel)

    # fanout broadcast all messages it receives to all the queues it knows
    AMQP.Exchange.declare(channel, "pubsub", :fanout)

    # create a queue with a server-generated random name, using "" as name.
    # the exclusive flag deletes the queue once the consumer connection is closed.
    {:ok, %{queue: queue_name}} = AMQP.Queue.declare(channel, "", exclusive: true)

    # tell the fanout exchange to send messages to the queue queue_name.
    AMQP.Queue.bind(channel, queue_name, "pubsub")

    # This process should receive message from the queue_name queue. The messages
    # could be obtained with the receive clause.
    AMQP.Basic.consume(channel, queue_name, nil, no_ack: true)

    IO.puts " [*] Waiting for messages. To exit press CTRL+C, CTRL+C"

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
