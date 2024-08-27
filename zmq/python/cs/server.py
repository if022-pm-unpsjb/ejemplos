import zmq

def server():
    """
    Servidor
    """
    context = zmq.Context()
    socket  = context.socket(zmq.REP)       # create reply socket
    socket.bind("tcp://*:12345")            # bind socket to address

    while True:
        message = socket.recv()                 # wait for incoming message
        if "STOP" not in str(message):          # if not to stop...
            reply = str(message.decode())+'*'   # append "*" to message
            socket.send(reply.encode())         # send it away (encoded)
        else:
            break                               # break out of loop and end

if __name__ == "__main__": #-
    server()
