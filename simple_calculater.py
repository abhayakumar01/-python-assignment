from tkinter import *
window=Tk()
window.geometry('500x300')
entry=Entry(window,width=50,bd=5)
entry.place(x=0,y=0)

def click(num):
    result=entry.get()
    entry.insert(0,str(result)+ str(num))

b=Button(window,text="1",width=10,bd=5,command=lambda:click(1))
b.place(x=10,y=20)
b=Button(window,text="2",width=10,bd=5,command=lambda:click(2))
b.place(x=10,y=40)
b=Button(window,text="3",width=10,bd=5,command=lambda:click(3))
b.place(x=10,y=60)
b=Button(window,text="4",width=10,bd=5,command=lambda:click(4))
b.place(x=80,y=20)
b=Button(window,text="5",width=10,bd=5,command=lambda:click(5))
b.place(x=80,y=40)
b=Button(window,text="6",width=10,bd=5,command=lambda:click(6))
b.place(x=80,y=60)
b=Button(window,text="7",width=10,bd=5,command=lambda:click(7))
b.place(x=150,y=20)
b=Button(window,text="8",width=10,bd=5,command=lambda:click(8))
b.place(x=150,y=40)
b=Button(window,text="9",width=10,bd=5,command=lambda:click(9))
b.place(x=150,y=60)
b=Button(window,text="0",width=10,bd=5,command=lambda:click(0))
b.place(x=10,y=80)


def sub():
    n1=entry.get()
    global math
    math = "subtract"
    global i
    i=int(n1)
    entry.delete(0,END)
b = Button(window, text="-", width=10, bd=5, command=sub)
b.place(x=150, y=80)
b.place(x=80, y=80)

def add( ):
    n1 = entry.get()
    global math
    math = "addition"
    global i
    i = int(n1)
    entry.delete(0, END)
b=Button(window,text="+",width=10,bd=5,command=add)
b.place(x=150,y=80)


def mult():
    n1=entry.get()
    global math
    math = "multiplication"
    global i
    i=int(n1)
    entry.delete(0,END)
b=Button(window,text="X",width=15,bd=5,command= mult)
b.place(x=10,y=100)

def equal():
    n2=entry.get()
    entry.delete(0, END)
    if math =="addition":
        entry.insert(0,i+int(n2))
    elif math =="subtract":
        entry.insert(0,i-int(n2))
    elif math =="multiplication":
       entry.insert(0,i* int(n2))
    elif math =="division":
       entry.insert(0,i / int(n2))


b=Button(window,text="equal",width=10,bd=5,command = equal)
b.place(x=80,y=100)

def div( ):
    n1=entry.get()
    global math
    math = "division"
    global i
    i=int(n1)
    entry.delete(0,END)
b = Button(window, text="%", width=10, bd=5, command=div)
b.place(x=150, y=100)

def clear( ):
    entry.delete(0,END)
b=Button(window,text="clear",width=10,bd=5,command=clear)
b.place(x=80,y=130)
mainloop()