import tkinter as tk
from ventana_login import VentanaLogin
from main import Aplicacion

class Controlador:
    def __init__(self):
        self.ventana_login = None
        self.aplicacion = None
        self.iniciar()
    
    def iniciar(self):
        self.ventana_login = VentanaLogin(self)
        self.ventana_login.mainloop()
    
    def iniciar_aplicacion(self, usuario):
        self.ventana_login.withdraw()
        self.aplicacion = Aplicacion(usuario, self)
        self.aplicacion.mainloop()
    
    def volver_login(self):
        if self.aplicacion:
            self.aplicacion.root.destroy()
        self.ventana_login.deiconify()
