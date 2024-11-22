import tkinter as tk
from tkinter import ttk, messagebox

class VentanaUsuarios(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Gestión de Usuarios")
        self.geometry("800x600")
        
        self.crear_widgets()
        
    def crear_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self, padding="10")
        main_frame.pack(fill="both", expand=True)
        
        # Botones de acción
        botones_frame = ttk.Frame(main_frame)
        botones_frame.pack(fill="x", pady=5)
        
        ttk.Button(botones_frame, text="Nuevo Usuario", command=self.nuevo_usuario).pack(side="left", padx=5)
        ttk.Button(botones_frame, text="Editar Usuario", command=self.editar_usuario).pack(side="left", padx=5)
        ttk.Button(botones_frame, text="Eliminar Usuario", command=self.eliminar_usuario).pack(side="left", padx=5)
        
        # Lista de usuarios
        self.lista_usuarios = ttk.Treeview(main_frame, 
                                         columns=("nombre", "correo", "rol", "estado"),
                                         show="headings")
        
        self.lista_usuarios.heading("nombre", text="Nombre")
        self.lista_usuarios.heading("correo", text="Correo")
        self.lista_usuarios.heading("rol", text="Rol")
        self.lista_usuarios.heading("estado", text="Estado")
        
        self.lista_usuarios.column("nombre", width=200)
        self.lista_usuarios.column("correo", width=200)
        self.lista_usuarios.column("rol", width=150)
        self.lista_usuarios.column("estado", width=100)
        
        scrolly = ttk.Scrollbar(main_frame, orient="vertical", command=self.lista_usuarios.yview)
        self.lista_usuarios.configure(yscrollcommand=scrolly.set)
        
        self.lista_usuarios.pack(fill="both", expand=True)
        scrolly.pack(side="right", fill="y")
        
        # Cargar datos
        self.cargar_usuarios()
        
    def cargar_usuarios(self):
        # Aquí cargarías los usuarios desde tu sistema de almacenamiento
        pass
        
    def nuevo_usuario(self):
        # Implementar creación de nuevo usuario
        pass
        
    def editar_usuario(self):
        seleccion = self.lista_usuarios.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Por favor seleccione un usuario")
            return
        # Implementar edición de usuario
        
    def eliminar_usuario(self):
        seleccion = self.lista_usuarios.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Por favor seleccione un usuario")
            return
        # Implementar eliminación de usuario