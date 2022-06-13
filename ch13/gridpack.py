from tkinter import *

win = Tk()
win.geometry('200x200')

btn1 = Button(win, text='one')
btn2 = Button(win, text='two')
btn3 = Button(win, text='three')
btn4 = Button(win, text='four')

btn1.grid(row=0, rowspan=2, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=1, column=1)
btn4.grid(row=2, column=0, columnspan=2)

win.mainloop()