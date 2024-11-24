from estudio import Estudio


class Coordinador:
    def __init__(self, nombre, email, rol="coordinador"):
        self.nombre = nombre
        self.email = email
        self.rol = rol
        self.estudios_asignados = []

    def crear_estudio(self, titulo, descripcion, tipo):
        nuevo_estudio = Estudio(titulo, descripcion, tipo, self)
        self.estudios_asignados.append(nuevo_estudio)
        return nuevo_estudio

    def obtener_estudios(self):
        return self.estudios_asignados

    def obtener_estadisticas(self):
        return {
            'total_estudios': len(self.estudios_asignados),
            'estudios_activos': len([e for e in self.estudios_asignados if e.estado == "en_curso"]),
            'estudios_finalizados': len([e for e in self.estudios_asignados if e.estado == "finalizado"])
        }
