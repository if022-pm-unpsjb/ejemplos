import time
import zmq

def publisher():
    """
    Publicador
    """

    # Crea un contexto de ZeroMQ
    context = zmq.Context()

    # Crea un socket PUB (publicador)
    socket = context.socket(zmq.PUB)

    # Enlaza el socket a una dirección
    socket.bind("tcp://*:5556")

    count = 0

    while True:

        # Crear un mensaje y publicarlo
        topic = "TopicA"
        message = f"Mensaje #{count}"
        print(f"Publicando: {topic} - {message}")
        socket.send_string(f"{topic} {message}")

        count = count + 1

        # Espera un segundo antes de enviar el próximo mensaje
        time.sleep(1)

if __name__ == "__main__":
    publisher()
