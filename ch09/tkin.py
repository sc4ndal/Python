import tkinter
import turtle as t
import tkinter.simpledialog as sim
# from turtle import shape, setup, screensize, write, done
from turtle import *
import random

title('거북이 글자쓰기')
swidth, sheight = 500,500
txtSize=30
shape('turtle')
penup()
setup(width=swidth+50,height=sheight+50)

screensize(swidth,sheight)
retStr=sim.askstring('문자열 입력','거북이 문자열')
for i in retStr:
    tX = random.randrange(-swidth/2,swidth/2)
    tY = random.randrange(-sheight/2,sheight/2)
    r=random.random();g=random.random();b=random.random()
    txtSize=random.randrange(10,80)
    pencolor((r,g,b))

    goto(tX, tY)
    write(i, font=('맑은고딕',txtSize,'bold'))


done()