from tkinter import *
from tkinter import ttk

def navBar(window):
    nav = ttk.Notebook(window)

    tab1 = ttk.Frame(nav)
    tab2 = ttk.Frame(nav)

    nav.add(tab1,text="INSERT")
    nav.add(tab2,text="SELECT")

    label1 = Label(tab1, text="Insert")
    label1.pack(padx=10, pady=10)

    label2 = Label(tab2, text="Select")
    label2.pack(padx=10, pady=10)

    nav.pack(expand=True,fill=Tk.BOTH)

    return nav

