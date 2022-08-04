import turtle as t

t.setup(500, 500)

t.shape("turtle")
t.color("green")

def poligono_regular(px, py, radio, lados):
    t.penup()
    t.goto(px, py - radio)
    t.pendown()
    t.circle(radio)

    angulo = 360 / lados
    print (angulo)

    for i in range(lados):
        t.penup()
        t.goto(px, py)
        t.pendown()

        t.seth(angulo*i+1)
        t.forward(radio)
        print(t.pos())

poligono_regular(0, 0, 100, 22)

t.done()
t.bye()