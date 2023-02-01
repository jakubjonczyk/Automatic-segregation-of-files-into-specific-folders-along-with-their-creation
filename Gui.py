from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os

# folder path
dir_path =os.getcwd()
dir_path = dir_path + "\\Code.py"

# Create a function
def open_file():
    os.system(dir_path)

# Create an instance
win= Tk()

# Set window fullscreen
win.attributes('-fullscreen',True)

# Add a label 
Label(win, text= "Choose what you want to do", font= ('Aerial 17 bold italic')).pack(pady= 30)

# Create a Button to run file
ttk.Button(win, text='Copy pdfs from dir', command=open_file).pack(pady= 20)

# Create a Button to exit
exit_button = Button(win, text="Exit", command=win.destroy)
exit_button.pack(pady=20)

# mainloop
win.mainloop()





