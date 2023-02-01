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
    pass

def receive_message(client_socket)
    '''Receive an incoming message from a specific client & forward the message to be broadcast'''
    pass

def connect_client():
    '''Connect an incoming client to the server'''
    pass

