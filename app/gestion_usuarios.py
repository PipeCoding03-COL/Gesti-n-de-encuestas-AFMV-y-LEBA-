from rol import TipoRol, Rol
from usuario import Usuario

# Gestión de usuarios del sistema
# Maneja la autenticación y administración de usuarios
class GestionUsuarios:
    def __init__(self):
        # Inicializa el sistema de gestión de usuarios
        self.usuarios = {}
        self.crear_usuarios_iniciales()
    
    def crear_usuarios_iniciales(self):
        # Coordinadores
        self.agregar_usuario(
            Usuario("Andrés F. Martínez V.", 
                   "andres@project.us", 
                   "Cali", 
                   Rol(TipoRol.COORDINADOR))
        )
        self.agregar_usuario(
            Usuario("Leymar E. Buenaventura L.", 
                   "leymar@project.us", 
                   "Tura", 
                   Rol(TipoRol.COORDINADOR))
        )
        self.agregar_usuario(
            Usuario("Diego Marín", 
                   "dmarin@ulibrecali.co", 
                   "ULibre", 
                   Rol(TipoRol.COORDINADOR))
        )
        
        # Analistas
        self.agregar_usuario(
            Usuario("Harold Preciado", 
                   "hpreciado@auditorias.co", 
                   "analista1", 
                   Rol(TipoRol.ANALISTA))
        )
    
    def agregar_usuario(self, usuario):
        self.usuarios[usuario.correo] = usuario
    
    def obtener_usuario(self, correo):
        return self.usuarios.get(correo)
    
    def validar_credenciales(self, correo, contraseña):
        usuario = self.obtener_usuario(correo)
        if usuario and usuario.contraseña == contraseña:
            return usuario
        return None
