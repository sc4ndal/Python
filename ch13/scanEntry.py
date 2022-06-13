from tkinter import *

def show():
    print("이름 : %s \n 나이 : %s" % (e1.get(), e2.get()))
    e1.delete(0, END)
    e1.insert(END, "ㅎㅇ")

win = Tk()
win.geometry('300x100')
Label(win, text='이름').place(x=20, y=20)
Label(win, text='나이').place(x=20, y=50)

e1 = Entry(win)
e2 = Entry(win)

e1.place(x=60,y=20)
e2.place(x=60,y=50)

Button(win, text="보이기", command=show).place(x=70,y=80)
Button(win, text="종료", command=quit).place(x=170,y=80)


win.mainloop()
