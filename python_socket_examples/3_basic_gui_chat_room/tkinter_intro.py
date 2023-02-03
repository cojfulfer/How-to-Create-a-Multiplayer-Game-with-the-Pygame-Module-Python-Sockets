# Tkinter introduction
import tkinter
from tkinter import BOTH, StringVar

# define window
root = tkinter.Tk()
root.title("Let's Chat")
root.iconbitmap('blue_talk.png')
root.geometry('400x600')
root.resizable(0,0)

# define colors (in hexadecimal)
root_color = "#535657" # R:83, G:86, B:87 (very dark grayish cyan)
input_color = "#4f646f" # R:79, G:100, B:111 (very dark grayish blue)
output_color = "#dee7e7" # R:222, G:231, B:231 (light grayish cyan)
root.config(bg=root_color)

# define functions


# define GUI layout
# define frames (that are placed onto the root window)
input_frame = tkinter.LabelFrame(root, bg=input_color)
output_frame = tkinter.LabelFrame(root, bg=output_color)
# place these frames onto the root window via the pack system
input_frame.pack(pady=10)
output_frame.pack(padx=10, pady=(0,10), fill=BOTH, expand=True)

# define widgets (that are placed onto the frames)
message_entry = tkinter.Entry(input_frame, text="Enter a message", width=30)
send_button = tkinter.Button(input_frame, text="Send")
# place these widgets onto the input frame via the grid system
message_entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
send_button.grid(row=0, column=3, rowspan=2, padx=10, pady=10) # did not include "ipadx=20, ipady=5" as the button gets cut off

text_color = StringVar() # 'text_color' is a string variable object of the 'StringVar()' class
text_color.set("#ff0000") # sets 'text_color' to the value red by default
# these Radiobutton widgets will track the string variable object 'text_color'
# the value of this string variable obj is expressed as a string, in this case text colors are defined as strings
red_button = tkinter.Radiobutton(input_frame, text="Red", variable=text_color, value="#ff0000", bg=input_color)
green_button = tkinter.Radiobutton(input_frame, text="Green", variable=text_color, value="#00ff00", bg=input_color)
blue_button = tkinter.Radiobutton(input_frame, text="Blue", variable=text_color, value="#0000ff", bg=input_color)
# place these Radiobutton widgets onto the input frame via the grid system
red_button.grid(row=1, column=0)
green_button.grid(row=1, column=1)
blue_button.grid(row=1, column=2)

# creates the "---Stored Messages---" header for the output messages
output_label = tkinter.Label(output_frame, text="---Stored Messages---", fg=input_color, bg=output_color, font=('Helvetica bold', 18)) # foreground color is text color
output_label.pack(pady=15)

# run the root window's mainloop()
root.mainloop()