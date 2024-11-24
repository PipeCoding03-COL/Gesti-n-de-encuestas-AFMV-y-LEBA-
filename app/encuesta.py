from datetime import datetime

# Modelo de encuesta
# Define la estructura y comportamiento de las encuestas
class Encuesta:
    def __init__(self, titulo, descripcion, creador):
        # Inicializa una nueva encuesta con sus atributos básicos
        self.titulo = titulo
        self.descripcion = descripcion
        self.creador = creador
        self.preguntas = []
        self.fecha_creacion = datetime.now()
        self.fecha_publicacion = None
        self.fecha_cierre = None
        self.estado = "borrador"  # borrador, publicada, cerrada
        self.participantes = []
        self.respuestas = {}

    def agregar_pregunta(self, texto, tipo, opciones=None):
        pregunta = {
            'texto': texto,
            'tipo': tipo,
            'opciones': opciones
        }
        self.preguntas.append(pregunta)


    def publicar(self, fecha_cierre=None):
        self.estado = "publicada"
        self.fecha_publicacion = datetime.now()
        self.fecha_cierre = fecha_cierre

    def cerrar(self):
        self.estado = "cerrada"
        self.fecha_cierre = datetime.now()

    def agregar_participante(self, participante):
        self.participantes.append(participante)

    def registrar_respuesta(self, participante_id, pregunta_id, respuesta):
        if participante_id not in self.respuestas:
            self.respuestas[participante_id] = {}
        self.respuestas[participante_id][pregunta_id] = respuesta

    def obtener_estadisticas(self):
        total_participantes = len(self.participantes)
        total_respuestas = len(self.respuestas)
        tasa_respuesta = (total_respuestas / total_participantes) if total_participantes > 0 else 0

        return {
            'total_participantes': total_participantes,
            'total_respuestas': total_respuestas,
            'tasa_respuesta': tasa_respuesta,
            'estado': self.estado
        }
