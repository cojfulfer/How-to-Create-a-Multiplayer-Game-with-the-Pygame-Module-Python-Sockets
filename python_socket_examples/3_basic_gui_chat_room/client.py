# Client Side GUI Chat Room
import tkinter, socket, threading
from tkinter import DISABLED, VERTICAL


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


# define functions
def connect():
    '''Connect to a server at a given ip/port address'''
    pass


def verify_connection():
    '''Verify that the server connection is valid & pass required information'''
    pass


def disconnect():
    "Disconnect from the server"
    pass


def send_message():
    "Send a message to the server to be broadcast"
    pass


def receive_message():
    "Receive an incoming message from the server"
    pass


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
connect_button = tkinter.Button(info_frame, text="Connect", font=my_font, bg=light_green, borderwidth=5, width=10)
disconnect_button = tkinter.Button(info_frame, text="Disconnect", font=my_font, bg=light_green, borderwidth=5, width=10, state=DISABLED) # disable disconnect button until a valid connection has been established

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

# place the widgets onto the info frame via the grid system
my_listbox.grid(row=0, column=0)
my_scrollbar.grid(row=0, column=1, sticky="NS")


# input frame layout
input_entry = tkinter.Entry(input_frame, width=45, borderwidth=3, font=my_font)
send_button = tkinter.Button(input_frame, text="send", borderwidth=5, width=10, font=my_font, bg=light_green, state=DISABLED) # disable send button until a valid connection has been established

# place the widgets onto the info frame via the grid system
input_entry.grid(row=0, column=0, padx=5, pady=5)
send_button.grid(row=0, column=1, padx=5, pady=5)



# run the root window's mainloop()
root.mainloop()