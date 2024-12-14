# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk

def sec_w(frame):
    ttk.Label(frame,text="Смена пароля").pack()
       
    inp=ttk.Frame(frame)
    inp.pack()
    ttk.Label(inp,text="Старый пароль").pack()
    op=ttk.Entry(inp,width=40)
    op.pack()
    ttk.Label(inp,text="Новый пароль").pack()
    np=ttk.Entry(inp,width=40)
    np.pack()
    ch=ttk.Label(inp)
    ch.pack()
    ttk.Button(frame,text="Подтвердить изменения",command=edit).pack()
        
def edit():
    ch["text"]=UserController.update_user_pass(nm.get(),dn.get())
