# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
from view.Create_a_w import Create_a_w
from view.auc_view_w import Auc_view_w
from controller.usercontroller import UserController

def story_w(frame):
    def update():
        for auc in view_tbl.get_children(""):
            view_tbl.delete(auc)
        for auc in UserController.get_story(nm.get()):
            view_tbl.insert("", END, values=auc)
            
    ttk.Label(frame,text="Аукционы").pack()
    s=ttk.Frame(frame)
    s.pack()
    nm=ttk.Entry(s,width=50)
    nm.pack()
    x=ttk.Button(s,text="s",width=50,command=update)
    x.pack()
    col=("id","nm","ln","sd","ed","cb")
    view_tbl=ttk.Treeview(frame,columns=col,show="headings")
    view_tbl.pack()
    view_tbl.heading("id",text="id",anchor=W)
    view_tbl.heading("nm",text="аукцион",anchor=W)
    view_tbl.heading("ln",text="лот",anchor=W)
    view_tbl.heading("sd",text="начало",anchor=W)
    view_tbl.heading("ed",text="окончание",anchor=W)
    view_tbl.heading("cb",text="текущая ставка",anchor=W)
    view_tbl.column("#1",stretch=NO,width=30)
    view_tbl.column("#2",stretch=NO,width=100)
    view_tbl.column("#3",stretch=NO,width=100)
    view_tbl.column("#4",stretch=NO,width=60)
    view_tbl.column("#5",stretch=NO,width=60)
    view_tbl.column("#6",stretch=NO,width=100)

    scrollbar = ttk.Scrollbar(frame,orient=VERTICAL, command=view_tbl.yview)
    view_tbl.configure(yscroll=scrollbar.set)
    scrollbar.pack()
    def auc_selected(event):
        Auc_view_w(view_tbl.item(view_tbl.selection()[0])["values"][0])
            #person = item["values"]
            #selected_people = f"{selected_people}{person}\n"
        #x["text"]=selected_people
 
    view_tbl.bind("<<TreeviewSelect>>", auc_selected)
    #ttk.Button(self.s,text="Создать аукцион",command=self.open_create).grid()
    
def open_create():
    Create_a_w()
