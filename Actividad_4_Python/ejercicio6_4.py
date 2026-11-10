import tkinter as tk
from tkinter import messagebox

class CuentaBancaria:
    def __init__(self, saldo_inicial: float = 100000.0):
        self.saldo = saldo_inicial
        self.numero_consignaciones = 0
        self.numero_retiros = 0

    def consignar(self, cantidad: float):
        if cantidad <= 0:
            raise ValueError("El valor a consignar debe ser mayor que cero.")
        self.saldo += cantidad
        self.numero_consignaciones += 1

    def retirar(self, cantidad: float):
        if cantidad <= 0:
            raise ValueError("El valor a retirar debe ser mayor que cero.")
        if cantidad > self.saldo:
            raise Exception("La cantidad a retirar excede el saldo actual disponible.")
        self.saldo -= cantidad
        self.numero_retiros += 1

class VentanaEjercicio6_4(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Ejercicio 6.4: Excepciones (Cuenta Bancaria)")
        self.geometry("450x300")
        self.cuenta = CuentaBancaria(100000.0)

        tk.Label(self, text="Saldo Actual:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.lbl_saldo = tk.Label(self, text=f"${self.cuenta.saldo:.2f}", font=("Arial", 10, "bold"))
        self.lbl_saldo.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self, text="N° Consignaciones:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.lbl_cons = tk.Label(self, text="0")
        self.lbl_cons.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self, text="N° Retiros:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.lbl_ret = tk.Label(self, text="0")
        self.lbl_ret.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self, text="Monto Operación:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.entry_monto = tk.Entry(self)
        self.entry_monto.grid(row=3, column=1, padx=10, pady=10)

        btn_cons = tk.Button(self, text="Consignar", command=self.ejecutar_consignacion, bg="#e1f5fe")
        btn_cons.grid(row=4, column=0, padx=10, pady=10)

        btn_ret = tk.Button(self, text="Retirar", command=self.ejecutar_retiro, bg="#ffebee")
        btn_ret.grid(row=4, column=1, padx=10, pady=10)

    def actualizar_interfaz(self):
        self.lbl_saldo.config(text=f"${self.cuenta.saldo:.2f}")
        self.lbl_cons.config(text=str(self.cuenta.numero_consignaciones))
        self.lbl_ret.config(text=str(self.cuenta.numero_retiros))
        self.entry_monto.delete(0, tk.END)

    def ejecutar_consignacion(self):
        try:
            monto = float(self.entry_monto.get())
            self.cuenta.consignar(monto)
            self.actualizar_interfaz()
            messagebox.showinfo("Éxito", "Consignación realizada correctamente.")
        except ValueError as ex:
            if "could not convert" in str(ex):
                messagebox.showerror("Error de Formato", "Debe ingresar un valor numérico válido.")
            else:
                messagebox.showwarning("Excepción Capturada", str(ex))

    def ejecutar_retiro(self):
        try:
            monto = float(self.entry_monto.get())
            self.cuenta.retirar(monto)
            self.actualizar_interfaz()
            messagebox.showinfo("Éxito", "Retiro realizado correctamente.")
        except ValueError as ex:
            if "could not convert" in str(ex):
                messagebox.showerror("Error de Formato", "Debe ingresar un valor numérico válido.")
            else:
                messagebox.showwarning("Excepción Capturada", str(ex))
        except Exception as ex:
            messagebox.showwarning("Excepción Capturada", str(ex))
