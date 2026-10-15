from turtle import Turtle
from .ejemplo import Ejemplo


def _estrella(t: Turtle):
    for _ in range(5):
        t.forward(50)
        t.right(144)


def _ejemplo2(t: Turtle):
    for _ in range(3):
        _estrella(t)
        t.penup()
        t.forward(150)
        t.left(120)
        t.pendown()


def crear(t: Turtle) -> Ejemplo:
    ejemplo = Ejemplo(t, "Ejemplo 1 de Blockly")
    ejemplo.asignar_funcion(_ejemplo2)

    return ejemplo
