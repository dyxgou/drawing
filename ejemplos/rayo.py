from turtle import Turtle
from .ejemplo import Ejemplo


def _ejemplo1(t: Turtle):
    t.penup()
    for i in range(2):
        t.left(90)
        t.forward(170)

    t.color((0, 0, 0), (227, 23, 26))

    t.begin_fill()
    t.pendown()
    t.left(180)
    t.forward(50)
    t.right(90)
    t.forward(25)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(25)
    t.right(90)
    t.forward(100)

    for i in range(3):
        t.right(90)
        t.forward(25)
        t.left(90)
        t.forward(25)
    t.forward(50)
    t.right(90)
    t.forward(25)
    t.left(90)
    t.forward(25)
    t.right(90)
    t.forward(50)
    for i in range(2):
        t.right(90)
        t.forward(25)
        t.left(90)
        t.forward(25)
    t.right(90)
    t.forward(150)
    for i in range(2):
        t.right(90)
        t.forward(25)
        t.left(90)
        t.forward(50)

    t.forward(25)
    t.right(90)
    t.forward(50)
    t.left(90)
    t.forward(25)
    t.right(90)
    t.forward(100)
    t.end_fill()

    t.penup()
    t.right(180)
    t.forward(25)
    t.pendown()
    t.color((0, 0, 0), (237, 119, 40))
    t.begin_fill()
    for i in range(5):
        t.forward(25)
        t.left(90)
    t.end_fill()

    t.forward(25)

    t.begin_fill()
    for i in range(2):
        t.forward(50)
        t.right(90)
        t.forward(25)
        t.right(90)
    t.end_fill()

    t.color((0, 0, 0), (235, 217, 28))
    t.right(90)

    t.begin_fill()
    for i in range(4):
        t.forward(25)
        t.right(90)
    t.end_fill()
    t.forward(25)

    t.begin_fill()
    for i in range(2):
        t.forward(25)
        t.left(90)
        t.forward(25)
        t.right(90)

    t.left(180)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.end_fill()

    t.penup()
    t.left(180)
    t.forward(325)
    t.right(90)
    t.forward(25)
    t.pendown()

    t.begin_fill()
    for i in range(4):
        t.forward(25)
        t.right(90)
    t.end_fill()

    t.penup()
    t.right(90)
    t.forward(150)
    t.pendown()

    t.begin_fill()
    for i in range(4):
        t.forward(25)
        t.left(90)
    t.end_fill()

    t.penup()
    t.left(90)
    t.color((0, 0, 0), (255, 255, 255))
    t.forward(25)
    t.pendown()

    t.begin_fill()
    t.forward(25)
    t.left(90)
    t.forward(25)
    t.right(90)
    t.forward(25)
    t.left(90)
    t.forward(75)
    t.left(90)
    t.forward(25)
    t.right(90)
    t.forward(25)
    t.left(90)
    t.forward(25)
    t.left(90)
    t.forward(125)
    t.end_fill()

    t.penup()
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.pendown()

    t.begin_fill()
    t.forward(50)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(25)
    t.left(90)
    t.forward(25)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(125)
    t.end_fill()

    t.left(180)
    t.forward(100)
    t.color((0, 0, 0), (22, 100, 196))

    t.begin_fill()
    for i in range(4):
        t.left(90)
        t.forward(25)
    t.end_fill()

    t.left(180)
    t.forward(50)

    t.begin_fill()
    for i in range(4):
        t.forward(25)
        t.right(90)
    t.end_fill()

    t.penup()
    t.forward(150)
    t.left(90)
    t.forward(25)
    t.pendown()

    t.color((0, 0, 0))

    t.begin_fill()
    t.forward(75)
    t.left(90)
    t.forward(50)
    for i in range(2):
        t.left(90)
        t.forward(25)
    t.right(90)
    t.forward(50)
    t.left(90)
    t.forward(25)
    t.end_fill()

    t.penup()
    t.left(180)
    t.forward(125)
    t.pendown()

    t.begin_fill()
    for i in range(2):
        t.right(90)
        t.forward(25)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(75)
    t.right(90)
    t.forward(50)
    t.end_fill()

    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(25)

    t.begin_fill()
    for i in range(2):
        t.right(90)
        t.forward(25)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(75)
    t.right(90)
    t.forward(50)
    t.end_fill()

    t.right(180)
    t.forward(200)

    t.begin_fill()
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    for i in range(2):
        t.forward(25)
        t.left(90)
        t.forward(25)
        t.right(90)
    t.end_fill()


def crear(t: Turtle) -> Ejemplo:
    ejemplo = Ejemplo(t, "Ejemplo 1 de Blockly", (245, 208, 221))
    ejemplo.asignar_funcion(_ejemplo1)

    return ejemplo
