import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(('localhost', 9999))

while True:
    message, address = server.recvfrom(1024)
    print(message.decode('utf-8'))