import pandas as pd

# Clase para gestionar la importación y exportación de datos
class GestorDatos:
    # Importa participantes desde un archivo CSV
    @staticmethod
    def importar_csv(ruta_archivo):
        try:
            df = pd.read_csv(ruta_archivo)
            return df.to_dict('records')
        except Exception as e:
            print(f"Error al importar CSV: {e}")
            return []
    
    # Exporta los resultados de una encuesta a CSV
    @staticmethod
    def exportar_resultados(encuesta, ruta_archivo):
        try:
            # Implementar exportación
            pass
        except Exception as e:
            print(f"Error al exportar resultados: {e}")
