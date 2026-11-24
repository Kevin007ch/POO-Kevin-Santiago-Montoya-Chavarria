import tkinter as tk
from ejercicio8_4 import VentanaEjercicio8_4
from ejercicio8_5 import VentanaEjercicio8_5

class AplicacionActividad5(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Actividad 5 POO - Universidad Nacional de Colombia")
        self.geometry("470x260")
        self.resizable(False, False)

        lbl_titulo = tk.Label(
            self,
            text="Actividad 5: Cuadros de Diálogo y Gestión de Contenido\n(Capítulo 8 - Python Tkinter)",
            font=("Arial", 11, "bold"),
            pady=20
        )
        lbl_titulo.pack()

        btn_84 = tk.Button(
            self,
            text="1. Ejercicio 8.4: Cuadros de Diálogo (Nómina)",
            command=lambda: VentanaEjercicio8_4(self),
            width=44,
            pady=8,
            bg="#e3f2fd"
        )
        btn_84.pack(pady=8)

        btn_85 = tk.Button(
            self,
            text="2. Ejercicio 8.5: Gestión de Contenido (Hotel)",
            command=lambda: VentanaEjercicio8_5(self),
            width=44,
            pady=8,
            bg="#e8f5e9"
        )
        btn_85.pack(pady=8)

if __name__ == "__main__":
    app = AplicacionActividad5()
    app.mainloop()
