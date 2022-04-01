import turtle as t
import random

t.setup(500,500,0,0)
# t.screensize(500,500)
t.shape('turtle')

t.speed(20)
t.penup()
t.goto(0,-250)
t.pendown()

for i in range(0,200) :
    t.pensize(10)
    ran = random.randrange(0,6)
    if ran == 0 :
        t.pencolor("red")
    elif ran == 1 :
        t.pencolor("#FFA500")
    elif ran == 2:
        t.pencolor("#FFFF00")
    elif ran == 3:
        t.pencolor("#008000")
    elif ran == 4:
        t.pencolor("#0000FF")
    elif ran == 5:
        t.pencolor("#000080")
    elif ran == 6:
        t.pencolor("#9400D3")

    t.circle(i,)

t.hideturtle()
t.done()
