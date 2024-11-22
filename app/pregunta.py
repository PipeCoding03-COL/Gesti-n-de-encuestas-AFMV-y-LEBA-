class Pregunta:
    """Clase que representa una pregunta de la encuesta"""
    
    def __init__(self, texto, tipo):
        self.texto = texto
        self.tipo = tipo  # 'multiple', 'abierta', 'escala'
        self.opciones = []
        
    def agregar_opcion(self, opcion):
        """Agrega una opción para preguntas de tipo múltiple"""
        if self.tipo == 'multiple':
            self.opciones.append(opcion)
