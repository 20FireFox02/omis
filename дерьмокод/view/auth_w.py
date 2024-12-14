# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
from view.buyer_w import Buyer_w
from controller.authcontroller import AuthController

class Auth_w(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("250x200")
        ttk.Label(self,text="AUCtion").pack(anchor=N,pady=10)
        self.ch_lbl=ttk.Label(self,text="")
        self.ch_lbl.pack(anchor=W)
        self.inp=ttk.Frame(self).pack(anchor=N,pady=10)
        ttk.Label(self.inp,text="Имя").pack(anchor=NW)
        self.nm=ttk.Entry(self.inp,width=40)
        self.nm.pack(anchor=N)
        ttk.Label(self.inp,text="Пароль").pack(anchor=NW)
        self.ps=ttk.Entry(self.inp,width=40)
        self.ps.pack(anchor=N)
        ttk.Button(self.inp,text="Войти",command=self.user_check).pack(anchor=N)
        ttk.Label(self.inp,text="Также вы можете").pack(anchor=NW)
        ttk.Button(self.inp,text="Создать новый аккаунт",command=self.open_reg_w).pack(anchor=N)

    def user_check(self):
        tmpl=AuthController.handle_login(self.nm.get(),self.ps.get())
        if(tmpl[0]):
            self.open_buyer_w()
        else:
            self.ch_lbl["text"]=tmpl[1]
        
    def open_buyer_w(self):
        Buyer_w()
        self.destroy()
        
    def open_reg_w(self):
        Reg_w()
        self.destroy()

class Reg_w(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("250x200")
        ttk.Label(self,text="AUCtion").pack(anchor=N)
        ttk.Label(self,text="Регистрация").pack(anchor=N)
        self.ch_lbl=ttk.Label(self,text="")
        self.ch_lbl.pack(anchor=W)
        ttk.Label(self,text="Имя").pack(anchor=N)
        self.nm=ttk.Entry(self,width=40)
        self.nm.pack(anchor=N)
        ttk.Label(self,text="Пароль").pack(anchor=N)
        self.ps=ttk.Entry(self,width=40)
        self.ps.pack(anchor=N)
        ttk.Button(self,text="Создать",command=self.user_check).pack(anchor=N)
        ttk.Button(self,text="У меня уже есть аккаунт",command=self.open_auth_w).pack(anchor=N)

    def user_check(self):
        tmpl=AuthController.handle_register(self.nm.get(),self.ps.get(),'img')
        if(tmpl[0]):
            self.open_buyer_w()
        else:
            self.ch_lbl["text"]=tmpl[1]

    def open_buyer_w(self):
        Buyer_w()
        self.destroy()

    def open_auth_w(self):
        Auth_w()
        self.destroy()  
