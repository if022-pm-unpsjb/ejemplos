defmodule Producer do
  @moduledoc """
  Módulo para enviar mensajes a RabbitMQ.
  """
  use AMQP

  # nombre de la cola de mensajes
  @queue_name "test_queue"
  # nombre del exchange
  @exchange_name "test_exchange"

  def send_message(queue_name, message) do
    # Obtener el canal AMQP (definido en la configuración)
    {:ok, channel} = AMQP.Application.get_channel(:channel)

    # Declara la cola de mensajes. Si no existe, se crea.
    Queue.declare(channel, queue_name, durable: true)

    # Publicar el mensaje
    Basic.publish(channel, "", queue_name, message)

    IO.puts("Mensaje enviado: #{message}")
  end


  def send_message(message) do
    # Obtener el canal AMQP (definido en la configuración)
    {:ok, channel} = AMQP.Application.get_channel(:channel)

    # Declara la cola de mensajes
    Queue.declare(channel, @queue_name, durable: true)

    # Declara el exchange
    Exchange.declare(channel, @exchange_name, :direct, durable: true)

    # Enlaza la cola de mensajes con el exchange
    Queue.bind(channel, @queue_name, @exchange_name)

    # Publicar el mensaje
    Basic.publish(channel, @exchange_name, "", message)

    IO.puts("Mensaje enviado: #{message}")
  end

  def publish_message(message) do
    {:ok, channel} = AMQP.Application.get_channel(:channel)

    AMQP.Exchange.declare(channel, "pubsub", :fanout)

    AMQP.Basic.publish(channel, "pubsub", "", message)

    IO.puts("Mensaje publicado: #{message}")
  end

end
