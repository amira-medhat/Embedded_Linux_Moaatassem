from tkinter import *


def calculate():
    if v.get() == 1:
        sub()
    if v.get() == 2:
        add()


def sub():
    result.set(int(e1.get()) - int(e2.get()))


def add():
    result.set(int(e1.get()) + int(e2.get()))


wd = Tk()
Label(wd, text="First number: ").grid(row=0, column=0)
Label(wd, text="Second number: ").grid(row=1, column=0)


e1 = Entry(wd)
e2 = Entry(wd)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
v = IntVar()

Radiobutton(wd, variable=v, text="sub", value=1).grid(row=2, column=0)
Radiobutton(wd, variable=v, text="add", value=2).grid(row=3, column=0)

Button(wd, text="calculate", command=calculate).grid(row=2, column=1)

result = StringVar()
Label(wd, textvariable=result).grid(row=3, column=1)
result.set("The result will show here")
wd.mainloop()
