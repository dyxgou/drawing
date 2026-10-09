from turtle import Turtle, Screen
from . import ejemplo as e


class Pintor:
    t: Turtle
    pantalla: Screen

    def __init__(self, turtle: Turtle):
        self.t = turtle

    def crear_pantalla(self, titulo: str):
        self.pantalla = Screen()
        self.pantalla.title(titulo)
        self.pantalla.setup(width=1200, height=1000)
        self.pantalla.screensize(canvwidth=1200, canvheight=1000)

    def asignar_fondo(self, color: e.Color):
        if self.pantalla is None:
            raise Exception("La pantalla no ha sido creada.")

        self.pantalla.colormode(255)
        self.pantalla.bgcolor(color)
