import tkinter as tk
from tkinter import messagebox

class FormularioCliente:
    @staticmethod
    def validar(identificacion: str, nombre: str, edad_str: str):
        if not identificacion.strip():
            raise ValueError("El campo 'ID' no puede estar vacío.")
        if not nombre.strip():
            raise ValueError("El campo 'Nombre' no puede estar vacío.")
        try:
            edad = int(edad_str)
        except ValueError:
            raise ValueError("La 'Edad' debe ser un número entero válido.")
        
        if edad < 0 or edad > 120:
            raise ValueError("La 'Edad' debe estar en un rango válido (0 a 120 años).")

class VentanaEjercicio6_7(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Ejercicio 6.7: Validación de Campos")
        self.geometry("380x250")

        tk.Label(self, text="ID / Cédula:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_id = tk.Entry(self)
        self.entry_id.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self, text="Nombre Completo:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self, text="Edad:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entry_edad = tk.Entry(self)
        self.entry_edad.grid(row=2, column=1, padx=10, pady=10)

        btn_validar = tk.Button(self, text="Validar Registro", command=self.procesar_validacion, bg="#e8f5e9")
        btn_validar.grid(row=3, column=0, columnspan=2, pady=15)

    def procesar_validacion(self):
        try:
            FormularioCliente.validar(
                self.entry_id.get(),
                self.entry_nombre.get(),
                self.entry_edad.get()
            )
            messagebox.showinfo("Éxito", "Todos los campos del formulario fueron validados correctamente.")
        except ValueError as ex:
            messagebox.showerror("Error de Validación", str(ex))
