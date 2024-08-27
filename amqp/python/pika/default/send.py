import os
import argparse
import pika

def main():
    """
    Envia mensaje a broker AMQP
    """

    # Parser de argumentos
    parser = argparse.ArgumentParser(description='Send a message to a RabbitMQ queue.')
    parser.add_argument('--queue', type=str, default="test", help='Destination queue.')
    parser.add_argument('message', type=str, help='The message to send to the queue.')

    url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/%2f')

    # Parsea argumentos
    args = parser.parse_args()

    # Conexión al servidor RabbitMQ
    connection = pika.BlockingConnection(pika.URLParameters(url))
    channel = connection.channel()

    # Declarar una cola (esto también crea la cola si no existe)
    channel.queue_declare(queue=args.queue)

    # Enviar el mensaje al exchange default con la clave de ruteo igual al nombre de la cola
    channel.basic_publish(exchange='', routing_key=args.queue, body=args.message)

    print(f" [x] Sent '{args.message}'")

    # Cerrar la conexión
    connection.close()

if __name__ == "__main__":
    main()
