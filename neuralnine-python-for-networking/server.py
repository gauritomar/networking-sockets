import socket


# To convert a socket to a server, we need to bind it to a host and a port
HOST = "192.168.29.171"
PORT = 9090

# AF_INET: Internet Socket, SOCK_STREAM = TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

# If more than 5 connections are waiting then we do not
# accept any more connections
server.listen(5)

while True:
    # we use another socket for connection
    communication_socket, address = server.accept()
    # it returns a new socket object representing the connection
    # the previous socket is just for accepting connections,
    # the communication socket is the socket returnde from the
    # acceptance method

    print(f"Connection from {address} has been established!")
    # we accept the connection and print the message from the client
    # when we send messages over a socket, we send bytes
    message = communication_socket.recv(1024).decode('utf-8')
    print("Message from client:", message)
    # we send a reply to the communication socket
    communication_socket.send(f"Got your message! Thank you!".encode('utf-8'))
    communication_socket.close()
    print(f"Connection from {address} has been closed!")


# this server is only for handling one connection at a time