# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from model.user import User

def acc_w(frame):
    ttk.Label(frame,text="Аккаунт").pack()
    inp=ttk.Frame(frame)
    inp.pack()
    ttk.Label(inp,text="Имя").pack()
    nm=Text(inp,width=40,height=1)
    nm.pack()
    ttk.Label(inp,text="Описание").pack()
    dn=Text(inp,width=40,height=5)
    dn.pack()
    ch=ttk.Label(inp)
    ch.pack()
    #photo = ImageTk.PhotoImage(Image.open("img\\us1.jpg")) 
    # Resizing image to fit on button 
    ttk.Button(frame,text="Подтвердить изменения",command=edit).pack()
        
def edit():
    ch["text"]=UserController.update_user_desc(nm.get(),dn.get())
