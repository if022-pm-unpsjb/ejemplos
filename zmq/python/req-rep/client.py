import time
import zmq

def client():
    """
    Cliente
    """

    # Crear un contexto de ZeroMQ
    context = zmq.Context()

    # Crear un socket REQ (solicitud)
    socket = context.socket(zmq.REQ)

    # Conectar el socket al servidor
    socket.connect("tcp://localhost:5555")

    for i in range(10):
        # Envia solicitud al servidor
        request = f"Cliente {i}"
        print(f"Cliente enviando: {request}")
        socket.send_string(request)

        # Espera la respuesta del servidor
        msg = socket.recv_string()
        print(f"Cliente recibió: {msg}")

        # Espera antes de enviar la próxima solicitud
        time.sleep(1)

if __name__ == "__main__":
    client()
