import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9999))

client.send("Hello Server".encode("utf-8"))
print(client.recv(1024).decode('utf-8'))

client.send(input("Enter your message to send to the server: ").encode('utf-8'))

client.send("Bye Server".encode("utf-8"))
print(client.recv(1024).decode('utf-8'))
