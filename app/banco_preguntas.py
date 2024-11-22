class BancoPreguntas:
    def __init__(self):
        self.tipos_pregunta = {
            'multiple': {
                'nombre': 'Opción Múltiple',
                'opciones': ['Totalmente de acuerdo', 'De acuerdo', 'Neutral', 'En desacuerdo', 'Totalmente en desacuerdo']
            },
            'si_no': {
                'nombre': 'Sí/No',
                'opciones': ['Sí', 'No']
            },
            'escala_5': {
                'nombre': 'Escala 1-5',
                'opciones': ['1', '2', '3', '4', '5']
            },
            'escala_10': {
                'nombre': 'Escala 1-10',
                'opciones': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
            },
            'probabilidad': {
                'nombre': 'Probabilidad',
                'opciones': ['Muy probable', 'Probable', 'Neutral', 'Poco probable', 'Nada probable']
            },
            'satisfaccion': {
                'nombre': 'Satisfacción',
                'opciones': ['Muy satisfecho', 'Satisfecho', 'Neutral', 'Insatisfecho', 'Muy insatisfecho']
            },
            'frecuencia': {
                'nombre': 'Frecuencia',
                'opciones': ['Siempre', 'Frecuentemente', 'A veces', 'Raramente', 'Nunca']
            },
            'importancia': {
                'nombre': 'Importancia',
                'opciones': ['Muy importante', 'Importante', 'Moderadamente importante', 'Poco importante', 'Nada importante']
            },
            'dificultad': {
                'nombre': 'Dificultad',
                'opciones': ['Muy fácil', 'Fácil', 'Moderado', 'Difícil', 'Muy difícil']
            },
            'calidad': {
                'nombre': 'Calidad',
                'opciones': ['Excelente', 'Buena', 'Regular', 'Mala', 'Muy mala']
            },
            'utilidad': {
                'nombre': 'Utilidad',
                'opciones': ['Muy útil', 'Útil', 'Neutral', 'Poco útil', 'Nada útil']
            },
            'tiempo': {
                'nombre': 'Tiempo',
                'opciones': ['Menos de 1 hora', '1-3 horas', '3-6 horas', '6-12 horas', 'Más de 12 horas']
            },
            'abierta': {
                'nombre': 'Respuesta Abierta',
                'opciones': ['Texto libre']  # Mantenemos la estructura pero solo será informativo
            },
        }

        self.preguntas = {
            'Satisfacción Laboral': [
                {'texto': '¿Qué aspectos de tu trabajo actual te resultan más satisfactorios?', 'tipo': 'abierta'},
                {'texto': '¿Qué cambios sugerirías para mejorar el ambiente laboral?', 'tipo': 'abierta'},
                {'texto': '¿Cómo describirías la cultura de la empresa?', 'tipo': 'abierta'},
                {'texto': '¿Qué aspectos de tu trabajo te generan mayor estrés?', 'tipo': 'abierta'},
                {'texto': '¿Qué sugerencias tienes para mejorar la comunicación en el equipo?', 'tipo': 'abierta'}
            ],
            'Desarrollo Profesional': [
                {'texto': '¿Cuáles son tus objetivos profesionales a largo plazo?', 'tipo': 'abierta'},
                {'texto': '¿Qué habilidades te gustaría desarrollar en tu rol actual?', 'tipo': 'abierta'},
                {'texto': '¿Qué tipo de capacitación consideras necesaria para tu desarrollo?', 'tipo': 'abierta'},
                {'texto': '¿Cómo visualizas tu carrera en los próximos 5 años?', 'tipo': 'abierta'},
                {'texto': '¿Qué proyectos te gustaría liderar?', 'tipo': 'abierta'}
            ],
            'Liderazgo': [
                {'texto': '¿Cómo describirías el estilo de liderazgo de tu supervisor?', 'tipo': 'abierta'},
                {'texto': '¿Qué características consideras esenciales en un buen líder?', 'tipo': 'abierta'},
                {'texto': '¿Cómo podría mejorar la comunicación con tu supervisor?', 'tipo': 'abierta'},
                {'texto': '¿Qué sugerencias tienes para mejorar las reuniones de equipo?', 'tipo': 'abierta'},
                {'texto': '¿Cómo te gustaría que se manejara el reconocimiento en el equipo?', 'tipo': 'abierta'}
            ],
            'Procesos y Eficiencia': [
                {'texto': '¿Qué procesos consideras que necesitan optimización?', 'tipo': 'abierta'},
                {'texto': '¿Qué herramientas adicionales necesitas para ser más eficiente?', 'tipo': 'abierta'},
                {'texto': '¿Cómo podríamos reducir el tiempo en tareas repetitivas?', 'tipo': 'abierta'},
                {'texto': '¿Qué sugerencias tienes para mejorar la colaboración entre departamentos?', 'tipo': 'abierta'},
                {'texto': '¿Qué obstáculos encuentras en tu trabajo diario?', 'tipo': 'abierta'}
            ],
            'Innovación': [
                {'texto': '¿Qué ideas innovadoras tienes para mejorar nuestros productos/servicios?', 'tipo': 'abierta'},
                {'texto': '¿Cómo podríamos fomentar más la creatividad en el equipo?', 'tipo': 'abierta'},
                {'texto': '¿Qué tendencias del mercado deberíamos estar considerando?', 'tipo': 'abierta'},
                {'texto': '¿Qué tecnologías nuevas consideras que deberíamos implementar?', 'tipo': 'abierta'},
                {'texto': '¿Cómo podríamos mejorar nuestra ventaja competitiva?', 'tipo': 'abierta'}
            ],
            'Clima Organizacional': [
                {'texto': '¿Qué hace única a nuestra cultura organizacional?', 'tipo': 'abierta'},
                {'texto': '¿Cómo podríamos mejorar el balance vida-trabajo?', 'tipo': 'abierta'},
                {'texto': '¿Qué actividades sugieres para fortalecer el trabajo en equipo?', 'tipo': 'abierta'},
                {'texto': '¿Qué aspectos del ambiente laboral te gustaría cambiar?', 'tipo': 'abierta'},
                {'texto': '¿Cómo podríamos mejorar la integración de nuevos empleados?', 'tipo': 'abierta'}
            ],
            'Servicio al Cliente': [
                {'texto': '¿Qué feedback recibes frecuentemente de los clientes?', 'tipo': 'abierta'},
                {'texto': '¿Cómo podríamos mejorar la experiencia del cliente?', 'tipo': 'abierta'},
                {'texto': '¿Qué necesidades no cubiertas has identificado en los clientes?', 'tipo': 'abierta'},
                {'texto': '¿Qué sugerencias tienes para mejorar nuestro servicio post-venta?', 'tipo': 'abierta'},
                {'texto': '¿Cómo podríamos superar las expectativas de los clientes?', 'tipo': 'abierta'}
            ],
            'Bienestar': [
                {'texto': '¿Qué iniciativas de bienestar te gustaría ver en la empresa?', 'tipo': 'abierta'},
                {'texto': '¿Cómo podríamos mejorar el ambiente físico de trabajo?', 'tipo': 'abierta'},
                {'texto': '¿Qué programas de salud te interesarían?', 'tipo': 'abierta'},
                {'texto': '¿Qué actividades sugieres para reducir el estrés laboral?', 'tipo': 'abierta'},
                {'texto': '¿Cómo podríamos promover hábitos saludables en el trabajo?', 'tipo': 'abierta'}
            ]
        }

    def obtener_tipos_pregunta(self):
        return self.tipos_pregunta

    def obtener_categoria(self, categoria):
        return self.preguntas.get(categoria, [])

    def obtener_categorias(self):
        return list(self.preguntas.keys())
    
    def obtener_preguntas(self, categoria):
        # Retorna la lista de preguntas de la categoría seleccionada
        return self.preguntas.get(categoria, [])

    def agregar_pregunta(self, categoria, pregunta, tipo, opciones_personalizadas=None):
        if categoria not in self.preguntas:
            self.preguntas[categoria] = []
            
        nueva_pregunta = {
            'texto': pregunta,
            'tipo': tipo,
            'opciones_personalizadas': opciones_personalizadas
        }
        
        self.preguntas[categoria].append(nueva_pregunta)

    def personalizar_opciones(self, categoria, indice_pregunta, opciones_nuevas):
        if categoria in self.preguntas and indice_pregunta < len(self.preguntas[categoria]):
            self.preguntas[categoria][indice_pregunta]['opciones_personalizadas'] = opciones_nuevas
