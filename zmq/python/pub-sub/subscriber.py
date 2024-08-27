import zmq

def subscriber():
    """
    Subscriptor
    """

    # Crea un contexto de ZeroMQ
    context = zmq.Context()

    # Crea un socket SUB (suscriptor)
    socket = context.socket(zmq.SUB)

    # Conecta el socket al publicador
    socket.connect("tcp://localhost:5556")

    # Suscribirse a un tema específico
    topic_filter = "TopicA"
    socket.setsockopt_string(zmq.SUBSCRIBE, topic_filter)

    # Recibe y procesa los mensajes
    while True:
        message = socket.recv_string()
        print(f"Recibo: {message}")

if __name__ == "__main__":
    subscriber()
