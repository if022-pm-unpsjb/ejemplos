import rabbitpy, os

def producer():
    url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/%2f')
    print(url)

    connection = rabbitpy.Connection(url) # Connect to RabbitMQ server
    channel = connection.channel()     # Create new channel on the connection

    exchange = rabbitpy.Exchange(channel, 'exchange') # Create an exchange
    exchange.declare()

    queue1 = rabbitpy.Queue(channel, 'example1') # Create 1st queue
    queue1.declare()

    queue1.bind(exchange, 'example-key') # Bind queue1 to a single key

    message = rabbitpy.Message(channel, 'Test message')
    message.publish(exchange, 'example-key') # Publish the message using the key
    exchange.delete() 

if __name__ == "__main__":
    producer()
