import rabbitpy, os, logging

url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/%2f')

logging.basicConfig(level=logging.INFO)

with rabbitpy.Connection(url) as conn:
    with conn.channel() as channel:
        for msg in rabbitpy.Queue(channel, 'test'):
            print(msg.body.decode())
            #msg.pprint(True)
            msg.ack()
