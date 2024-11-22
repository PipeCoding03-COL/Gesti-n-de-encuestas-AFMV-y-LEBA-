import pandas as pd

class GestorDatos:
    """Clase para gestionar la importación y exportación de datos"""
    
    @staticmethod
    def importar_csv(ruta_archivo):
        """Importa participantes desde un archivo CSV"""
        try:
            df = pd.read_csv(ruta_archivo)
            return df.to_dict('records')
        except Exception as e:
            print(f"Error al importar CSV: {e}")
            return []
            
    @staticmethod
    def exportar_resultados(encuesta, ruta_archivo):
        """Exporta los resultados de una encuesta a CSV"""
        try:
            # Implementar exportación
            pass
        except Exception as e:
            print(f"Error al exportar resultados: {e}")
