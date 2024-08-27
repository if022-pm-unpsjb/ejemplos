import zmq

def server():
    """
    Servidor
    """

    # Crear un contexto de ZeroMQ
    context = zmq.Context()

    # Crear un socket REP (respuesta)
    socket = context.socket(zmq.REP)

    # Enlaza el socket a una dirección
    socket.bind("tcp://*:5555")

    while True:
        # Espera una solicitud del cliente
        message = socket.recv_string()
        print(f"Servidor recibió: {message}")

        # Responde al cliente
        response = f"Hola, {message}"
        socket.send_string(response)

if __name__ == "__main__":
    server()
