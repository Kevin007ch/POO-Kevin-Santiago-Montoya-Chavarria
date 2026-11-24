import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from enum import Enum

# --- CLASES DE DOMINIO (MODELO POO) ---

class TipoCargo(Enum):
    DIRECTIVO = "Directivo"
    ESTRATEGICO = "Estratégico"
    OPERATIVO = "Operativo"

class TipoGenero(Enum):
    MASCULINO = "Masculino"
    FEMENINO = "Femenino"

class Empleado:
    def __init__(self, nombre: str, apellidos: str, cargo: TipoCargo, genero: TipoGenero,
                 salario_dia: float, dias_trabajados: int, otros_ingresos: float,
                 pagos_salud: float, aporte_pensiones: float):
        self.nombre = nombre
        self.apellidos = apellidos
        self.cargo = cargo
        self.genero = genero
        self.salario_dia = salario_dia
        self.dias_trabajados = dias_trabajados
        self.otros_ingresos = otros_ingresos
        self.pagos_salud = pagos_salud
        self.aporte_pensiones = aporte_pensiones

    def calcular_nomina(self) -> float:
        return (self.salario_dia * self.dias_trabajados) + self.otros_ingresos - self.pagos_salud - self.aporte_pensiones

class ListaEmpleados:
    def __init__(self):
        self.lista: list[Empleado] = []

    def agregar_empleado(self, empleado: Empleado):
        self.lista.append(empleado)

    def calcular_total_nomina(self) -> float:
        return sum(emp.calcular_nomina() for emp in self.lista)

    def convertir_texto(self) -> str:
        texto = "=== REPORTE DE NÓMINA DE EMPLEADOS ===\n\n"
        for emp in self.lista:
            texto += (
                f"Nombre: {emp.nombre} {emp.apellidos}\n"
                f"Cargo: {emp.cargo.value} | Género: {emp.genero.value}\n"
                f"Salario por día: ${emp.salario_dia:,.2f} | Días trabajados: {emp.dias_trabajados}\n"
                f"Otros ingresos: ${emp.otros_ingresos:,.2f} | Salud: ${emp.pagos_salud:,.2f} \vert{} Pensión: ${emp.aporte_pensiones:,.2f}\n"
                f"Sueldo Neto Mensual: ${emp.calcular_nomina():,.2f}\n"
                + "-" * 50 + "\n"
            )
        texto += f"\nTOTAL NÓMINA EMPRESA: ${self.calcular_total_nomina():,.2f}\n"
        return texto

# --- VENTANAS Y CUADROS DE DIÁLOGO (GUI TKINTER) ---

class DialogoAgregarEmpleado(tk.Toplevel):
    def __init__(self, parent, lista_empleados: ListaEmpleados):
        super().__init__(parent)
        self.title("Agregar Empleado")
        self.geometry("400x460")
        self.resizable(False, False)
        self.lista_empleados = lista_empleados
        self.grab_set()

        # Campos de texto
        tk.Label(self, text="Nombre:").grid(row=0, column=0, padx=10, pady=8, sticky="w")
        self.entry_nombre = tk.Entry(self, width=25)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=8)

        tk.Label(self, text="Apellidos:").grid(row=1, column=0, padx=10, pady=8, sticky="w")
        self.entry_apellidos = tk.Entry(self, width=25)
        self.entry_apellidos.grid(row=1, column=1, padx=10, pady=8)

        tk.Label(self, text="Cargo:").grid(row=2, column=0, padx=10, pady=8, sticky="w")
        self.combo_cargo = ttk.Combobox(self, values=[c.value for c in TipoCargo], state="readonly", width=22)
        self.combo_cargo.current(0)
        self.combo_cargo.grid(row=2, column=1, padx=10, pady=8)

        tk.Label(self, text="Género:").grid(row=3, column=0, padx=10, pady=8, sticky="w")
        self.var_genero = tk.StringVar(value=TipoGenero.MASCULINO.value)
        frame_gen = tk.Frame(self)
        frame_gen.grid(row=3, column=1, padx=10, pady=8, sticky="w")
        tk.Radiobutton(frame_gen, text="Masculino", variable=self.var_genero, value=TipoGenero.MASCULINO.value).pack(side="left")
        tk.Radiobutton(frame_gen, text="Femenino", variable=self.var_genero, value=TipoGenero.FEMENINO.value).pack(side="left")

        tk.Label(self, text="Salario por día ($):").grid(row=4, column=0, padx=10, pady=8, sticky="w")
        self.entry_salario = tk.Entry(self, width=25)
        self.entry_salario.grid(row=4, column=1, padx=10, pady=8)

        tk.Label(self, text="Días trabajados (1-31):").grid(row=5, column=0, padx=10, pady=8, sticky="w")
        self.spin_dias = tk.Spinbox(self, from_=1, to=31, width=23)
        self.spin_dias.delete(0, tk.END)
        self.spin_dias.insert(0, "30")
        self.spin_dias.grid(row=5, column=1, padx=10, pady=8)

        tk.Label(self, text="Otros ingresos ($):").grid(row=6, column=0, padx=10, pady=8, sticky="w")
        self.entry_otros = tk.Entry(self, width=25)
        self.entry_otros.insert(0, "0")
        self.entry_otros.grid(row=6, column=1, padx=10, pady=8)

        tk.Label(self, text="Pagos por salud ($):").grid(row=7, column=0, padx=10, pady=8, sticky="w")
        self.entry_salud = tk.Entry(self, width=25)
        self.entry_salud.insert(0, "0")
        self.entry_salud.grid(row=7, column=1, padx=10, pady=8)

        tk.Label(self, text="Aporte pensiones ($):").grid(row=8, column=0, padx=10, pady=8, sticky="w")
        self.entry_pension = tk.Entry(self, width=25)
        self.entry_pension.insert(0, "0")
        self.entry_pension.grid(row=8, column=1, padx=10, pady=8)

        # Botones
        frame_btns = tk.Frame(self)
        frame_btns.grid(row=9, column=0, columnspan=2, pady=15)
        tk.Button
