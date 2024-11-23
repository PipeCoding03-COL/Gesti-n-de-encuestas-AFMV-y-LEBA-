# SISTEMA DE GESTIÓN DE ENCUESTAS
Sistema para crear, gestionar y analizar encuestas de manera eficiente.

## Realizado por:
+ Andrés Felipe Martínez Veloza
+ Leymar Erney Buenaventura Asprilla

## Características
- Sistema de autenticación de usuarios
- Gestión de encuestas
  - Crear nuevas encuestas
  - Editar encuestas existentes
  - Banco de preguntas predefinidas
  - Personalización de preguntas
- Gestión de participantes
  - Registro de participantes
  - Visualización de lista de participantes
- Interfaz gráfica intuitiva

## Requisitos
- Python 3.x
- Librerías listadas en el requirements.txt

## Instalación

1. Clonar el repositorio:
git clone https://github.com/usuario/sistema_encuestas.git

2. Instalar dependencias:
pip install -r requirements.txt

## Uso

Ejecutar el programa principal:
python app/main.py


## Estructura del Proyecto
app/ ├── main.py ├── ventana_login.py ├── ventana_principal.py ├── ventana_edicion.py ├── ventana_gestionar_encuestas.py ├── ventana_gestionar_participantes.py ├── dialogo_nuevo_participante.py ├── banco_preguntas.py ├── encuesta.py └── gestion_usuarios.py

- `/app`: Código fuente de la aplicación
- `/docs`: Documentación y diagramas
- `requirements.txt`: Dependencias del proyecto
