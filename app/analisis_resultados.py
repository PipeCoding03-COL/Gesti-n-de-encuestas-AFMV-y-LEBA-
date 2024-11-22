import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

class AnalizadorResultados:
    def __init__(self, estudio):
        self.estudio = estudio
        self.resultados = None
        
    def analizar(self):
        self.resultados = {
            'informacion_general': self.obtener_info_general(),
            'estadisticas': self.calcular_estadisticas(),
            'graficos': self.generar_graficos(),
            'datos_crudos': self.obtener_datos_crudos()
        }
        return self.resultados
        
    def obtener_info_general(self):
        return {
            'titulo_estudio': self.estudio.titulo,
            'tipo_estudio': self.estudio.tipo,
            'fecha_inicio': self.estudio.fecha_inicio,
            'fecha_fin': self.estudio.fecha_fin,
            'total_participantes': len(self.estudio.grupo_objetivo),
            'total_respuestas': len(self.estudio.encuesta.respuestas)
        }
        
    def calcular_estadisticas(self):
        stats = {}
        for pregunta in self.estudio.encuesta.preguntas:
            respuestas = self.obtener_respuestas_pregunta(pregunta['id'])
            if pregunta['tipo'] == 'multiple':
                stats[pregunta['id']] = self.analizar_pregunta_multiple(respuestas)
            elif pregunta['tipo'] == 'abierta':
                stats[pregunta['id']] = self.analizar_pregunta_abierta(respuestas)
        return stats
        
    def generar_graficos(self):
        graficos = {}
        for pregunta in self.estudio.encuesta.preguntas:
            if pregunta['tipo'] == 'multiple':
                graficos[pregunta['id']] = self.generar_grafico_pregunta(pregunta)
        return graficos
        
    def obtener_datos_crudos(self):
        datos = []
        for participante_id, respuestas in self.estudio.encuesta.respuestas.items():
            participante = self.obtener_participante(participante_id)
            for pregunta_id, respuesta in respuestas.items():
                datos.append({
                    'participante_id': participante_id,
                    'pregunta_id': pregunta_id,
                    'respuesta': respuesta,
                    'datos_demograficos': participante.datos_adicionales
                })
        return datos
        
    def exportar_resultados(self, formato='csv'):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        if formato == 'csv':
            df = pd.DataFrame(self.obtener_datos_crudos())
            df.to_csv(f'resultados_{self.estudio.titulo}_{timestamp}.csv', index=False)
