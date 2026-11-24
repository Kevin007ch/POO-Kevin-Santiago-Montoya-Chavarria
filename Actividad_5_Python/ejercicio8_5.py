import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# --- CLASES DE DOMINIO (MODELO POO) ---

class Huesped:
    def __init__(self, nombres: str, apellidos: str, documento_identidad: int):
        self.nombres = nombres
        self.apellidos = apellidos
        self.documento_identidad = documento_identidad
        self.fecha_ingreso: datetime | None = None
        self.fecha_salida: datetime | None = None

    def obtener_dias_alojamiento(self) -> int:
        if self.fecha_ingreso and self.fecha_salida:
            dias = (self.fecha_salida - self.fecha_ingreso).days
            return max(1, dias)  # Mínimo 1 día de cobro si entra y sale el mismo día
        return 0

class Habitacion:
    def __init__(self, numero_habitacion: int, disponible: bool, precio_dia: float):
        self.numero_habitacion = numero_habitacion
        self.disponible = disponible
        self.precio_dia = precio_dia
        self.huesped: Huesped | None = None

class Hotel:
    def __init__(self):
        self.lista_habitaciones: list[Habitacion] = []
        # Inicialización de las 10 habitaciones según especificación del libro
        for i in range(1, 11):
            precio = 120000.0 if i <= 5 else 160000.0
            self.lista_habitaciones.append(Habitacion(i, True, precio))

    def buscar_habitacion(self, numero: int) -> Habitacion | None:
        for hab in self.lista_habitaciones:
            if hab.numero_habitacion == numero:
                return hab
        return None

    def buscar_fecha_ingreso(self, numero: int) -> str:
        hab = self.buscar_habitacion(numero)
        if hab and hab.huesped and hab.huesped.fecha_ingreso:
            return hab.huesped.fecha_ingreso.strftime("%Y-%m-%d")
        return ""

# --- VENTANAS DE GESTIÓN DE CONTENIDO (GUI TKINTER) ---

class VentanaHabitaciones(tk.Toplevel):
    def __init__(self, parent, hotel: Hotel):
        super().__init__(parent)
        self.title("Habitaciones del Hotel")
        self.geometry("620x340")
        self.hotel = hotel
        self.grab_set()

        tk.Label(self, text="Estado Actual de las Habitaciones", font=("Arial", 11, "bold")).pack(pady=10)

        frame_grid = tk.Frame(self)
        frame_grid.pack(pady=10)

        for idx, hab in enumerate(self.hotel.lista_habitaciones):
            fila = (idx // 5) * 3
            col = idx % 5
            estado_txt = "Disponible" if hab.disponible else "No disponible"
            color_bg = "#e8f5e9" if hab.disponible else "#ffebee"
            color_fg = "#2e7d32" if hab.disponible else "#c62828"

            card = tk.Frame(frame_grid, bd=1, relief="solid", bg=color_bg, padx=8, pady=6)
            card.grid(row=fila, column=col, padx=6, pady=6)

            tk.Label(card, text=f"Habitación {hab.numero_habitacion}", font=("Arial", 9, "bold"), bg=color_bg).pack()
            tk.Label(card, text=f"${hab.precio_dia:,.0f}/día", font=("Arial", 8), bg=color_bg).pack()
            tk.Label(card, text=estado_txt, font=("Arial", 8, "bold"), fg=color_fg, bg=color_bg).pack()

        frame_ing = tk.Frame(self)
        frame_ing.pack(pady=15)
        tk.Label(frame_ing, text="Habitación a reservar (1-10):").pack(side="left", padx=5)
        self.spin_hab = tk.Spinbox(frame_ing, from_=1, to=10, width=5)
        self.spin_hab.pack(side="left", padx=5)
        tk.Button(frame_ing, text="Aceptar / Ingresar Huésped", command=self.seleccionar_habitacion, bg="#e3f2fd").pack(side="left", padx=10)

    def seleccionar_habitacion(self):
        try:
            num = int(self.spin_hab.get())
            hab = self.hotel.buscar_habitacion(num)
            if not hab:
                raise ValueError("Número de habitación inválido.")
            if not hab.disponible:
                messagebox.showerror("Ocupada", f"La habitación {num} ya se encuentra ocupada.", parent=self)
                return
            self.destroy()
            VentanaIngreso(self.master, self.hotel, num)
        except ValueError as e:
            messagebox.showerror("Error", str(e), parent=self)


class VentanaIngreso(tk.Toplevel):
    def __init__(self, parent, hotel: Hotel, numero_habitacion: int):
        super().__init__(parent)
        self.title("Ingreso de Huésped (Check-In)")
        self.geometry("380x280")
        self.hotel = hotel
        self.numero_habitacion = numero_habitacion
        self.grab_set()

        tk.Label(self, text=f"Habitación: {numero_habitacion}", font=("Arial", 11, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self, text="Fecha ingreso (AAAA-MM-DD):").grid(row=1, column=0, padx=10, pady=6, sticky="w")
        self.entry_fecha = tk.Entry(self, width=20)
        self.entry_fecha.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.entry_fecha.grid(row=1, column=1, padx=10, pady=6)

        tk.Label(self, text="Nombres:").grid(row=2, column=0, padx=10, pady=6, sticky="w")
        self.entry_nombres = tk.Entry(self, width=20)
        self.entry_nombres.grid(row=2, column=1, padx=10, pady=6)

        tk.Label(self, text="Apellidos:").grid(row=3, column=0, padx=10, pady=6, sticky="w")
        self.entry_apellidos = tk.Entry(self, width=20)
        self.entry_apellidos.grid(row=3, column=1, padx=10, pady=6)

        tk.Label(self, text="Doc. Identidad:").grid(row=4, column=0, padx=10, pady=6, sticky="w")
        self.entry_doc = tk.Entry(self, width=20)
        self.entry_doc.grid(row=4, column=1, padx=10, pady=6)

        frame_btns = tk.Frame(self)
        frame_btns.grid(row=5, column=0, columnspan=2, pady=15)
        tk.Button(frame_btns, text="Aceptar", command=self.registrar_ingreso, bg="#e8f5e9", width=12).pack(side="left", padx=8)
        tk.Button(frame_btns, text="Cancelar", command=self.destroy, width=12).pack(side="left", padx=8)

    def registrar_ingreso(self):
        try:
            fecha_str = self.entry_fecha.get().strip()
            fecha_ing = datetime.strptime(fecha_str, "%Y-%m-%d")
            nombres = self.entry_nombres.get().strip()
            apellidos = self.entry_apellidos.get().strip()
            doc = int(self.entry_doc.get().strip())

            if not nombres or not apellidos:
                raise ValueError("Nombres y apellidos son obligatorios.")

            hab = self.hotel.buscar_habitacion(self.numero_habitacion)
            huesped = Huesped(nombres, apellidos, doc)
            huesped.fecha_ingreso = fecha_ing
            hab.huesped = huesped
            hab.disponible = False

            messagebox.showinfo("Registro Exitoso", f"El huésped ha sido registrado en la habitación {self.numero_habitacion}.", parent=self)
            self.destroy()
        except ValueError as e:
            messagebox.showerror("Error de Datos", f"Verifique el formato de fecha (AAAA-MM-DD) y los campos numéricos.\nDetalle: {e}", parent=self)


class VentanaSalida(tk.Toplevel):
    def __init__(self, parent, hotel: Hotel, numero_habitacion: int):
        super().__init__(parent)
        self.title("Salida de Huéspedes (Check-Out)")
        self.geometry("410x320")
        self.hotel = hotel
        self.habitacion = self.hotel.buscar_habitacion(numero_habitacion)
        self.grab_set()

        huesped = self.habitacion.huesped
        fecha_ing_str = self.hotel.buscar_fecha_ingreso(numero_habitacion)

        tk.Label(self, text=f"Habitación: {numero_habitacion}", font=("Arial", 11, "bold")).grid(row=0, column=0, columnspan=2, pady=8)
        tk.Label(self, text=f"Huésped: {huesped.nombres} {huesped.apellidos}").grid(row=1, column=0, columnspan=2, pady=4)
        tk.Label(self, text=f"Fecha de ingreso: {fecha_ing_str}").grid(row=2, column=0, columnspan=2, pady=4)

        tk.Label(self, text="Fecha salida (AAAA-MM-DD):").grid(row=3, column=0, padx=10, pady=8, sticky="w")
        self.entry_salida = tk.Entry(self, width=18)
        self.entry_salida.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.entry_salida.grid(row=3, column=1, padx=10, pady=8)

        tk.Button(self, text="Calcular Total", command=self.calcular_total, bg="#e3f2fd").grid(row=4, column=0, columnspan=2, pady=6)

        self.lbl_dias = tk.Label(self, text="Cantidad de días: -")
        self.lbl_dias.grid(row=5, column=0, columnspan=2, pady=4)

        self.lbl_total = tk.Label(self, text="Total a pagar: $0", font=("Arial", 10, "bold"), fg="#1b5e20")
        self.lbl_total.grid(row=6, column=0, columnspan=2, pady=4)

        self.btn_registrar_salida = tk.Button(self, text="Registrar Salida", command=self.confirmar_salida, state="disabled", bg="#ffebee", width=20)
        self.btn_registrar_salida.grid(row=7, column=0, columnspan=2, pady=12)

    def calcular_total(self):
        try:
            fecha_sal = datetime.strptime(self.entry_salida.get().strip(), "%Y-%m-%d")
            huesped = self.habitacion.huesped
            if fecha_sal < huesped.fecha_ingreso:
                raise ValueError("La fecha de salida no puede ser anterior a la fecha de ingreso.")

            huesped.fecha_salida = fecha_sal
            dias = huesped.obtener_dias_alojamiento()
            total = dias * self.habitacion.precio_dia

            self.lbl_dias.config(text=f"Cantidad de días: {dias}")
            self.lbl_total.config(text=f"Total a pagar: ${total:,.2f}")
            self.btn_registrar_salida.config(state="normal")
        except ValueError as e:
            messagebox.showerror("Error en Fecha", str(e), parent=self)

    def confirmar_salida(self):
        self.habitacion.huesped = None
        self.habitacion.disponible = True
        messagebox.showinfo("Salida Registrada", f"La habitación {self.habitacion.numero_habitacion} ahora está disponible.", parent=self)
        self.destroy()


class VentanaEjercicio8_5(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Ejercicio 8.5: Gestión de Contenido (Hotel)")
        self.geometry("450x290")
        self.hotel = Hotel()

        # Barra de Menú
        menubar = tk.Menu(self)
        menu_hotel = tk.Menu(menubar, tearoff=0)
        menu_hotel.add_command(label="Consultar habitaciones", command=self.abrir_habitaciones)
        menu_hotel.add_command(label="Salida de huéspedes", command=self.solicitar_salida)
        menubar.add_cascade(label="Menú", menu=menu_hotel)
        self.config(menu=menubar)

        lbl_titulo = tk.Label(
            self,
            text="Sistema de Gestión Hotelera (10 Habitaciones)\nSeleccione una operación desde el menú o botones:",
            font=("Arial", 10),
            pady=20
        )
        lbl_titulo.pack()

        tk.Button(self, text="1. Consultar Habitaciones / Registrar Ingreso", command=self.abrir_habitaciones, width=38, pady=6, bg="#e8f5e9").pack(pady=8)
        tk.Button(self, text="2. Registrar Salida de Huésped (Check-Out)", command=self.solicitar_salida, width=38, pady=6, bg="#fff3e0").pack(pady=8)

    def abrir_habitaciones(self):
        VentanaHabitaciones(self, self.hotel)

    def solicitar_salida(self):
        dialogo = tk.Toplevel(self)
        dialogo.title("Salida de Huéspedes")
        dialogo.geometry("300x140")
        dialogo.grab_set()

        tk.Label(dialogo, text="Ingrese número de habitación (1-10):").pack(pady=10)
        spin = tk.Spinbox(dialogo, from_=1, to=10, width=10)
        spin.pack(pady=5)

        def validar():
            try:
                num = int(spin.get())
                hab = self.hotel.buscar_habitacion(num)
                if not hab:
                    raise ValueError("Habitación no existe.")
                if hab.disponible:
                    messagebox.showinfo("Disponible", f"La habitación {num} no está ocupada actualmente.", parent=dialogo)
                    return
                dialogo.destroy()
                VentanaSalida(self, self.hotel, num)
            except ValueError as e:
                messagebox.showerror("Error", str(e), parent=dialogo)

        tk.Button(dialogo, text="Aceptar", command=validar, bg="#e3f2fd", width=12).pack(pady=10)
