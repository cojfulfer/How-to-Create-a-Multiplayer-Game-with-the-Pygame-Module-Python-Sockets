# chat client side
import socket

# define constants to be used
DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 12345
ENCODER = "utf-8"
BYTE_SIZE = 1024

# create a client socket & connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((DEST_IP, DEST_PORT))

# send/receive messages
while True:
    # receive info from the server
    message = client_socket.recv(BYTE_SIZE).decode(ENCODER)

    # quit if the connected server wants to quit, else keep sending messages
    if message.lower() == "quit":
        client_socket.send("quit".encode(ENCODER))
        print("\nEnding the chat...goodbye!")
        break
    else:
        print(f"\n{message}\n")
        message = input("Message: ")
        client_socket.send(message.encode(ENCODER))

# close the client socket
client_socket.close()
