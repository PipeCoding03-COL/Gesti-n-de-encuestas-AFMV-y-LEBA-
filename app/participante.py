class Participante:
    """Clase que representa un participante de la encuesta"""
    
    def __init__(self, nombre, email, edad=None, genero=None):
        self.nombre = nombre
        self.email = email
        self.edad = edad
        self.genero = genero
        self.datos_adicionales = {}
        
    def agregar_dato(self, clave, valor):
        """Agrega un dato adicional al participante"""
        self.datos_adicionales[clave] = valor
