# Clase que representa un participante de la encuesta
class Participante:    
    def __init__(self, nombre, email, edad=None, genero=None):
        self.nombre = nombre
        self.email = email
        self.edad = edad
        self.genero = genero
        self.datos_adicionales = {}

    # Agrega un dato adicional al participante   
    def agregar_dato(self, clave, valor):
        self.datos_adicionales[clave] = valor
