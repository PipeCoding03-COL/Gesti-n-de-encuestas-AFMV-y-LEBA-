# Clase que representa una pregunta de la encuesta 
class Pregunta:   
    def __init__(self, texto, tipo):
        self.texto = texto
        self.tipo = tipo  # 'multiple', 'abierta', 'escala'
        self.opciones = []
        
    # Agrega una opción para preguntas de tipo múltiple"
    def agregar_opcion(self, opcion):
        if self.tipo == 'multiple':
            self.opciones.append(opcion)
