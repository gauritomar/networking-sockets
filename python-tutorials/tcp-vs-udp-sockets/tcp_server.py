import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9999))
server.listen()

while True:
    # server.accept() returns the address of the client connected to it
    # and also a new socket object to send and receive data from the client
    client, address = server.accept()
    print(f"Connected to {address}")

    # TCP is connection oriented so it doesnt matter if we
    # have to specify how many bytes we want to receive
    # But in the case of UDP we have to specify the number of bytes
    # as it will drop the bytes after the specified number size of datagram
    print(client.recv(1024).decode("utf-8"))
    client.send("Hello Client".encode("utf-8"))
    print(client.recv(1024).decode("utf-8"))
    client.send("Goodbye Client".encode("utf-8"))
    client.close()