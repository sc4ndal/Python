from tkinter import *
def show():
    print("이름 : %s \n나이 : %s" % (e1.get(), e2.get()))
    e1.delete(0,END)
    e2.delete(0,END)
    e1.focus_set()


win = Tk()
win.geometry("300x100")
lab1 = Label(win,text="이름")
lab2 = Label(win,text="나이")
lab1.grid(row=0,column=0)
lab2.grid(row=1,column=0)

e1 = Entry(win)
e2 = Entry(win)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

btn1 = Button(win, text="출력", command=show)
btn2 = Button(win, text="종료", command=quit)

btn1.grid(row=2,column=0)
btn2.grid(row=2,column=1)

win.mainloop()
