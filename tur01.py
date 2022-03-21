import turtle as t

t.setup(960,560)   #실행 윈도우창 크기 설정

t.shape('turtle')
t.speed(0)       #거북이 속도 
t.pensize(20)    

#기본으로 검정색으로 그림
t.circle(100)    #반지름이 100인 원 그리기

t.up()            #펜 올라가서 선 안 그려짐
t.forward(240)     #우측으로 240픽셀이동
t.down()          #펜 내려와서 선 그림
t.pencolor('red')   #펜 색상을 레드로 함
t.circle(100)

t.up()
t.backward(480)     #좌측으로 480픽셀 이동
t.down()
t.pencolor('#1E90FF')    #색상표 번호로 색상 지정
t.circle(100)

t.up()
t.sety(-120)       #거북이 밑으로 120픽셀 이동
t.down()

t.up()
t.forward(120)
t.down()
t.pencolor('#FFD700')   
t.circle(100)

t.up()
t.forward(240)
t.down()
t.pencolor('green')
t.circle(100)

t.hideturtle()      #거북이 숨김


t.done()
