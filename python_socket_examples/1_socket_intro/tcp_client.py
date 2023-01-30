# TCP client side

import socket

# create a client side IPv4 socket (AF_INET) & TCP (SOCK_STREAM)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the socket to a server located at a given IP & port
client_socket.connect(((socket.gethostbyname(socket.gethostname())), 12345)) # we don't have to hardcode the address since the server is on the same machine as the client


