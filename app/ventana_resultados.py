import tkinter as tk
from tkinter import ttk, messagebox

class VentanaResultados(tk.Toplevel):
    def __init__(self, parent, usuario):
        super().__init__(parent)
        self.title("Resultados de Encuestas")
        self.geometry("1000x600")
        self.usuario = usuario
        
        self.crear_widgets()
        
    def crear_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self, padding="10")
        main_frame.pack(fill="both", expand=True)
        
        # Lista de encuestas
        encuestas_frame = ttk.LabelFrame(main_frame, text="Encuestas Disponibles", padding="5")
        encuestas_frame.pack(side="left", fill="both", expand=True, padx=5)
        
        self.lista_encuestas = ttk.Treeview(encuestas_frame, columns=("titulo", "estado", "fecha"), show="headings")
        self.lista_encuestas.heading("titulo", text="Título")
        self.lista_encuestas.heading("estado", text="Estado")
        self.lista_encuestas.heading("fecha", text="Fecha")
        
        scrolly = ttk.Scrollbar(encuestas_frame, orient="vertical", command=self.lista_encuestas.yview)
        self.lista_encuestas.configure(yscrollcommand=scrolly.set)
        
        self.lista_encuestas.pack(side="left", fill="both", expand=True)
        scrolly.pack(side="right", fill="y")
        
        # Frame de resultados
        resultados_frame = ttk.LabelFrame(main_frame, text="Resultados", padding="5")
        resultados_frame.pack(side="right", fill="both", expand=True, padx=5)
        
        # Botones de análisis
        botones_frame = ttk.Frame(resultados_frame)
        botones_frame.pack(fill="x", pady=5)
        
        ttk.Button(botones_frame, text="Ver Estadísticas", command=self.ver_estadisticas).pack(side="left", padx=5)
        ttk.Button(botones_frame, text="Generar Informe", command=self.generar_informe).pack(side="left", padx=5)
        ttk.Button(botones_frame, text="Exportar Datos", command=self.exportar_datos).pack(side="left", padx=5)
        
        # Área de resultados
        self.resultado_text = tk.Text(resultados_frame, wrap="word", height=20)
        self.resultado_text.pack(fill="both", expand=True, pady=5)
        
        # Cargar datos
        self.cargar_encuestas()
        
    def cargar_encuestas(self):
        # Aquí cargarías las encuestas desde tu sistema de almacenamiento
        pass
        
    def ver_estadisticas(self):
        seleccion = self.lista_encuestas.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Por favor seleccione una encuesta")
            return
        # Implementar visualización de estadísticas
        
    def generar_informe(self):
        seleccion = self.lista_encuestas.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Por favor seleccione una encuesta")
            return
        # Implementar generación de informe
        
    def exportar_datos(self):
        seleccion = self.lista_encuestas.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Por favor seleccione una encuesta")
            return
        # Implementar exportación de datos
