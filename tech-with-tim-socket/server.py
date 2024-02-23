import socket
import threading

# the message we sent will have to be bytes = 64
HEADER = 64
# the message is padded to this length so the
# server knows what lenght to expect and make the message
PORT = 5050
SERVER = "192.168.29.171"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# we bind this socket to this address, anything that hits this 
# address will be sent to this socket
server.bind(ADDR)

# this function will be running in a thread hence it will
# be running in parallel to the main thread
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        # Receive the message length from the client
        msg_length = conn.recv(HEADER).decode(FORMAT).strip()  # Remove leading/trailing whitespace
        if not msg_length:  # Check if the message length is empty
            print("[CLIENT DISCONNECTED] Client disconnected.")
            break  # Break out of the loop if the client has disconnected

        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        print(f"[{addr}] {msg}")
        conn.send("Msg received".encode(FORMAT))

        # Check if the client wants to disconnect
        if msg == DISCONNECT_MESSAGE:
            print("[CLIENT DISCONNECTED] Client requested disconnection.")
            break  # Break out of the loop if the client requested disconnection
    
    conn.close()



def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        # store the connection and the address from which a 
        # connection is made to the server
        conn, addr = server.accept()

        # start a thread of the handle client function
        # that will handle the client
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        # print the number of active connections to the server
        # we subtract one as the def start() is the already started thread
        print(f"[ACTIVE CONNECtIONS] {threading.activeCount() -1}")




print("[STARTING] server is starting...")
start()