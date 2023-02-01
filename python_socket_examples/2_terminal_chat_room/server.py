# Server Side Chat Room
import socket, threading

# define constants to be used
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345
ENCODER = "utf-8"
BYTE_SIZE = 1024

# create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()

# create two blank lists to store connected client sockets & their names
client_socket_list = []
client_name_list = []


def broadcast_message(message):
    '''Send a message to ALL clients connected to the server'''
    # I feel as if there could be a socket function that broadcasts a message so we wouldn't need to define & call our own function
    for client_socket in client_socket_list:
        client_socket.send(message)


def receive_message(client_socket):
    '''Receive an incoming message from a specific client & forward the message to be broadcast'''
    while True:
        try:
            # get the name of the given client
            index = client_socket_list.index(client_socket)
            name = client_name_list[index]

            # receive message from the client
            message = client_socket.recv(BYTE_SIZE).decode(ENCODER)
            message = f"{name}: {message}".encode(ENCODER)
            broadcast_message(message)
        except:
            # find the index of the client socket in our list
            # I don't understand why we have to redefine 'index' & 'name', seems redundant
            index = client_socket_list.index(client_socket)
            name = client_name_list[index]

            # remove the client socket & name from lists
            client_socket_list.remove(client_socket)
            client_name_list.remove(name)

            # close the client socket
            client_socket.close()

            # broadcast that the client has left the chat
            broadcast_message(f"{name} has left the chat!".encode(ENCODER))
            break


def connect_client():
    '''Connect an incoming client to the server'''
    while True:
        # accept any incoming client connection
        client_socket, client_address = server_socket.accept()
        print(f"Connected with {client_address}...")

        # send a NAME flag to prompt the client for their name
        client_socket.send("NAME".encode(ENCODER))
        client_name = client_socket.recv(BYTE_SIZE).decode(ENCODER)

        # add new client socket & client name to appropriate lists
        client_socket_list.append(client_socket)
        client_name_list.append(client_name)

        # update the server, individual client, & ALL clients
        print(f"Name of new client is {client_name}\n") # server
        client_socket.send(f"{client_name}, you have connected to the server!".encode(ENCODER)) # individual client
        broadcast_message(f"{client_name} has joined the chat!".encode(ENCODER)) # all clients

        # now that a new client has connected, start a thread
        receive_thread = threading.Thread(target=receive_message, args=(client_socket,))
        receive_thread.start()


# start the server
print("Server is listening for incoming connections...")
connect_client()
# connect_thread = threading.thread(target=connect_client)
# connect_thread.start()



