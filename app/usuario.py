class Usuario:
    def __init__(self, nombre, correo, contraseña, rol):
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña  # Debe ser encriptada en producción
        self.rol = rol
        self.activo = True

    def tiene_permiso(self, permiso):
        return self.rol.permisos.get(permiso, False)

    def puede_crear_encuesta(self):
        return self.tiene_permiso('crear_encuesta')

    def puede_ver_resultados(self):
        return self.tiene_permiso('ver_resultados')

    def puede_generar_informes(self):
        return self.tiene_permiso('generar_informes')

    def puede_gestionar_usuarios(self):
        return self.tiene_permiso('gestionar_usuarios')
