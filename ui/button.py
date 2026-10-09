import sys
from tkinter import ttk
from ejemplos import ejemplo as e


class EjemploButton:
    ejemplo: e.Ejemplo

    def __init__(self, parent, index: int):
        self.button = ttk.Button(
            parent,
            text=f"Ejemplo {index + 1}",
            command=self.click,
            style="Example.TButton",
        )

        self.button.pack(fill="x", padx=30, pady=6, ipady=8)

    def asignar_ejemplo(self, ejemplo: e.Ejemplo):
        self.ejemplo = ejemplo

    def click(self):
        if self.ejemplo is None:
            raise Exception("El ejemplo no ha sido asignado")

        self.ejemplo.ejecutar()

    def cerrar():
        sys.exit(0)
