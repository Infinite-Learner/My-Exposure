import tkinter as tk
from tkinter import *

def login():
    login_frame = tk.Tk()
    login_frame.title("Library_Management_System : Login")
    login_frame.geometry('720x720')
    login_frame.anchor('se')
    login_frame.configure(background="darkblue")
    login_frame.resizable(False,True)
    frame = Frame(login_frame,height=350,bg='lightgray',width=600,padx = 20,borderwidth=9,relief=tk.RIDGE)
    frame.place_configure(x=70,y=90)
    frame.pack_propagate(True)
    log_lb = Label(frame,text = "Login To Access",height=5,width=75)
    log_lb.place_configure(x=30,y=10)
    login_frame.mainloop()


login()