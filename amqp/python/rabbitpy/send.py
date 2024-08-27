import rabbitpy, os

url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/%2f')
print(url)
with rabbitpy.Connection(url) as conn:
    with conn.channel() as channel:
        message = rabbitpy.Message(channel, "Hola")
        message.publish('', "hello")
