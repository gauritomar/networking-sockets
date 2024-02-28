import socket 

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.connect(('localhost', 9999))

client.sendto("Hello Server!".encode('utf-8'), ('localhost', 9999))
print(client.recvfrom(1024)[0].decode('utf-8'))
while True:
    msg = input()
    client.sendto(msg.encode('utf-8'), ('localhost', 9999))
    if msg == "done":
        break
