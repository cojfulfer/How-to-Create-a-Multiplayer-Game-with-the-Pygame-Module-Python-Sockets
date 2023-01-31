# chat server side
import socket

# define constants to be used
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345
ENCODER = "utf-8"
BYTE_SIZE = 1024

# create a server socket, bind it to a ip/port, & listen
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()

# accept any incoming connection & let them know that they're connected
print("Server is running...\n")
client_socket, client_address = server_socket.accept()
client_socket.send("You are connected to the server...\n".encode(ENCODER))

# send/receive messages
while True:
    # receive info from the client
    message = client_socket.recv(BYTE_SIZE).decode(ENCODER)

    # quit if the client socket wants to quit, else display the message
    if message.lower() == "quit":
        client_socket.send("quit".encode(ENCODER))
        print("\nEnding the chat...goodbye!")
        break
    else:
        print(f"\n{message}\n")
        message = input("Message: ")
        client_socket.send(message.encode(ENCODER))

# close the socket
server_socket.close()
