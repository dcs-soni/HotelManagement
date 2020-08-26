from tkinter import *
import time
from tkinter import ttk

root = Tk()
root.geometry('1400x800+0+0')
root.title("Hotel Management System")

#------------------------------------Window's Partitions--------------------

Tops = Frame(root,width=1600,height=100, bg='blue',relief=SUNKEN)
Tops.pack(side=BOTTOM)

f1 = Frame(root,width=800, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width=300, height=700,relief=SUNKEN)
f2.pack(side=RIGHT)

f3 = Frame(root, width=35, height=700, relief=SUNKEN)
f3.pack(side=LEFT)

f4 = Frame(root, width=100, height=700, relief=SUNKEN)
f4.pack(side=LEFT)

#----------------------------------Main Screen----------------------------------
txt_input = StringVar(value='Hotel Management System')
Display = Entry(Tops,font=('arial',80,'bold'),fg='white',bd=20,bg='blue',justify='right',
                textvariable=txt_input)
Display.grid(columnspan=1)
#Comment








root.mainloop()