from turtle import Turtle
from .ejemplo import Ejemplo


def _estrella(t: Turtle):
    for _ in range(5):
        t.forward(50)
        t.right(144)


def _ejemplo3(t: Turtle):
    for _ in range(3):
        _estrella(t)
        t.penup()
        t.forward(150)
        t.left(120)
        t.pendown()

    t.right(180)
    t.penup()
    t.forward(100)
    t.pendown()

    t.begin_fill()
    t.circle(50)
    t.end_fill()


def crear(t: Turtle) -> Ejemplo:
    ejemplo = Ejemplo(t, "Ejemplo 1 de Blockly")
    ejemplo.asignarFuncion(_ejemplo3)

    return ejemplo
