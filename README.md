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

## Estructura del Proyecto
- `/app`: Código fuente de la aplicación
- `/docs`: Documentación y diagramas de clase UML
- `requirements.txt`: Dependencias del proyecto

## Instalación
1. Clonar el repositorio:
```bash
git clone https://github.com/yourusername/Gestion-de-encuestas-AFMV-y-LEBA-.git
```

2. Crear e inicializar el entorno virtual: 
```bash
python3 -m venv venv
source venv/bin/activate #Linux/MacOS
venv\scripts\activate #Windows
```

3. Instalar librerías:
```bash
pip install -r requirements.txt
```

## Ejecución
```bash
python app/Main.py #Linux/MacOS
python app\Main.py #Windows
```