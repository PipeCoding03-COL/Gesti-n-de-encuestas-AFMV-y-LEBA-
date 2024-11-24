import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ventana_participantes import VentanaParticipantes

# Ventana principal de la aplicación
# Proporciona acceso a todas las funcionalidades principales del sistema
class VentanaPrincipal:
    def __init__(self, usuario, parent):
        # Inicializa la interfaz principal con el usuario autenticado
        self.parent = parent
        self.usuario = usuario
        self.root = tk.Tk()
        self.root.title(f"Sistema de Encuestas - {usuario.nombre}")
        self.root.geometry("800x600")
        self.crear_widgets()

    def crear_widgets(self):
        # Menú principal
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)
        
        # Menú Encuestas
        menu_encuestas = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Encuestas", menu=menu_encuestas)
        
        if self.usuario.puede_crear_encuesta():
            menu_encuestas.add_command(label="Gestionar Encuestas", 
                                     command=self.abrir_gestionar_encuestas)
            
        if self.usuario.puede_ver_resultados():
            menu_encuestas.add_command(label="Ver Resultados", 
                                     command=self.abrir_resultados)
            
        # Menú Administración
        if self.usuario.puede_gestionar_usuarios():
            menu_admin = tk.Menu(menu_bar, tearoff=0)
            menu_bar.add_cascade(label="Administración", menu=menu_admin)
            menu_admin.add_command(label="Gestionar participantes", 
                                 command=self.gestionar_usuarios)
        
        # Menú Usuario
        menu_usuario = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Usuario", menu=menu_usuario)
        menu_usuario.add_command(label="Cerrar Sesión", command=self.cerrar_sesion)
        menu_usuario.add_command(label="Salir", command=self.cerrar_aplicacion)

        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill="both", expand=True)
        
        # Mensaje de bienvenida
        ttk.Label(
            main_frame, 
            text=f"Bienvenido/a {self.usuario.nombre}",
            font=('Helvetica', 16)
        ).pack(pady=20)
        
        # Información del rol
        ttk.Label(
            main_frame,
            text=f"Rol: {self.usuario.rol.tipo.value}",
            font=('Helvetica', 12)
        ).pack(pady=10)
        
        # Frame para botones
        botones_frame = ttk.Frame(main_frame)
        botones_frame.pack(pady=20)
        
        # Botones según permisos
        if self.usuario.puede_crear_encuesta():
            ttk.Button(
                botones_frame,
                text="Gestionar Encuestas",
                command=self.abrir_gestionar_encuestas
            ).pack(pady=5)
            
        if self.usuario.puede_ver_resultados():
            ttk.Button(
                botones_frame,
                text="Ver Resultados",
                command=self.abrir_resultados
            ).pack(pady=5)
            
        if self.usuario.puede_gestionar_usuarios():
            ttk.Button(
                botones_frame,
                text="Gestionar Usuarios",
                command=self.gestionar_usuarios
            ).pack(pady=5)

    def abrir_gestionar_encuestas(self):
        from ventana_edicion import VentanaGestionarEncuestas
        ventana = VentanaGestionarEncuestas(self.root)

    def abrir_resultados(self):
        pass

    def gestionar_usuarios(self):
        VentanaParticipantes(self.root)

    def cerrar_sesion(self):
        if messagebox.askyesno("Cerrar Sesión", "¿Está seguro que desea cerrar sesión?"):
            self.root.destroy()
            self.parent.deiconify()

    def cerrar_aplicacion(self):
        if messagebox.askyesno("Salir", "¿Está seguro que desea salir?"):
            self.root.quit()

    def mainloop(self):
        self.root.mainloop()
