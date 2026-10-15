from turtle import Turtle
from .ejemplo import Ejemplo


def _ejemplo1(t: Turtle):
    for _ in range(4):
        t.forward(100)
        t.left(90)


def crear(t: Turtle) -> Ejemplo:
    ejemplo = Ejemplo(t, "Ejemplo 1 de Blockly")
    ejemplo.asignar_funcion(_ejemplo1)

    return ejemplo
