import rabbitpy, os, sys

url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/%2f')

with rabbitpy.Connection(url) as conn:
    with conn.channel() as channel:
        #exchange = rabbitpy.Exchange(channel, 'my-exchange')
        #exchange.declare()

        #queue = rabbitpy.Queue(channel, 'my-queue')
        #queue.declare()
        #queue.bind(exchange, 'routing-key')

        message = rabbitpy.Message(channel, sys.argv[1])
        message.publish('', 'test')
