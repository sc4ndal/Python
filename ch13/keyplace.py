from tkinter import *
from math import *

def calculate(event):
    label.configure(text="결과 :" +str(eval(entry.get())))
    entry.delete(0, END)

win = Tk()

Label(win, text="파이썬 수식 입력 : ").pack()
entry = Entry(win)
entry.bind("<Return>", calculate)
entry.pack()

label = Label(win, text="결과 : ")
label.pack()

win.mainloop()