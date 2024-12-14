from tkinter import *
from tkinter import ttk
from controller.auctioncontroller import AuctionController
from controller.walletcontroller import WalletController
from model.user import c_user

class Auc_view_w(Tk):
    def __init__(self,ID:int):
        super().__init__()
        self.auc=AuctionController.get_auction(ID)
        self.geometry("500x200")
        self.fi=ttk.Frame(self)
        self.fi.grid()
        ttk.Label(self.fi,text=self.auc[1]).grid(row=0,column=0,sticky=W)
        ttk.Label(self.fi,text=f"Лот: {self.auc[6]}").grid(row=1,column=0,sticky=W)
        ttk.Label(self.fi,text=f"Текущая ставка: {self.auc[4]} $").grid(row=2,column=0,sticky=W)
        ttk.Button(self.fi,text="Участвовать",command=self.participate).grid(row=2,column=2,sticky=E)
        ttk.Label(self.fi,text="Описание аукциона").grid(row=3,column=0,sticky=W)
        ttk.Label(self.fi,text=f"Начало: {self.auc[2]}").grid(row=0,column=1,sticky=W)
        ttk.Label(self.fi,text=f"Окончание: {self.auc[3]}").grid(row=1,column=1,sticky=W)
        ttk.Label(self.fi,text=f"Создатель: {self.auc[5]}").grid(row=0,column=2,rowspan=2,sticky=W)
        ttk.Label(self.fi,text=f"{self.auc[7]}",wraplength=600).grid(row=4,column=0,columnspan=3,sticky=W)

    def participate(self):
        Participate_w(self.auc[0],self.auc[4])
        self.destroy()

class Participate_w(Tk):
    def __init__(self,ID:int,c_bet:float):
        super().__init__()
        self.geometry("500x200")
        self.ID=ID
        self.c_bet=c_bet
        ttk.Label(self,text="Учасник").pack(anchor=N,pady=10)
        ttk.Label(self,text="Способ оплаты").pack(anchor=NW)
        self.paym=ttk.Combobox(self,values=WalletController.get_wallets_names(c_user[0].ID))
        self.paym.pack(anchor=NW)
        ttk.Label(self,text="Ставка").pack(anchor=NW)
        self.bet=ttk.Entry(self,width=50)
        self.bet.pack()
        self.bet.insert(0,c_bet)
        self.ch=ttk.Label(self)
        self.ch.pack(anchor=NW)
        ttk.Button(self,text="Принять участие",command=self.participate).pack()

    def participate(self):
        tmpl=WalletController.get_balance(c_user[0].ID,self.paym.get(),float(self.bet.get()))
        if(tmpl[0]):
            self.ch["text"]=AuctionController.new_bet(self.ID,c_user[0].ID,float(self.bet.get()),self.c_bet)
            self.destroy()
        else:
            self.ch["text"]=tmpl[1]
