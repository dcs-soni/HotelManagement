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
Display = Entry(Tops,font=('arial',80,'bold'),fg='white',bd=20,bg='blue',justify='right',textvariable=txt_input)

Display.grid(columnspan=1)


#--------------------------------Date and Time------------------------------------

localtime = time.asctime(time.localtime(time.time()))

lblInfo = Label(f2,font=('arial',20,'bold'), text=localtime,fg='dark blue', bd=10, anchor=W)
lblInfo.grid(row=0,column=0,columnspan=4)


#------------------------------Row 1----------------------------------------------
btn7 = Button(f2,padx=15,pady=5,bd=8,fg='black',font=('arial',20,'bold'),text='7').grid(row=1,column=0)
btn8 = Button(f2,padx=15,pady=5,bd=8,fg='black',font=('arial',20,'bold'),text='8').grid(row=1,column=1)
btn9 = Button(f2,padx=15,pady=5,bd=8,fg='black',font=('arial',20,'bold'),text='9').grid(row=1,column=2)
btnC = Button(f2,padx=15,pady=5,bd=8,fg='black',font=('arial',20,'bold'),text='C',bg='green').grid(row=1,column=3)

#------------------------------Row 2----------------------------------------------

btn4 = Button(f2,padx=15,pady=5,bd=8,fg='black',font=('arial',20,'bold'),text='4').grid(row=2,column=0)
btn5 = Button(f2,padx=15,pady=5,bd=8,fg='black',font=('arial',20,'bold'),text='5').grid(row=2,column=1)
btn6 = Button(f2,padx=15,pady=5,bd=8,fg='black',font=('arial',20,'bold'),text='6').grid(row=2,column=2)
btnplus = Button(f2,padx=18,pady=5,bd=8,fg='black',font=('arial',20,'bold'),text='+',bg='orange').grid(row=2,column=3)

#------------------------------Row 3----------------------------------------------

btn1 = Button(f2,padx=15,pady=5,bd=8,fg='black',font=('arial',20,'bold'),text='1').grid(row=3,column=0)
btn2 = Button(f2,padx=15,pady=5,bd=8,fg='black',font=('arial',20,'bold'),text='2').grid(row=3,column=1)
btn3 = Button(f2,padx=15,pady=5,bd=8,fg='black',font=('arial',20,'bold'),text='3').grid(row=3,column=2)
btnminus = Button(f2,padx=23,pady=5,bd=8,fg='black',font=('arial',20,'bold'),text='-',bg='orange').grid(row=3,column=3)

#------------------------------Row 4----------------------------------------------

btn0 = Button(f2,padx=15,pady=5,bd=8,fg='black',font=('arial',20,'bold'),text='0').grid(row=4,column=0)
btndot = Button(f2,padx=21,pady=5,bd=8,fg='black',font=('arial',20,'bold'),text='.',bg='orange').grid(row=4,column=1)
btndivision = Button(f2,padx=20,pady=5,bd=8,fg='black',font=('arial',20,'bold'),text='/',bg='orange').grid(row=4,column=2)
btnmultiply = Button(f2,padx=19,pady=5,bd=8,fg='black',font=('arial',20,'bold'),text='*',bg='orange').grid(row=4,column=3)

#------------------------------Row 5----------------------------------------------

btnequals = Button(f2,padx=64,pady=2,bd=8,fg='black',font=('arial',20,'bold'),text='=',bg='green').grid(row=5,column=0,columnspan=2)
btnopenbracket = Button(f2,padx=19,pady=2,bd=8,fg='black',font=('arial',20,'bold'),text='(',bg='orange').grid(row=5,column=2)
btnclosebracket = Button(f2,padx=23,pady=2,bd=8,fg='black',font=('arial',20,'bold'),text=')',bg='orange').grid(row=5,column=3)



# --------------------------------------------Choose Meal-----------------------------------
Meal = IntVar()
Mealdicator = StringVar(value='Delicious Meals')

lblMeal = Label(f1,font=('arial',16,'bold'),text='Choose Meal',bd=10, anchor=W)
lblMeal.grid(row=0,column=0)
txtMeal = ttk.Combobox(f1,font=('arial',16,'bold'),textvariable=Mealdicator)
txtMeal['value'] = ('Fried Rice','Fried Rice & Chicken','Beef','Sharwama','Cheese Balls','Burger')
txtMeal.grid(row=0,column=1)

lblQtofMeal = Label(f1,font=('arial',16,'bold'),text='Qty of Meal',bd=10,anchor=W)
lblQtofMeal.grid(row=1,column=0)
txtQtofMeal = Entry(f1,font=('arial',16,'bold'),textvariable=Meal,bd=10,insertwidth=4,bg='white',justify='right')
txtQtofMeal.grid(row=1,column=1)


# ---------------------------------------------Choose Drinks-----------------------------------

Drink = IntVar()
Drinkdicator = StringVar(value='Fresh drinks')

lblDrink = Label(f1,font=('arial',16,'bold'),text='Choose Drinks',bd=10, anchor=W)
lblDrink.grid(row=2,column=0)
txtDrink = ttk.Combobox(f1,font=('arial',16,'bold'),textvariable=Drinkdicator)
txtDrink['value'] = ('Bottled Water','Coca-Coala','Pepse','Maaza','Wine','Alcohol')
txtDrink.grid(row=2,column=1)

lblQtofDrink = Label(f1,font=('arial',16,'bold'),text='Qty of Drinks',bd=10,anchor=W)
lblQtofDrink.grid(row=3,column=0)
txtQtofDrink = Entry(f1,font=('arial',16,'bold'),textvariable=Drink,bd=10,insertwidth=4,bg='white',justify='right')
txtQtofDrink.grid(row=3,column=1)

# --------------------------------------------Order Delivery-----------------------------------

chkb1 = IntVar()
lblHomeDev = Label(f1,font=('arial',16,'bold'),text='Order Delivery',bd=10,anchor = W)
lblHomeDev.grid(row=4,column=0)
check1 = Checkbutton(f1,text='Yes',variable=chkb1,font=('aral',16,'bold'))
check1.grid(row=4,column=1)


# -----------------------------------------Book a room-------------------------------------

v = IntVar()
v.set(3)
lblRoom = Label(f1,font=('arial',16,'bold'),text='Book a Room',bd=10,anchor=W)
lblRoom.grid(row=5,column=0)

Myradios = Radiobutton(f1,text='VIP',font=('arial',16,'bold'),variable=v,value=1)
Myradios.grid(row=5,column=1,sticky=W)

Myradios = Radiobutton(f1,text='Normal',font=('arial',16,'bold'),variable=v,value=1)
Myradios.grid(row=5,column=1)
Myradios = Radiobutton(f1,text='No',font=('arial',16,'bold'),variable=v,value=1)
Myradios.grid(row=5,column=1,sticky=E)



root.mainloop()