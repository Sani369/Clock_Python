# 
from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("clock")

def time():
    String = strftime('%H:%M:%S %p')
    Label.config(text=String)
    Label.after(1000,time)


Label = Label(root, font=("",80), background="black",foreground="green")
Label.pack(anchor='center')
time()


mainloop()

