# Ejemplo LavinMQ

El ejemplo esta tomado de la documentación oficial (Python).

Ejecutar el servidor mediante docker de la siguiente manera:

docker run --network host --rm -it -P -v /var/lib/lavinmq:/tmp/amqp cloudamqp/lavinmq
