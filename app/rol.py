from enum import Enum

class TipoRol(Enum):
    COORDINADOR = "Coordinador de Estudios"
    ANALISTA = "Analista de Resultados"

class Rol:
    def __init__(self, tipo):
        self.tipo = tipo
        self.permisos = self._asignar_permisos()

    def _asignar_permisos(self):
        if self.tipo == TipoRol.COORDINADOR:
            return {
                'crear_encuesta': True,
                'editar_encuesta': True,
                'eliminar_encuesta': True,
                'publicar_encuesta': True,
                'ver_resultados': True,
                'generar_informes': True,
                'exportar_datos': True,
                'gestionar_usuarios': True
            }
        elif self.tipo == TipoRol.ANALISTA:
            return {
                'crear_encuesta': False,
                'editar_encuesta': False,
                'eliminar_encuesta': False,
                'publicar_encuesta': False,
                'ver_resultados': True,
                'generar_informes': True,
                'exportar_datos': True,
                'gestionar_usuarios': False
            }
