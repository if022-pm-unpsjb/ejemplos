defmodule Producer do
  @moduledoc """
  Módulo para enviar mensajes a RabbitMQ.
  """
  use AMQP

  def send_message(message) do
    # Conectar al servidor RabbitMQ
    {:ok, connection} = Connection.open("amqpurl", ssl_options: [verify: :verify_none])
    {:ok, channel} = Channel.open(connection)

    # Declarar una cola y un exchange
    queue_name = "test_queue"
    exchange_name = "test_exchange"

    Queue.declare(channel, queue_name, durable: true)
    Exchange.declare(channel, exchange_name, :direct, durable: true)

    # Enlazar la cola con el exchange
    Queue.bind(channel, queue_name, exchange_name)

    # Publicar el mensaje
    Basic.publish(channel, exchange_name, "", message)

    IO.puts("Mensaje enviado: #{message}")

    # Cerrar conexión
    Channel.close(channel)
    Connection.close(connection)
  end
end
