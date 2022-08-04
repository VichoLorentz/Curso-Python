import turtle as t

t.setup(500, 500)

t.shape("turtle")
t.color("green")

print("Origen", t.pos())
t.forward(250)
t.left(90)
t.forward(250)
print("Esquina superior derecha", t.pos())
t.left(90)
t.forward(500)
print("Esquina superior izquierda",t.pos())
t.left(90)
t.forward(500)
print("Esquina inferior izquierda",t.pos())
t.left(90)
t.forward(500)
print("Esquina inferior derecha",t.pos())

t.done()
t.bye()