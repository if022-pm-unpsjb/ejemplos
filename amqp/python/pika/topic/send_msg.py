import os
import argparse
import pika

def send_message(url, exchange, routing_key, message):
    connection = pika.BlockingConnection(pika.URLParameters(url))
    channel = connection.channel()

    channel.exchange_declare(exchange=exchange, exchange_type='topic', durable=True)

    channel.basic_publish(exchange=exchange, routing_key=routing_key, body=message)
    print(f" [x] Sent {routing_key}:{message}")
    
    connection.close()

def main():
    # Parser de argumentos
    parser = argparse.ArgumentParser(description='Send a message to a RabbitMQ queue.')
    parser.add_argument('--exchange', type=str, default="amq.topic", help='Destination exchange.')
    parser.add_argument('--topic', type=str, default="if022", help='Destination topic.')
    parser.add_argument('message', type=str, help='The message to send.')

    url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/%2f')

    # Parsea argumentos
    args = parser.parse_args()

    send_message(url, args.exchange, args.topic, args.message)


if __name__ == "__main__":
    main()
