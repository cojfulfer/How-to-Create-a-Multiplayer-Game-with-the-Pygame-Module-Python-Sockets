# TCP Server Side

import socket

# create a server side socket using IPv4 (AF_INET) & TCP (SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # see how to get IP address dynamically
# print(socket.gethostname()) # hostname
# print(socket.gethostbyname(socket.gethostname())) # IP address of the given hostname

# bind our new socket to a tuple (IP address, port address)
server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))

# put the socket into listening mode to listen for any possible connections
server_socket.listen()

# listen forever to accept ANY connection
while True:
    # accept every single connection & store 2 pieces of info
    client_socket, client_address = server_socket.accept() # returns a tuple of the client socket obj & a tuple of the client IPv4 address & port address that the client is using for the connection (not the same port address that client is connecting to)
    # print(type(client_socket))
    # print(client_socket)
    # print(type(client_address))
    # print(client_address)

    print(f"Connected to {client_address}!\n")

    # send a message to the client that just connected
    client_socket.send("You are connected!".encode("utf-8"))

    # close the connection
    server_socket.close()
    break