import tkinter as tk
from tkinter import messagebox

class ValidadorRango:
    @staticmethod
    def verificar(valor: float, min_val: float, max_val: float):
        if valor < min_val or valor > max_val:
            raise ValueError(f"Excepción: El valor {valor} está fuera del rango permitido [{min_val} - {max_val}].")

class VentanaEjercicio6_5(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Ejercicio 6.5: Lanzamiento de Excepciones (raise)")
        self.geometry("400x230")

        tk.Label(self, text="Valor a evaluar:").grid(row=0, column=0, padx=10, pady=10)
        self.entry_val = tk.Entry(self)
        self.entry_val.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self, text="Límite Mínimo:").grid(row=1, column=0, padx=10, pady=5)
        self.entry_min = tk.Entry(self)
        self.entry_min.insert(0, "0")
        self.entry_min.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self, text="Límite Máximo:").grid(row=2, column=0, padx=10, pady=5)
        self.entry_max = tk.Entry(self)
        self.entry_max.insert(0, "100")
        self.entry_max.grid(row=2, column=1, padx=10, pady=5)

        btn_validar = tk.Button(self, text="Validar Rango", command=self.procesar)
        btn_validar.grid(row=3, column=0, columnspan=2, pady=15)

    def procesar(self):
        try:
            v = float(self.entry_val.get())
            mn = float(self.entry_min.get())
            mx = float(self.entry_max.get())
            ValidadorRango.verificar(v, mn, mx)
            messagebox.showinfo("Aprobado", "El valor ingresado está dentro del rango permitido.")
        except ValueError as ex:
            if "could not convert" in str(ex):
                messagebox.showerror("Error de Entrada", "Todos los campos deben ser números.")
            else:
                messagebox.showwarning("Excepción Lanzada", str(ex))
