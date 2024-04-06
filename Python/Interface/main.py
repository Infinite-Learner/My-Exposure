from tkinter import *
from PIL import *
import tkinter as t
tk1 = t.Tk()
tk1.title('Demo App')
tk1.geometry("680x480")
frm1 = Frame(tk1,bg = "Yellow",border=4,borderwidth=5,highlightbackground='red',width=500,height=100)
frm1.pack()
lb1  = Label(frm1,text="ITS ME ELANGO")
lb1.pack()

t.mainloop()
