import turtle as t
import random

t.shape('turtle')
t.title('거북이 그림 그리기')

pSize, tSize = 10, 0
# r = 0.0
# g = 0.0
# b = 0.0
r, g, b = 0.0, 0.0, 0.0

def screenLeftClick(x,y):   #마우스 좌클릭 시 현재 팬 색상으로 내려와서 위치 이동
    global r, g, b       #global로 함수 밖의 r,g,b를 가져옴
    t.pencolor((r, g, b))
    t.pendown()
    t.goto(x, y)

def screenRightClick(x,y):  #마우스 우클릭 시 팬 들어가면서 위치만 이동
    t.penup()
    t.goto(x, y)

def screenMidClick(x,y):    #마우스 휠클릭 시 거북이 크기 랜덤으로 변하면서 팬 색 변함
    global r, g, b
    tSize = random.randrange(1, 10)    #tSize를 1에서 10까지 랜덤 크기
    t.shapesize(tSize)    #거북아 크기 tSize
    r = random.random()
    g = random.random()
    b = random.random()

t.onscreenclick(screenLeftClick,1)
t.onscreenclick(screenMidClick,2)
t.onscreenclick(screenRightClick,3)

t.done()
