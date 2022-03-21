import turtle as t
import random



def screenLeftClick(x, y):
    tSize = random.randrange(2,10)  #크기를 2에서 10까지 랜덤으로 변환
    t.shapesize(tSize)     #모양 크기를 위의 랜덤으로 지정
    r = random.random()
    g = random.random()
    b = random.random()
    t.color((r, g, b))
    t.Angle = random.randrange(0, 360)   #각도를 0도에서 360도까지 랜덤으로 돌림


    t.shape('turtle')   #거북이 모양
    t.penup()       #펜을 올림으로서 이동할때 줄이 그어지지 않는다
    t.goto(x,y)   #좌표로 이동
    t.left(t.Angle)   #왼쪽으로 돌아감
    t.stamp()           #스탬프 찍기


t.onscreenclick(screenLeftClick, 1)       #스크린을 마우스 좌클릭 했을때 screenLeftClick 함수 실행
t.done()