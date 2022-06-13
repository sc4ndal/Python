import tkinter
from tkinter import *

window = Tk()
window.geometry("600x300+300+100")#윈도우 창 크기, 실행 위치
window.resizable(True,False)#width조절가능,height조절불가

l1 = Label(window, text="hello world")
l1.pack(side=LEFT)#창에서 왼쪽에 위치

l2 = Label(window, text="go home")
l2.pack(side=RIGHT)#창에서 오른쪽에 위치

img = PhotoImage(file="moon1.png")
l3 = Label(window, image=img,width=100,height=100)
l3.pack()

def myFun():
    print('hi')

# def add(a,b):
#     c=a+b
#     print(c)

b1 = Button(window, text='버튼',command=myFun(),width=20,height=10)
b1.pack()

# b2 = Button(window,exit())
# b2.pack()

window.mainloop()