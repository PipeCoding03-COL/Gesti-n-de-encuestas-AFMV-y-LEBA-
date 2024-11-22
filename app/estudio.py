from datetime import datetime
from encuesta import Encuesta

class Estudio:
    """Clase que representa un estudio completo"""
    
    def __init__(self, titulo, descripcion, tipo, coordinador):
        self.titulo = titulo
        self.descripcion = descripcion
        self.tipo = tipo  # satisfaccion_cliente, clima_laboral, marketing
        self.coordinador = coordinador
        self.fecha_creacion = datetime.now()
        self.fecha_inicio = None
        self.fecha_fin = None
        self.estado = "preparacion"  # preparacion, en_curso, finalizado
        self.encuesta = None
        self.grupo_objetivo = []
        self.resultados = None
        
    def crear_encuesta(self, encuesta):
        self.encuesta = encuesta
        
    def definir_grupo_objetivo(self, participantes, criterios=None):
        if criterios:
            self.grupo_objetivo = self.filtrar_participantes(participantes, criterios)
        else:
            self.grupo_objetivo = participantes
            
    def iniciar_estudio(self):
        if self.encuesta and self.grupo_objetivo:
            self.estado = "en_curso"
            self.fecha_inicio = datetime.now()
            self.encuesta.publicar()
            
    def finalizar_estudio(self):
        self.estado = "finalizado"
        self.fecha_fin = datetime.now()
        self.encuesta.cerrar()
        self.generar_resultados()
        
    def filtrar_participantes(self, participantes, criterios):
        filtrados = participantes
        for criterio, valor in criterios.items():
            filtrados = [p for p in filtrados if self.cumple_criterio(p, criterio, valor)]
        return filtrados
        
    def cumple_criterio(self, participante, criterio, valor):
        if criterio == 'edad':
            return int(participante.edad) >= valor[0] and int(participante.edad) <= valor[1]
        elif criterio == 'genero':
            return participante.genero == valor
        elif criterio == 'ciudad':
            return participante.datos_adicionales.get('ciudad') == valor
        return True
