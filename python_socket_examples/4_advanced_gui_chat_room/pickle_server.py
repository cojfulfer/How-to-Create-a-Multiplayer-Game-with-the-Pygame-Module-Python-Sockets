# Pickle Server
import socket, pickle


# Lets create a regular old list
unpickled_list = ['dill', 'bread & butter', 'half-sour']
print(unpickled_list)
print(type(unpickled_list))


# try to encode the list using .encode (DOESN'T WORK; not a string obj!)
# trial_list = unpickled_list.encode("utf-8")
# print(trial_list)
#print(type(trial_list))


# now let's encode by pickling the list!
pickled_list = pickle.dumps(unpickled_list)
print(pickled_list)
print(type(pickled_list)) # bytes obj


# create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostbyname(socket.gethostname()), 54321))
server_socket.listen()


# listen forever to accept ANY connection
while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connected to {client_address}!")

    # send the encoded pickled list...THIS IS ALREADY ENCODED
    client_socket.send(pickled_list)

    # close the socket
    server_socket.close()



