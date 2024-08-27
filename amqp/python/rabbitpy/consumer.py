import rabbitpy, os

def consumer():
    url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/%2f')
    print(url)

    connection = rabbitpy.Connection(url)
    channel = connection.channel()

    queue = rabbitpy.Queue(channel, 'example1')

    # While there are messages in the queue, fetch them using Basic.Get
    while len(queue) > 0:
        message = queue.get()
        print('Message Q1: %s' % message.body.decode())
        message.ack()

if __name__ == "__main__":
    consumer()
