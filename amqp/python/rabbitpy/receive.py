import rabbitpy, os

url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/%2f')
print(url)
msg = rabbitpy.simple.get(url, "hello")
print(msg.body)

