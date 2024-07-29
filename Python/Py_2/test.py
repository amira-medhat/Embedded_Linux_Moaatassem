from tkinter import *


def fun():
    reversed_text = "".join(reversed(e1.get()))
    print(reversed_text)


wd = Tk()
wd.resizable(True, True)
Label(wd, text="Input: ").grid(row=0, column=1)
e1 = Entry(wd, width=20)
e1.grid(row=0, column=2)
Button(wd, text="Enter", fg="black", command=fun).grid(row=1, column=2)

wd.mainloop()
