from tkinter import *

win = Tk()
win.title('pack test')
win.geometry('450x200')
data = IntVar()
data.set(20)

h_label = Label(win, text='Height: ', font=('맑은고딕',15), fg='blue')
h_entry = Entry(win, font=('맑은고딕',15),width=10)

w_label = Label(win, text='Height: ', font=('맑은고딕',15), fg='blue')
h_entry = Entry(win, font=('맑은고딕',15),width=10, bd=3, textvariable=data)

'''추가필요'''

win.mainloop()