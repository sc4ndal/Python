from tkinter import *
win = Tk()

Label(win, text='박스 #1', bg='red', fg='white').place(x=0,y=0)
Label(win, text='박스 #2', bg='green', fg='white').place(x=20,y=20)
Label(win, text='박스 #3', bg='blue', fg='white').place(x=40,y=40)

win.mainloop()