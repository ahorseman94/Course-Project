#calendar module

import tkinter as tk
from tkcalendar import DateEntry
my_w = tk.Tk()
my_w.geometry("340x220")
sel=tk.StringVar() #declaring string variable

cal = DateEntry(my_w,selectmode="day", textvariable=sel)
cal.grid(row=1,column=1,padx=20)

def my_upd(*args): #triggered when string variable changes
   l1.config(text=sel.get()) 

def print_sel(e):
    dt=cal.get_date()
    str_dt=dt.strftime("%d-%B-%Y") #format
    l1.config(text=str_dt)
    print(str_dt)
cal.bind("<<DateEntrySelected>>", print_sel)

def delivery_date():
    print(print_sel)

l1=tk.Label(my_w,bg="yellow") #label to display date
l1.grid(row=1,column=2)

sel.trace("w",my_upd) #on change of string variable
my_w.mainloop()
