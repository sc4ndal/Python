import turtle as t

t.shape('turtle')
t.pensize(4)

#t.color("blue") #line
t.bgcolor("lightgreen") #bg
#t.fillcolor("lightblue") #채우기
t.speed(5) #speed
t.pencolor('skyblue')


#r = int(input("몇개의 원을 그릴까요?"))
r=5
for i in range(r):
    t.circle(100)
    t.left(360/r)
    t.forward(20)
'''
t.begin_fill()
t.circle(100)
t.end_fill()
'''
#그래픽 창이 열린 상태로 유지
t.done()