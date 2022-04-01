import random
import turtle as t
from random import randint

t.setup(400,400,0,0)
t.screensize(100,100)

t.shape('turtle')
t.speed(5)
exitCount = 0
swidth, sheight = 300, 300
curX, cruY = [0] * 2


for _ in range(0,100):


    r=random.random()
    g=random.random()
    b=random.random()
    t.color((r,g,b))
    tSize=random.randrange(1,10)
    t.pensize(tSize)
    t.Angle = random.randrange(0, 360)
    t.right(t.Angle)
    x=random.randrange(-200,200)
    y=random.randrange(-200,200)
    t.goto(x,y)

    curX = t.xcor()
    curY = t.ycor()
    if(-swidth/2<=curX and curX <=swidth/2)and(-sheight/2<=curY and curY<=sheight/2):
        pass
    else:
        t.penup()
        t.goto(0,0)
        t.pendown()

        exitCount += 1
        if exitCount >=10:
                break



t.hideturtle()
t.done()