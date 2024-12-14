from tkinter import *
from tkinter import ttk
from view.acc_w import acc_w
from view.sec_w import sec_w
from view.auc_w import auc_w
from view.wal_w import wal_w
from view.story_w import story_w

class Buyer_w(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x200")
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill=BOTH)

        self.auc = ttk.Frame(self.notebook)
        self.wal = ttk.Frame(self.notebook)
        self.str = ttk.Frame(self.notebook)
        self.sec = ttk.Frame(self.notebook)
        self.acc = ttk.Frame(self.notebook)

        self.auc.pack(fill=BOTH, expand=True)
        self.wal.pack(fill=BOTH, expand=True)
        self.str.pack(fill=BOTH, expand=True)
        self.sec.pack(fill=BOTH, expand=True)
        self.acc.pack(fill=BOTH, expand=True)

        acc_w(self.acc)
        sec_w(self.sec)
        auc_w(self.auc)
        wal_w(self.wal)
        story_w(self.str)
        
        self.notebook.add(self.auc, text="Аукционы")
        self.notebook.add(self.wal, text="Электронный кошелёк")
        self.notebook.add(self.str, text="Истроия")
        self.notebook.add(self.sec, text="Безопасность")
        self.notebook.add(self.acc, text="Аккаунт")
