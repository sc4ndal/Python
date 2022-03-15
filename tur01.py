import turtle as t

t.setup(960,560)

t.shape('turtle')
t.speed(0)
t.pensize(20)

#기본으로 검정색으로 그림
t.circle(100)

t.up()
t.forward(240)
t.down()
t.pencolor('red')
t.circle(100)

t.up()
t.backward(480)
t.down()
t.pencolor('#1E90FF')
t.circle(100)

t.up()
t.sety(-120)
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

t.hideturtle()


t.done()
