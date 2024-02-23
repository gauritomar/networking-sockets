import socket

# Ip of the server not the computer
# Doesnt matter the IP of the client, this IP needs
# to be of the server router, the public IP of the server
HOST = "192.168.29.171"
PORT = 9090

# no longer hosting but connecting hence we dont need a while True
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sends a request to the server and the server has to connect
socket.connect((HOST, PORT))
socket.send("Hello World!".encode('utf-8'))
print(socket.recv(1024).decode('utf-8'))