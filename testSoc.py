import socket

soc =socket.socket()
soc.bind(("localhost",2004))
soc.listen(5)
soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

while True:
    (clientsocket, address) = soc.accept()

    

soc.close()