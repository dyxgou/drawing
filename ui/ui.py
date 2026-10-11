import sys
from turtle import Turtle
from typing import List
import tkinter as tk
from tkinter import ttk
from .button import EjemploButton

FONT = "MesloLGL Nerd Font Mono"


class App(tk.Tk):
    buttons: List[ttk.Button]

    def __init__(self):
        super().__init__()

        self.buttons = []
        self.title("Dibujante")
        self.geometry("420x700")
        self.resizable(False, False)

        self.configure(bg="#1e1e2e")

        self.setup_styles()
        self.create_ui()

    def setup_styles(self):
        style = ttk.Style(self)
        style.theme_use("clam")

        style.configure(
            "Example.TButton",
            font=(FONT, 12, "bold"),
            padding=(15, 12),
            background="#313244",
            foreground="#cdd6f4",
            borderwidth=0,
            corner_radious=12,
            relief="flat",
        )

        style.map(
            "Example.TButton",
            background=[
                ("active", "#585b70"),
                ("pressed", "#45475a"),
            ],
            foreground=[
                ("active", "#ffffff"),
            ],
        )

        style.configure(
            "Exit.TButton",
            font=(FONT, 11),
            padding=(15, 10),
            background="#45475a",
            foreground="#f38ba8",
            corner_radious=12,
            borderwidth=0,
        )

        style.map(
            "Exit.TButton",
            background=[
                ("active", "#585b70"),
                ("pressed", "#313244"),
            ],
        )

    def create_ui(self):
        container = tk.Frame(self, bg="#1e1e2e")
        container.pack(fill="both", expand=True, padx=25, pady=25)

        title = tk.Label(
            container,
            text="Ejemplos",
            font=(FONT, 24, "bold"),
            bg="#1e1e2e",
            fg="#cdd6f4",
        )
        title.pack(pady=(10, 5))

        subtitle = tk.Label(
            container,
            text="Selecciona un ejemplo para continuar",
            font=(FONT, 11),
            bg="#1e1e2e",
            fg="#a6adc8",
        )
        subtitle.pack(pady=(0, 25))

        buttons_frame = tk.Frame(container, bg="#1e1e2e")
        buttons_frame.pack(fill="x")

        for btn in self.crear_botones(buttons_frame):
            self.buttons.append(btn)

        ttk.Button(
            container, text="Salir", command=lambda: sys.exit(0), style="Exit.TButton"
        ).pack(fill="x", padx=30, pady=(25, 0), ipady=8)

    def crear_botones(self, contenedor: tk.Frame) -> List[EjemploButton]:
        from ejemplos import ejemplo1 as e1
        from ejemplos import ejemplo2 as e2
        from ejemplos import ejemplo3 as e3
        from ejemplos import ejemplo4 as e4
        from ejemplos import rayo as r

        common_turtle = Turtle()

        ejemplos = [
            e1.crear(common_turtle),
            e2.crear(common_turtle),
            e3.crear(common_turtle),
            e4.crear(common_turtle),
            r.crear(common_turtle),
        ]

        botones: List[EjemploButton] = []
        for index, ejem in enumerate(ejemplos):
            btn = EjemploButton(contenedor, index)
            btn.asignar_ejemplo(ejem)
            botones.append(ejem)

        return botones


if __name__ == "__main__":
    app = App()
    app.mainloop()
