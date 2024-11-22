import tkinter as tk
from tkinter import ttk, messagebox
from main import Aplicacion
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
        
        # Sistema de usuarios - creado cada vez
        self.gestion_usuarios = GestionUsuarios()
        
        # Variables
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
        correo = self.correo_var.get()
        password = self.password_var.get()
        
        usuario = self.gestion_usuarios.validar_credenciales(correo, password)
        if usuario:
            self.iniciar_aplicacion(usuario)
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")
            
    def iniciar_aplicacion(self, usuario):
        self.withdraw()
        # Import here to avoid circular import
        from main import Aplicacion
        app = Aplicacion(usuario, self)  # Pass login window as parent
        app.mainloop()

    def cerrar_aplicacion(self, app):
        app.root.destroy()
        self.destroy()

def main():
    app = VentanaLogin()
    app.mainloop()

if __name__ == "__main__":
    main()
