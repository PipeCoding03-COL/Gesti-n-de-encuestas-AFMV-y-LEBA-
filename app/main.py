import tkinter as tk
from tkinter import ttk, messagebox
from gestion_usuarios import GestionUsuarios

class VentanaLogin(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Encuestas - Login")
        self.geometry("400x300")
        self.resizable(False, False)
        
        # Centrar la ventana
        ancho_ventana = 400
        alto_ventana = 300
        x_ventana = self.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.winfo_screenheight() // 2 - alto_ventana // 2
        self.geometry(f"{ancho_ventana}x{alto_ventana}+{x_ventana}+{y_ventana}")
        
        self.correo_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.gestion_usuarios = GestionUsuarios()
        
        self.crear_widgets()

    def crear_widgets(self):
        main_frame = ttk.Frame(self, padding="20")
        main_frame.pack(fill="both", expand=True)
        
        titulo = ttk.Label(main_frame, text="Iniciar Sesión", font=('Helvetica', 14, 'bold'))
        titulo.pack(pady=10)
        
        ttk.Label(main_frame, text="Correo:").pack(fill="x", pady=(10,0))
        ttk.Entry(main_frame, textvariable=self.correo_var).pack(fill="x")
        
        ttk.Label(main_frame, text="Contraseña:").pack(fill="x", pady=(10,0))
        ttk.Entry(main_frame, textvariable=self.password_var, show="*").pack(fill="x")
        
        ttk.Button(main_frame, text="Iniciar Sesión", command=self.login).pack(fill="x", pady=20)
        
        self.bind('<Return>', lambda e: self.login())

    def login(self):
        """correo = self.correo_var.get()
        password = self.password_var.get()"""
        correo = "andres@project.us"
        password = "Cali"
        
        usuario = self.gestion_usuarios.validar_credenciales(correo, password)
        if usuario:
            self.iniciar_aplicacion(usuario)
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")

    def iniciar_aplicacion(self, usuario):
        self.withdraw()
        ventana_principal = VentanaPrincipal(usuario, self)
        ventana_principal.mainloop()

class VentanaPrincipal:
    def __init__(self, usuario, parent):
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
            menu_admin.add_command(label="Gestionar Usuarios", 
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
        pass

    def cerrar_sesion(self):
        if messagebox.askyesno("Cerrar Sesión", "¿Está seguro que desea cerrar sesión?"):
            self.root.destroy()
            self.parent.deiconify()

    def cerrar_aplicacion(self):
        if messagebox.askyesno("Salir", "¿Está seguro que desea salir?"):
            self.root.quit()

    def mainloop(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = VentanaLogin()
    app.mainloop()
