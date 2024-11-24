import tkinter as tk
from tkinter import ttk, messagebox


class DialogoNuevoParticipante(tk.Toplevel):
    def __init__(self, parent):
        # Configura el diálogo modal para ingreso de nuevo participante
        super().__init__(parent)
        self.title("Nuevo Participante")
        self.geometry("400x300")
        self.resizable(False, False)

        # Inicializar los StringVars
        self.nombre_var = tk.StringVar(self)
        self.email_var = tk.StringVar(self)
        self.edad_var = tk.StringVar(self)
        self.genero_var = tk.StringVar(self)

        self.participante = None

        # Hacer que la clase sea modal
        self.transient(parent)
        self.grab_set()

        self.crear_widgets()
        self.center_window()
    # Crea los widgets del diálogo

    def crear_widgets(self):
        frame = ttk.Frame(self, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        ttk.Label(frame, text="Nombre:").grid(
            row=0, column=0, sticky=tk.W, pady=5)
        self.nombre_entry = ttk.Entry(frame, width=30)
        self.nombre_entry.grid(row=0, column=1, pady=5)

        ttk.Label(frame, text="Email:").grid(
            row=1, column=0, sticky=tk.W, pady=5)
        self.email_entry = ttk.Entry(frame, width=30)
        self.email_entry.grid(row=1, column=1, pady=5)
        ttk.Label(frame, text="Edad:").grid(
            row=2, column=0, sticky=tk.W, pady=5)
        self.edad_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.edad_var,
                  width=30).grid(row=2, column=1, pady=5)

        ttk.Label(frame, text="Género:").grid(
            row=3, column=0, sticky=tk.W, pady=5)
        self.genero_var = tk.StringVar()
        ttk.Combobox(frame, textvariable=self.genero_var,
                     values=["Masculino", "Femenino", "Otro"],
                     width=27).grid(row=3, column=1, pady=5)

        # Botones
        frame_botones = ttk.Frame(frame)
        frame_botones.grid(row=4, column=0, columnspan=2, pady=20)

        ttk.Button(frame_botones, text="Guardar",
                   command=self.guardar).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_botones, text="Cancelar",
                   command=self.destroy).pack(side=tk.LEFT, padx=5)

    # Guarda los datos del nuevo participante
    def guardar(self):
        nombre = self.nombre_entry.get()
        email = self.email_entry.get()
        edad = self.edad_var.get()
        genero = self.genero_var.get()
        # Print captured values
        print(f"Nombre: {nombre}\nEmail: {
              email}\nEdad: {edad}\nGénero: {genero}")

        if nombre.strip() and email.strip():
            self.participante = (
                nombre,
                email,
                self.edad_var.get(),
                self.genero_var.get()
            )
            self.destroy()
        else:
            messagebox.showerror("Error", "Nombre y email son obligatorios")

    # Valida los datos ingresados
    def validar_datos(self):
        if not self.nombre_var.get().strip() or not self.email_var.get().strip():
            messagebox.showerror("Error", "Nombre y email son obligatorios")
            return False
        try:
            if self.edad_var.get():
                edad = int(self.edad_var.get())
                if edad < 0 or edad > 120:
                    raise ValueError
        except ValueError:
            messagebox.showerror("Error", "La edad debe ser un número válido")
            return False
        return True

    # Centra la ventana en la pantalla
    def center_window(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')
