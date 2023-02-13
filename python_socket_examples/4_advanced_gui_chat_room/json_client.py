# Client Side Json
import socket, json

# create a client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((socket.gethostbyname(socket.gethostname()), 54321))

# receive the encoded json object (string) from the server...do we have to decode???
message_json = client_socket.recv(1024)
# we can decode, but we don't have to with json...
# message_json = client_socket.recv(1024).decode('utf-8')
print(message_json)
print(type(message_json))

# turn the bytes obj or string obj (if decoded) back into a dict using json
# the loads method can kill 2 birds with 1 stone: it can de-serialize a bytes obj (encoded str) containing a json obj (str) to its corresponding Python obj (dict)
message_packet = json.loads(message_json)
print(message_packet)
print(type(message_packet))

# our new obj is in fact a dict
print(message_packet['message'])
for (key, value) in message_packet.items():
    print(f"{key}:{value}")

# close the socket
client_socket.close()

