# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk

class Create_a_w(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("250x200")
        ttk.Label(self,text="Создание нового аукциона").grid()
        self.inp=ttk.Frame(self)
        self.inp.grid()
        ttk.Label(self.inp,text="Название аукциона").grid()
        self.nm=ttk.Entry(self.inp,width=40).grid()
        ttk.Label(self.inp,text="Название лота").grid()
        self.ps=ttk.Entry(self.inp,width=40).grid()
        ttk.Label(self.inp,text="Описание").grid()
        self.ps=ttk.Entry(self.inp,width=40).grid()
        ttk.Button(self.inp,text="Загрузить изображение").grid()

        self.date=ttk.Frame(self)
        self.b=ttk.Frame(self.date)
        self.e=ttk.Frame(self.date)
        self.a=ttk.Frame(self.date)
        self.date.grid()
        self.b.grid(row=0,column=0)
        self.e.grid(row=0,column=1)
        self.a.grid(row=0,column=2)
        ttk.Label(self.b,text="Начало").grid(row=0,column=0)
        ttk.Label(self.e,text="Окончание").grid(row=0,column=1)
        ttk.Label(self.a,text="Начальная ставка").grid(row=0,column=2)
        self.eb=ttk.Entry(self.b,width=10).grid(row=1,column=0)
        self.ee=ttk.Entry(self.e,width=10).grid(row=1,column=1)
        self.ea=ttk.Entry(self.a,width=10).grid(row=1,column=2)
        ttk.Button(self,text="Создать новый аукцион",command=self.create).grid()

    def open_enter(self):
        self.destroy()
        
    def create(self):
        self.destroy()
