import os
import argparse
import pika

def callback(ch, method, properties, body):
    print(f" [x] Received: {body.decode()}")

def receive_message(url, exchange):
    connection = pika.BlockingConnection(pika.URLParameters(url))
    channel = connection.channel()

    channel.exchange_declare(exchange=exchange, exchange_type='fanout', durable=True)

    result = channel.queue_declare('', exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange=exchange, queue=queue_name)

    print(' [*] Waiting for messages. To exit press CTRL+C')

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()

def main():
    # Parser de argumentos
    parser = argparse.ArgumentParser(description='Receive messages from RabbitMQ topic.')
    parser.add_argument('-e', '--exchange', type=str,
            default="amq.fanout", help='Destination exchange.')

    url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/%2f')

    # Parsea argumentos
    args = parser.parse_args()

    receive_message(url, args.exchange)


if __name__ == "__main__":
    main()
