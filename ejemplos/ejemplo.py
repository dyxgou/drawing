import sys
from .pintor import Pintor
from turtle import Turtle
from collections.abc import Callable

type EjemploFunc = Callable[Turtle]
type Color = tuple[int, int, int]
BLANCO: Color = (255, 255, 255)


class Ejemplo(Pintor):
    titulo: str
    fondo: Color
    func: EjemploFunc

    def __init__(self, turtle: Turtle, titulo: str, fondo: Color = BLANCO):
        super().__init__(turtle)
        self.t.pensize(2)
        self.t.speed(9)
        self.titulo = titulo
        self.fondo = fondo
        self.crear_pantalla(self.titulo)
        self.asignar_fondo(fondo)

    def asignarFuncion(self, func: EjemploFunc):
        self.func = func

    def ejecutar(self):
        self.reset()

        if self.func is None:
            raise Exception("La función del ejemplo no ha sido asignada.")

        self.func(self.t)

    def cerrar():
        sys.exit(0)

    def reset(self):
        self.t.home()
        self.t.clear()
        self.t.pendown()
        self.t.color("black")
