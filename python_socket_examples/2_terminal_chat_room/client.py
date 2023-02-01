# Client Side Chat Room
import socket, threading

# define constants to be used
DEST_IP = socket.gethostbyname(socket.gethostname())
# DEST_IP = "192.168.1.247"
DEST_PORT = 12345
ENCODER = "utf-8"
BYTE_SIZE = 1024

# create a client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((DEST_IP, DEST_PORT))


def send_message():
    "Send a message to the server to be broadcast"
    while True:
        message = input("")
        client_socket.send(message.encode(ENCODER))


def receive_message():
    "Receive an incoming message from the server"
    while True:
        try:
            # receive an incoming message from the server
            message = client_socket.recv(BYTE_SIZE).decode(ENCODER)

            # check for the name flag, else show the message
            if message == "NAME":
                name = input("What is your name?: ")
                client_socket.send(name.encode(ENCODER))
            else:
                print(message)
        except:
            # an error occured, close the connection
            print("An error occured...")
            client_socket.close()
            break


# create threads to continuously send & receive messages
receive_thread = threading.Thread(target=receive_message)
send_thread = threading.Thread(target=send_message)

# start the client
receive_thread.start()
send_thread.start()
