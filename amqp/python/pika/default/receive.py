import os
import argparse
import pika

def callback(channel, method, properties, body):
    print(f" [x] Received {body.decode()}")

def main():
    """
    Conecta con broker AMQP y espera por mensajes.
    """

    # Configurar el parser de argumentos
    parser = argparse.ArgumentParser(description='Receive messages from a RabbitMQ queue.')
    parser.add_argument('--queue', type=str, default='test',
            help='The queue to receive messages from.')

    url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/%2f')

    # Argumentos
    args = parser.parse_args()

    # Conexión con servidor RabbitMQ
    connection = pika.BlockingConnection(pika.URLParameters(url))
    channel = connection.channel()

    # Declarar la cola (esto también crea la cola si no existe)
    channel.queue_declare(queue=args.queue)

    # función de callback para procesar los mensajes
    channel.basic_consume(queue=args.queue,
                          on_message_callback=callback,
                          auto_ack=True)

    print(f" [*] Waiting for messages in '{args.queue}'. To exit press CTRL+C")

    # Consumir mensajes
    channel.start_consuming()

if __name__ == "__main__":
    main()
