# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
from view.Create_a_w import Create_a_w
from view.auc_view_w import Auc_view_w
from controller.walletcontroller import WalletController
from model.user import c_user

def wal_w(frame):
    def update():
        for wal in view_tbl.get_children(""):
            view_tbl.delete(wal)
        for wal in WalletController.get_wallets(c_user[0].ID,nm.get()):
            view_tbl.insert("", END, values=wal)
            
    ttk.Label(frame,text="Ваши электронные кошельки").pack()
    s=ttk.Frame(frame)
    s.pack()
    nm=ttk.Entry(s,width=50)
    nm.pack()
    ttk.Button(s,text="s",width=50,command=update).pack()
    ttk.Button(s,text="Добавить",width=50,command=Add_wal_w).pack()
    col=("tp","nm","bl")
    view_tbl=ttk.Treeview(frame,columns=col,show="headings")
    view_tbl.pack()
    view_tbl.heading("tp",text="тип",anchor=W)
    view_tbl.heading("nm",text="имя",anchor=W)
    view_tbl.heading("bl",text="баланс",anchor=W)
    view_tbl.column("#1",stretch=NO,width=50)
    view_tbl.column("#2",stretch=NO,width=100)
    view_tbl.column("#3",stretch=NO,width=100)

    scrollbar = ttk.Scrollbar(frame,orient=VERTICAL, command=view_tbl.yview)
    view_tbl.configure(yscroll=scrollbar.set)
    scrollbar.pack()
    #def auc_selected(event):
        #Auc_view_w(view_tbl.item(view_tbl.selection()[0])["values"][0])
 
    #view_tbl.bind("<<TreeviewSelect>>", auc_selected)

class Add_wal_w(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x200")
        ttk.Label(self,text="Кошелёк").pack(anchor=N,pady=10)
        ttk.Label(self,text="Тип").pack(anchor=NW)
        self.tp=ttk.Combobox(self,values=WalletController.get_MoneyType())
        self.tp.pack(anchor=NW)
        ttk.Label(self,text="Имя").pack(anchor=NW)
        self.nm=ttk.Entry(self,width=50)
        self.nm.pack()
        self.ch=ttk.Label(self)
        self.ch.pack(anchor=NW)
        ttk.Button(self,text="Привязать кошелёк",command=self.add).pack()

    def add(self):
        tmpl=WalletController.add(self.tp.get(),c_user[0].ID,self.nm.get())
        if(not tmpl[0]):
            self.ch["text"]=tmpl[1]
        else:
            self.destroy()
