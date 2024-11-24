from ventana_login import VentanaLogin
from main import Aplicacion

# Clase Controlador: Gestiona el flujo principal de la aplicación implementando el patrón MVC
# - Maneja la navegación entre ventanas
# - Controla el estado de la sesión del usuario
# - Coordina la comunicación entre los diferentes módulos
class Controlador:
    # Inicializa el controlador principal
    # - Establece las referencias iniciales a None para las ventanas
    # - Prepara el sistema para comenzar con el flujo de autenticación
    def __init__(self):
        self.ventana_login = None
        self.aplicacion = None
        self.iniciar()
    
    # Inicia el flujo de la aplicación
    # - Crea la ventana de login
    # - Establece esta ventana como punto de entrada
    # - Inicia el bucle de eventos de tkinter
    def iniciar(self):
        self.ventana_login = VentanaLogin(self)
        self.ventana_login.mainloop()
    
    # Gestiona la transición del login a la aplicación principal
    # - Oculta la ventana de login
    # - Inicializa la aplicación principal con los datos del usuario
    # - Establece el nuevo contexto de la aplicación
    def iniciar_aplicacion(self, usuario):
        self.ventana_login.withdraw()
        self.aplicacion = Aplicacion(usuario, self)
        self.aplicacion.mainloop()
    
    # Gestiona el retorno a la pantalla de login
    # - Limpia el estado de la aplicación principal
    # - Restaura la vista de login
    # - Permite reiniciar el flujo de autenticación
    def volver_login(self):
        if self.aplicacion:
            self.aplicacion.root.destroy()
        self.ventana_login.deiconify()
