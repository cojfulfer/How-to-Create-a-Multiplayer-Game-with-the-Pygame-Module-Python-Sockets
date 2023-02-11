# Client Side GUI Chat Room
import tkinter, socket, threading
from tkinter import DISABLED, VERTICAL, END, NORMAL


# define window
root = tkinter.Tk()
root.title("Chat Client")
root.iconbitmap("message_icon.png")
root.geometry("600x600")
root.resizable(0,0)


# define fonts & colors
my_font = ('SimSun', 14)
black = "#010101"
light_green = "#1fc742"
root.config(bg=black)


# define socket constants
ENCODER = 'utf-8'
BYTE_SIZE = 1024
global client_socket # 'global' means not restricted to 1 function; any changes made to this variable within a function will carry over to all other functions


# define functions
def connect():
    '''Connect to a server at a given ip/port address'''
    global client_socket 

    # clear any previous chats
    my_listbox.delete(0, END) # delete listbox contents from row index 0 to the last row index

    # get the required connection information
    # 'get()' function returns the input of an Entry class obj in a string format
    name = name_entry.get()
    ip = ip_entry.get() # 192.168.1.253 is local IP address
    port = port_entry.get()

    # only try to make a connection if all 3 fields are filled in
    if name and ip and port: # if all 3 have values associated with them
        # conditions for connection are met, try for connection
        my_listbox.insert(0, f'{name} is waiting to connect to {ip} at {port}...') # insert this message at row index 0 (top) of the listbox

        # create a client socket to connect to the server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((ip, int(port))) # must convert port address from string to integer

        # # what I would have done:
        # try:
        #     client_socket.connect((ip, int(port))) # must convert port address from string to integer
        # except ConnectionRefusedError: # no verification message was received
        #     my_listbox.insert(0, "Invalid connection. Goodbye...")  # insert this message at row index 0 (top) of the listbox
        #     client_socket.close()

        # verify that the connection is valid
        verify_connection(name)
    else:
        # conditions for connection were not met
        my_listbox.insert(0, "Insufficient information for connection...") # insert this message at row index 0 (top) of the listbox


def verify_connection(name):
    '''Verify that the server connection is valid & pass required information'''
    global client_socket

    # the server will send a NAME flag if a valid connection is made
    flag = client_socket.recv(BYTE_SIZE).decode(ENCODER) # the string "NAME"

    if flag == 'NAME':
        # the connection was made, send client name & await verification
        client_socket.send(name.encode(ENCODER))
        message = client_socket.recv(BYTE_SIZE).decode(ENCODER) # "[name], you have connected to the server!"

        if message: # if the server sent a message, display it
            # server sent a verification, connection is valid!
            my_listbox.insert(0, message) # insert this message at row index 0 (top) of the listbox

            # change button states
            connect_button.config(state=DISABLED)
            disconnect_button.config(state=NORMAL) # 'NORMAL' means 'ENABLED'
            send_button.config(state=NORMAL)
            # change entry states
            name_entry.config(state=DISABLED)
            ip_entry.config(state=DISABLED)
            port_entry.config(state=DISABLED)

            # create a thread to continuously receive messages from the server
            receive_thread = threading.Thread(target=receive_message)
            receive_thread.start()

        else:
            # no verification message was received
            my_listbox.insert(0, "Connection not verified. Goodbye...") # insert this message at row index 0 (top) of the listbox
            client_socket.close()

    else:
        # no name flag was sent, connection was refused # my program doesn't reach this when entering an invalid port number
        my_listbox.insert(0, "Invalid connection. Goodbye...") # technically, the connection was 'invalid' not 'refused' as no server would exist at the address the client enters # insert this message at row index 0 (top) of the listbox
        client_socket.close()


def disconnect():
    "Disconnect from the server"
    global client_socket

    # close the socket
    client_socket.close()

    # change button states
    connect_button.config(state=NORMAL) # 'NORMAL' means 'ENABLED'
    disconnect_button.config(state=DISABLED)
    send_button.config(state=DISABLED)
    # change entry states
    name_entry.config(state=NORMAL)
    ip_entry.config(state=NORMAL)
    port_entry.config(state=NORMAL)


def send_message():
    "Send a message to the server to be broadcast"
    global client_socket

    # send the message to the server
    message = input_entry.get() # what the user enters into the input entry as a string
    client_socket.send(message.encode(ENCODER))

    # clear the input entry
    input_entry.delete(0, END)


def receive_message():
    "Receive an incoming message from the server"
    global client_socket

    while True:
        try:
            # receive an incoming message from the server
            message = client_socket.recv(BYTE_SIZE).decode(ENCODER)
            my_listbox.insert(0, message)
        except:
            # an error occured, disconnect from the server
            my_listbox.insert(0, "Closing the connection. Goodbye...")
            disconnect()
            break


# define GUI layout
# create frames
info_frame = tkinter.Frame(root, bg=black) # for the client/user to input their name along with the ip & port address of the server that they want to connect to
output_frame = tkinter.Frame(root, bg=black) # to display the sent messages
input_frame = tkinter.Frame(root, bg=black) # for the client/user to input and send their message

# place the frames onto the root window via the pack system
info_frame.pack()
output_frame.pack(pady=10) # output frame will take up the majority of the space
input_frame.pack()


# info frame layout
name_label = tkinter.Label(info_frame, text="Client Name:", font=my_font, fg=light_green, bg=black)
name_entry = tkinter.Entry(info_frame, borderwidth=3, font=my_font)
ip_label = tkinter.Label(info_frame, text="Host IP:", font=my_font, fg=light_green, bg=black)
ip_entry = tkinter.Entry(info_frame, borderwidth=3, font=my_font)
port_label = tkinter.Label(info_frame, text="Port Num:", font=my_font, fg=light_green, bg=black)
port_entry = tkinter.Entry(info_frame, borderwidth=3, font=my_font, width=10)
connect_button = tkinter.Button(info_frame, text="Connect", font=my_font, bg=light_green, borderwidth=5, width=10, command=connect) # when button is pressed, 'connect()' function is called # my button is white instead of light green...
disconnect_button = tkinter.Button(info_frame, text="Disconnect", font=my_font, bg=light_green, borderwidth=5, width=10, state=DISABLED, command=disconnect) # disable disconnect button until a valid connection has been established # when button is pressed, 'disconnect()' function is called # my button is white instead of light green...

# place the widgets onto the info frame via the grid system
name_label.grid(row=0, column=0, padx=2, pady=10)
name_entry.grid(row=0, column=1, padx=2, pady=10)
port_label.grid(row=0, column=2, padx=2, pady=10)
port_entry.grid(row=0, column=3, padx=2, pady=10)
ip_label.grid(row=1, column=0, padx=2, pady=5)
ip_entry.grid(row=1, column=1, padx=2, pady=5)
connect_button.grid(row=1, column=2, padx=4, pady=5)
disconnect_button.grid(row=1, column=3, padx=4, pady=5)


# output frame layout
my_scrollbar = tkinter.Scrollbar(output_frame, orient=VERTICAL) # define scroll bar to scroll through sent messages
my_listbox = tkinter.Listbox(output_frame, height=20, width=55, borderwidth=3, bg=black, fg=light_green, font=my_font, yscrollcommand=my_scrollbar.set) # the container that holds the sent messages; my listbox outline doesn't display like in the tutorial
my_scrollbar.config(command=my_listbox.yview) # to synchronize the scroll bar & listbox so that the scroll bar changes the vertical view of the listbox

# place the widgets onto the output frame via the grid system
my_listbox.grid(row=0, column=0)
my_scrollbar.grid(row=0, column=1, sticky="NS") # 'sticky="NS"' attribute expands scroll bar vertically north & south


# input frame layout
input_entry = tkinter.Entry(input_frame, width=45, borderwidth=3, font=my_font)
send_button = tkinter.Button(input_frame, text="send", borderwidth=5, width=10, font=my_font, bg=light_green, state=DISABLED, command=send_message) # disable send button until a valid connection has been established # when button is pressed, 'connect()' function is called # my button is white instead of light green...

# place the widgets onto the input frame via the grid system
input_entry.grid(row=0, column=0, padx=5, pady=5)
send_button.grid(row=0, column=1, padx=5, pady=5)



# run the root window's mainloop()
root.mainloop() # calls the functions of the Tk() class