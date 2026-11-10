import tkinter as tk
from tkinter import messagebox
import math

class CalculadoraEspecial:
    @staticmethod
    def calcular_logaritmo(val: float) -> float:
        if val <= 0:
            raise ArithmeticError("ArithmeticError: El logaritmo natural solo aplica para números mayores a cero.")
        return math.log(val)

    @staticmethod
    def calcular_raiz(val: float) -> float:
        if val < 0:
            raise ArithmeticError("ArithmeticError: No existe raíz cuadrada real para números negativos.")
        return math.sqrt(val)

class VentanaEjercicio6_6(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Ejercicio 6.6: Catchs Múltiples")
        self.geometry("450x220")

        tk.Label(self, text="Ingrese un número:").grid(row=0, column=0, padx=10, pady=15)
        self.entry_num = tk.Entry(self)
        self.entry_num.grid(row=0, column=1, padx=10, pady=15)

        btn_log = tk.Button(self, text="Logaritmo Natural", command=self.calc_log)
        btn_log.grid(row=1, column=0, padx=10, pady=10)

        btn_raiz = tk.Button(self, text="Raíz Cuadrada", command=self.calc_raiz)
        btn_raiz.grid(row=1, column=1, padx=10, pady=10)

        self.lbl_resultado = tk.Label(self, text="Resultado: -", font=("Arial", 10, "bold"))
        self.lbl_resultado.grid(row=2, column=0, columnspan=2, pady=15)

    def calc_log(self):
        self._ejecutar_operacion(CalculadoraEspecial.calcular_logaritmo)

    def calc_raiz(self):
        self._ejecutar_operacion(CalculadoraEspecial.calcular_raiz)

    def _ejecutar_operacion(self, funcion):
        try:
            val = float(self.entry_num.get())
            res = funcion(val)
            self.lbl_resultado.config(text=f"Resultado: {res:.4f}")
        except ValueError:
            messagebox.showerror("ValueError Capturado", "Error de entrada: Debe ingresar un valor numérico válido.")
        except ArithmeticError as ex:
            messagebox.showwarning("ArithmeticError Capturado", str(ex))
