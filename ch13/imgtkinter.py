from tkinter import *
from tkinter import messagebox

def myFunc():
    button2.configure(text='와우')
    messagebox.showinfo('고양이 버튼', '고양이가 매우 엄청 정말로 귀엽습니다')






window = Tk()
window.title('윈도우 창 연습')

photo = PhotoImage(file="moon1.png")
button1 = Button(window, image=photo, command=myFunc, width=100, height=20)

photo2 = PhotoImage(file="cat2.png")
label = Label(window, image=photo2)

button2 = Button(window, text="종료", command=window.destroy, width=10, height=2)

button1.pack(side=LEFT)
label.pack()
button2.pack()

window.mainloop()