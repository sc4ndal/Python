import turtle as t
import random

t.shape('turtle')

pSize, tSize = 10, 0
r = 0.0
g = 0.0
b = 0.0

def screenLeftClick(x,y):
    global r, g, b
    t.pencolor((r, g, b))
    t.pendown()
    t.goto(x, y)

def screenRightClick(x,y):
    t.penup()
    t.goto(x, y)

def screenMidClick(x,y):
    global r, g, b
    tSize = random.randrange(1, 10)
    t.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()

t.onscreenclick(screenLeftClick,1)
t.onscreenclick(screenMidClick,2)
t.onscreenclick(screenRightClick,3)

t.done()
