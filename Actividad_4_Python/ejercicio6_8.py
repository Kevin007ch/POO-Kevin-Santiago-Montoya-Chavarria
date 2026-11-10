import tkinter as tk
from tkinter import filedialog, messagebox

class LectorArchivos:
    @staticmethod
    def leer_contenido(ruta_archivo: str) -> str:
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            return f.read()

class VentanaEjercicio6_8(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Ejercicio 6.8: Lectura de Archivos (IOError)")
        self.geometry("550x380")

        btn_abrir = tk.Button(self, text="Seleccionar y Abrir Archivo (.txt)", command=self.abrir_archivo, bg="#fff3e0")
        btn_abrir.pack(fill="x", padx=10, pady=10)

        self.txt_area = tk.Text(self, wrap="word")
        self.txt_area.pack(expand=True, fill="both", padx=10, pady=10)

    def abrir_archivo(self):
        ruta = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
        if ruta:
            try:
                contenido = LectorArchivos.leer_contenido(ruta)
                self.txt_area.delete("1.0", tk.END)
                self.txt_area.insert(tk.END, contenido)
            except FileNotFoundError:
                messagebox.showerror("Error de Archivo", "El archivo no existe o no fue encontrado.")
            except IOError as ex:
                messagebox.showerror("IOError Capturado", f"Error al intentar leer el archivo: {ex}")
            except Exception as ex:
                messagebox.showerror("Error Inesperado", str(ex))
