# Client Side Advanced GUI Chat Room (Admin)
import tkinter, socket, threading, json
from tkinter import DISABLED, VERTICAL, END, NORMAL


# define window
root = tkinter.Tk()
root.title("Chat Server")
root.iconbitmap("message_icon.png")
root.geometry('600x600')
root.resizable(0,0) # user not able to resize window


# define fonts & colors
my_font = ('SimSun', 14)
black = "#010101"
light_green = "#1fc742"
root.config(bg=black)


# create a connection class to hold our server socket
class Connection():
    '''A class to store a connection - a server socket & pertinent information'''
    def __init__(self):
        self.host_ip = socket.gethostbyname(socket.gethostname())
        self.encoder = 'utf-8'
        self.byte_size = 1024

        self.client_sockets = [] # list of client sockets connected to the server
        self.client_ips = [] # list of the IP addresses of the client sockets
        self.banned_ips = [] # list of banned client sockets


# define functions
def start_server(connection):
    '''Start the server on a given port number'''
    # retrieve the port number to run the server & attach to the connection obj
    # we can append attributes to the 'Connection()' class by passing in a 'Connection()' class obj into the function
    connection.port = int(port_entry.get()) # essentially 'self.port'

    # create server socket
    connection.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # essentially 'self.server_socket'
    connection.server_socket.bind((connection.host_ip, connection.port))
    connection.server_socket.listen()

    # update GUI
    history_listbox.delete(0, END) # reset chat history
    history_listbox.insert(0, f"Server started on port {connection.port}.")
    # enable server buttons & disable start button
    end_button.config(state=NORMAL)
    self_broadcast_button.config(state=NORMAL)
    message_button.config(state=NORMAL)
    kick_button.config(state=NORMAL)
    ban_button.config(state=NORMAL)
    start_button.config(state=DISABLED)

    # create a thread to continuously listen for connections
    connect_thread = threading.Thread(target=connect_client, args=(connection,))
    connect_thread.start()


def end_server(connection):
    '''Begin the process of ending the server'''
    pass


def connect_client(connection):
    '''Connect an incoming client to the server'''
    while True:
        try:
            client_socket, client_address = connection.server_socket.accept()
            # check to see if the client's IP address is banned
            if client_address[0] in connection.banned_ips: # 'client_address' is a tuple consisting of client IP address & port number
                message_packet = create_message("DISCONNECT", "Admin (private)", "You have been banned...goodbye", light_green) # dictionary
                message_json = json.dumps(message_packet)
                client_socket.send(message_json.encode(connection.encoder)) # encoding string representation of dictionary to bytes obj

                # close the client socket
                client_socket.close()
            else:
                # send a message packet to receive client info
                message_packet = create_message("INFO", "Admin (private)", "Please send your name", light_green) # create message dict
                message_json = json.dumps(message_packet) # converting dict to str rep of dict; can't convert directly from dict to bytes obj with JSON like with pickle
                client_socket.send(message_json.encode(connection.encoder)) # encoding str rep of dict to bytes obj

                # wait for confirmation message to be sent verifying the connection
                message_json = client_socket.recv(connection.byte_size) # encoded bytes obj of a str rep of a dict
                process_message(connection, message_json, client_socket, client_address)
        # break out of loop if any errors
        except:
            break


def create_message(flag, name, message, color):
    '''Return a message packet to be sent'''
    # message packet in the form of a dictionary
    message_packet = {
        "flag": flag,
        "name": name,
        "message": message,
        "color": color,
    }

    return message_packet


def process_message(connection, message_json, client_socket, client_address=(0,0)):
    '''Update server information based on a message packet flag'''
    message_packet = json.loads(message_json) # decode & turn to dict in 1 step!
    flag = message_packet["flag"]
    name = message_packet["name"]
    message = message_packet["message"]
    color = message_packet["color"]

    if flag == "INFO":
        # add the new client info to the appropriate lists
        connection.client_sockets.append(client_socket)
        connection.client_ips.append(client_address[0]) # adds the client's IP address

        # broadcast the new client joining & update GUI
        message_packet = create_message("MESSAGE", "Admin (broadcast)", f"{name} has joined the server!", light_green) # creates message dict
        message_json = json.dumps(message_packet) # converting dict to str rep of dict
        broadcast_message(connection, message_json.encode(connection.encoder))

        # update server UI with the client's name & IP address
        client_listbox.insert(END, f"Name: {name}        IP Addr: {client_address[0]}") # add to end of chat history

        # now that a client has been established, start a thread to receive messages
        receive_thread = threading.Thread(target=receive_message, args=(connection, client_socket,))
        receive_thread.start()

    elif flag == "MESSAGE"
        pass
    elif flag == "DISCONNECT"
        pass
    else:
        # catch for errors
        history_listbox.insert(0, "Error processing message...") # insert at beginning of chat history




def broadcast_message(connection, message_json):
    "Send a message to all client sockets connected to the server...ALL JSON ARE ENCODED"
    for client_socket in connection.client_sockets:
        client_socket.send(message_json)


def receive_message(connection, client_socket):
    "Receive an incoming message from a client"
    pass


def self_broadcast(connection):
    "Broadcast a special admin message to all clients"
    pass


def private_message(connection):
    "Send a private message to a single client"
    pass


def kick_client(connection):
    "kick a given client off the server"
    pass


def ban_client(connection):
    "Ban a given client based on their IP address"
    pass


# define GUI layout
# create frames
connection_frame = tkinter.Frame(root, bg=black)
history_frame = tkinter.Frame(root, bg=black)
client_frame = tkinter.Frame(root, bg=black)
message_frame = tkinter.Frame(root, bg=black)
admin_frame = tkinter.Frame(root, bg=black)

connection_frame.pack(pady=5)
history_frame.pack()
client_frame.pack(pady=5)
message_frame.pack()
admin_frame.pack()

#connection frame layout
port_label = tkinter.Label(connection_frame, text="Port Number:", font=my_font, bg=black, fg=light_green)
port_entry = tkinter.Entry(connection_frame, width=10, borderwidth=3, font=my_font)
start_button = tkinter.Button(connection_frame, text="Start Server", borderwidth=5, width=15, font=my_font, bg=light_green, command=lambda:start_server(my_connection)) # 'lambda' means we can link this button to a function that takes in an arg
end_button = tkinter.Button(connection_frame, text="End Server", borderwidth=5, width=15, font=my_font, bg=light_green, state=DISABLED)

port_label.grid(row=0, column=0, padx=2, pady=10)
port_entry.grid(row=0, column=1, padx=2, pady=10)
start_button.grid(row=0, column=2, padx=5, pady=10)
end_button.grid(row=0, column=3, padx=5, pady=10)

# history frame layout to display chat history
history_scrollbar = tkinter.Scrollbar(history_frame, orient=VERTICAL)
history_listbox = tkinter.Listbox(history_frame, height=10, width=55, borderwidth=3, font=my_font, bg=black, fg=light_green, yscrollcommand=history_scrollbar.set) # my listbox outline doesn't display like in the tutorial
# to synchronize the scroll bar & listbox so that the scroll bar changes the vertical view of the listbox
history_scrollbar.config(command=history_listbox.yview)

history_listbox.grid(row=0, column=0)
history_scrollbar.grid(row=0, column=1, sticky="NS") # 'sticky="NS"' attribute expands scroll bar vertically north & south

# client frame layout
client_scrollbar = tkinter.Scrollbar(client_frame, orient=VERTICAL)
client_listbox = tkinter.Listbox(client_frame, height=10, width=55, borderwidth=3, font=my_font, bg=black, fg=light_green, yscrollcommand=client_scrollbar.set) # my listbox outline doesn't display like in the tutorial
# to synchronize the scroll bar & listbox so that the scroll bar changes the vertical view of the listbox
client_scrollbar.config(command=client_listbox.yview)

client_listbox.grid(row=0, column=0)
client_scrollbar.grid(row=0, column=1, sticky="NS") # 'sticky="NS"' attribute expands scroll bar vertically north & south

# message frame layout
input_entry = tkinter.Entry(message_frame, width=40, borderwidth=3, font=my_font)
self_broadcast_button = tkinter.Button(message_frame, text="Broadcast", width=13, borderwidth=5, font=my_font, bg=light_green, state=DISABLED)

input_entry.grid(row=0, column=0, padx=5, pady=5)
self_broadcast_button.grid(row=0, column=1, padx=5, pady=5)

# admin frame layout
message_button = tkinter.Button(admin_frame, text="PM", borderwidth=5, width=15, font=my_font, bg=light_green, state=DISABLED)
kick_button = tkinter.Button(admin_frame, text="Kick", borderwidth=5, width=15, font=my_font, bg=light_green, state=DISABLED)
ban_button = tkinter.Button(admin_frame, text="Ban", borderwidth=5, width=15, font=my_font, bg=light_green, state=DISABLED)

message_button.grid(row=0, column=0, padx=5, pady=5)
kick_button.grid(row=0, column=1, padx=5, pady=5)
ban_button.grid(row=0, column=2, padx=5, pady=5)


# create a 'Connection()' class obj & run the root window's mainloop()
my_connection = Connection()
root.mainloop()

