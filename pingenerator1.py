import tkinter as tk
from tkinter import filedialog
from tkinter import *
import random

window = tk.Tk()
window.geometry("1950x1080")
window.title("Pin Generator 1.0")
window.iconbitmap('d:/untitled - 3.ico')


window.grid_columnconfigure(0, weight=1)

#class Menubar:

def __init__(self, parent):
    font_specs = ("arial", 26)

    menubar = tk.Menu(parent.master, font=font_specs)
    parent.master.config(menu=menubar)

    file_dropdown.add_separator()
    file_dropdown.add_command(label ="Exit",
                                  command=parent.master.destroy)

    menubar.add_cascade(label="file", menu=file_dropdown)

#class window:
    #def __init__(self, master):
        #master.geometry("1950x1080")

#self.menubar = Menubar(self)

welcome_label = tk.Label(window,
                         text="Welcome To Pin Generator",
                         pady=10, font=("arial", 16))
welcome_label.grid(row=0, column=0, sticky="n", padx=20, pady=10)
 

for number in range(1):
    pinna = random.randint(1000,9999)

def pin():
    text =(pinna)
    text_output = tk.Label(window, text=text, fg="blue", font=("arial", 37))
    text_output.grid(row=6, column=0)

button1 = tk.Button(text="Show Pin", command=pin)
button1.grid(row=4, column=0)

#print("your pin is:" + str(random.randint(1000,9999)))


if __name__== "__main__":
    window.mainloop()
