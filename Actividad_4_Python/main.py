import tkinter as tk
from ejercicio6_4 import VentanaEjercicio6_4
from ejercicio6_5 import VentanaEjercicio6_5
from ejercicio6_6 import VentanaEjercicio6_6
from ejercicio6_7 import VentanaEjercicio6_7
from ejercicio6_8 import VentanaEjercicio6_8

class AplicacionPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Actividad 4 POO - Universidad Nacional de Colombia")
        self.geometry("450x380")
        self.resizable(False, False)

        lbl_titulo = tk.Label(
            self, 
            text="Actividad 4: Excepciones y Archivos (GUI - Python)", 
            font=("Arial", 12, "bold"),
            pady=15
        )
        lbl_titulo.pack()

        btn_64 = tk.Button(self, text="1. Ejercicio 6.4 (Cuenta Bancaria)", command=lambda: VentanaEjercicio6_4(self), width=40, pady=5)
        btn_64.pack(pady=5)

        btn_65 = tk.Button(self, text="2. Ejercicio 6.5 (Lanzamiento raise)", command=lambda: VentanaEjercicio6_5(self), width=40, pady=5)
        btn_65.pack(pady=5)

        btn_66 = tk.Button(self, text="3. Ejercicio 6.6 (Catchs Múltiples)", command=lambda: VentanaEjercicio6_6(self), width=40, pady=5)
        btn_66.pack(pady=5)

        btn_67 = tk.Button(self, text="4. Ejercicio 6.7 (Validación de Campos)", command=lambda: VentanaEjercicio6_7(self), width=40, pady=5)
        btn_67.pack(pady=5)

        btn_68 = tk.Button(self, text="5. Ejercicio 6.8 (Lectura de Archivos)", command=lambda: VentanaEjercicio6_8(self), width=40, pady=5)
        btn_68.pack(pady=5)

if __name__ == "__main__":
    app = AplicacionPrincipal()
    app.mainloop()
