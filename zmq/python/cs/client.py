from time import sleep
import zmq

def client():
    """
    Cliente
    """

    # Crea un contexto ZMQ
    context = zmq.Context()

    # Crea un socket de tipo REQUEST
    socket  = context.socket(zmq.REQ)

    # Conecta el socket y se bloquea
    socket.connect("tcp://localhost:12345")

    for _ in range(3):
        # Envia un mensaje
        socket.send(b"Hola mundo")
        # Espera la respuesta
        message = socket.recv()
        # Imprime el mensaje
        print(message.decode())
        sleep(1)

if __name__ == "__main__":
    client()
