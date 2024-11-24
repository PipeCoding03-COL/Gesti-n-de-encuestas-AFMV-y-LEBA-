import tkinter as tk
from gestion_usuarios import GestionUsuarios

# Punto de entrada principal de la aplicación
# Maneja la inicialización de la ventana de login y la configuración básica
class Aplicacion:
    def __init__(self, root):
        # Inicializa la ventana principal y las variables core
        self.root = root
        self.root.title("Sistema de Encuestas")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        self.correo_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.gestion_usuarios = GestionUsuarios()

        self.crear_widgets()

if __name__ == "__main__":
    from ventana_login import VentanaLogin
    app = VentanaLogin()
    app.mainloop()
