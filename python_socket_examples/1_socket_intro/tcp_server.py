# TCP Server Side

import socket

# create a server side socket using IPV4 (AF_INET) & TCP (SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# see how to get IP address dynamically
print(socket.gethostname()) # hostname
print(socket.gethostbyname(socket.gethostname())) # IP address of the given hostname

# bind our new socket to a tuple (IP address, port address)
server_socket.bind(socket.gethostbyname(socket.gethostname()), 12345)

# put the socket into listening mode to listen for any possible connections
server_socket.listen()