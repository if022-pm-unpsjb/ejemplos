import os
import argparse
import pika

def send_message(url, exchange, message):
    connection = pika.BlockingConnection(pika.URLParameters(url))
    channel = connection.channel()

    channel.exchange_declare(exchange=exchange, exchange_type='fanout', durable=True)

    channel.basic_publish(exchange=exchange, routing_key='', body=message)
    print(f" [x] Sent: {message}")
    
    connection.close()

def main():
    # Parser de argumentos
    parser = argparse.ArgumentParser(description='Send a message to a RabbitMQ queue.')
    parser.add_argument('-e', '--exchange', type=str, default="amq.fanout", help='Destination exchange.')
    parser.add_argument('message', type=str, help='The message to send.')

    url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/%2f')

    # Parsea argumentos
    args = parser.parse_args()

    send_message(url, args.exchange, args.message)


if __name__ == "__main__":
    main()
