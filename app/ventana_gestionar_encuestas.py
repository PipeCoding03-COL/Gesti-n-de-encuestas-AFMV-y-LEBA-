import tkinter as tk
from tkinter import ttk, messagebox
import encuesta
from encuesta import Encuesta
from datetime import datetime
import csv
from tkinter import filedialog

class VentanaGestionarEncuestas(tk.Toplevel):
    encuestas = []  # Lista estática para almacenar encuestas

    @classmethod
    def agregar_encuesta(cls, encuesta):
        cls.encuestas.append(encuesta)

    def __init__(self, parent):
        super().__init__(parent)
        self.title("Gestión de Encuestas")
        self.geometry("1000x600")
        
        # Hacer la ventana modal
        self.transient(parent)
        self.grab_set()
        
        self.crear_widgets()
        self.cargar_encuestas()

    def crear_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Botones de acción
        frame_botones = ttk.Frame(main_frame)
        frame_botones.grid(row=0, column=0, columnspan=2, pady=10)

        ttk.Button(frame_botones, text="Nueva Encuesta", 
                  command=self.nueva_encuesta).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_botones, text="Publicar", 
                  command=self.publicar_encuesta).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_botones, text="Cerrar Encuesta", 
                  command=self.cerrar_encuesta).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_botones, text="Eliminar", 
                  command=self.eliminar_encuesta).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_botones, text="Ver Resultados", 
                  command=self.ver_resultados).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_botones, text="Cargar CSV", 
          command=self.cargar_desde_csv).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_botones, text="Editar", 
          command=self.editar_encuesta).pack(side=tk.LEFT, padx=5)

        # Tabla de encuestas
        columns = ("titulo", "estado", "fecha_creacion", "participantes", "respuestas")
        self.tabla = ttk.Treeview(main_frame, columns=columns, show='headings')
        
        # Configurar columnas
        self.tabla.heading("titulo", text="Título")
        self.tabla.heading("estado", text="Estado")
        self.tabla.heading("fecha_creacion", text="Fecha Creación")
        self.tabla.heading("participantes", text="Participantes")
        self.tabla.heading("respuestas", text="Respuestas")
        
        self.tabla.column("titulo", width=300)
        self.tabla.column("estado", width=100)
        self.tabla.column("fecha_creacion", width=150)
        self.tabla.column("participantes", width=100)
        self.tabla.column("respuestas", width=100)

        # Scrollbar
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scrollbar.set)

        # Grid
        self.tabla.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=1, column=1, sticky=(tk.N, tk.S))

        # Filtros
        frame_filtros = ttk.LabelFrame(main_frame, text="Filtros", padding="5")
        frame_filtros.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)

        ttk.Label(frame_filtros, text="Estado:").grid(row=0, column=0, padx=5)
        self.estado_var = tk.StringVar()
        ttk.Combobox(frame_filtros, textvariable=self.estado_var,
                    values=["Todas", "Borrador", "Publicada", "Cerrada"]).grid(row=0, column=1, padx=5)

        ttk.Button(frame_filtros, text="Aplicar Filtros", 
                  command=self.aplicar_filtros).grid(row=0, column=2, padx=5)

    def editar_encuesta(self):
        from ventana_edicion import VentanaEdicion
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Por favor seleccione una encuesta")
            return
            
        indice = self.tabla.index(seleccion[0])
        encuesta = self.encuestas[indice]
        VentanaEdicion(self, encuesta, indice)  # Pasamos el índice
    
    # Actualizar la encuesta en vez de crear una nueva
    def actualizar_encuesta(self):
        import ventana_edicion
        
        if ventana_edicion.validar_datos():
            encuesta.titulo = ventana_edicion.titulo_var.get()
            encuesta.descripcion = ventana_edicion.descripcion_text.get("1.0", tk.END).strip()
            encuesta.preguntas = []
            
            for pregunta in ventana_edicion.preguntas_seleccionadas:
                encuesta.agregar_pregunta(pregunta['texto'], pregunta['tipo'])
            
            self.cargar_encuestas()
            messagebox.showinfo("Éxito", "Encuesta actualizada correctamente")
            ventana_edicion.destroy()

    def nueva_encuesta(self):
        from ventana_encuesta import VentanaEncuesta
        VentanaEncuesta(self)
        self.cargar_encuestas()

    def publicar_encuesta(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Por favor seleccione una encuesta")
            return
            
        item = self.tabla.item(seleccion[0])
        if item['values'][1] != "Borrador":
            messagebox.showwarning("Advertencia", "Solo se pueden publicar encuestas en borrador")
            return
            
        if messagebox.askyesno("Confirmar", "¿Desea publicar la encuesta seleccionada?"):
            indice = self.tabla.index(seleccion[0])
            self.encuestas[indice].estado = "Publicada"
            self.encuestas[indice].fecha_publicacion = datetime.now()
            self.cargar_encuestas()
            messagebox.showinfo("Éxito", "Encuesta publicada correctamente")

    def cerrar_encuesta(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Por favor seleccione una encuesta")
            return
            
        item = self.tabla.item(seleccion[0])
        if item['values'][1] != "Publicada":
            messagebox.showwarning("Advertencia", "Solo se pueden cerrar encuestas publicadas")
            return
            
        if messagebox.askyesno("Confirmar", "¿Desea cerrar la encuesta seleccionada?"):
            indice = self.tabla.index(seleccion[0])
            self.encuestas[indice].estado = "Cerrada"
            self.encuestas[indice].fecha_cierre = datetime.now()
            self.cargar_encuestas()
            messagebox.showinfo("Éxito", "Encuesta cerrada correctamente")

    def eliminar_encuesta(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Por favor seleccione una encuesta")
            return
            
        if messagebox.askyesno("Confirmar", "¿Desea eliminar la encuesta seleccionada?"):
            indice = self.tabla.index(seleccion[0])
            self.encuestas.pop(indice)
            self.cargar_encuestas()
            messagebox.showinfo("Éxito", "Encuesta eliminada correctamente")

    def ver_resultados(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Por favor seleccione una encuesta")
            return
            
        item = self.tabla.item(seleccion[0])
        if item['values'][1] == "Borrador":
            messagebox.showwarning("Advertencia", "No hay resultados para encuestas en borrador")
            return
            
        indice = self.tabla.index(seleccion[0])
        encuesta = self.encuestas[indice]
        self.mostrar_resultados(encuesta)

    def mostrar_resultados(self, encuesta):
        ventana_resultados = tk.Toplevel(self)
        ventana_resultados.title(f"Resultados: {encuesta.titulo}")
        ventana_resultados.geometry("600x400")
        
        # Aquí agregarías la lógica para mostrar los resultados
        ttk.Label(ventana_resultados, 
                 text=f"Mostrando resultados de: {encuesta.titulo}\n"
                      f"Total participantes: {len(encuesta.participantes)}\n"
                      f"Total respuestas: {len(encuesta.respuestas)}").pack(pady=20)

    def cargar_encuestas(self):
        # Limpiar tabla
        for item in self.tabla.get_children():
            self.tabla.delete(item)
            
        # Cargar encuestas reales
        for encuesta in self.encuestas:
            self.tabla.insert("", tk.END, values=(
                encuesta.titulo,
                encuesta.estado,
                encuesta.fecha_creacion.strftime("%Y-%m-%d"),
                len(encuesta.participantes),
                len(encuesta.respuestas)
            ))

    def aplicar_filtros(self):
        estado = self.estado_var.get()
        for item in self.tabla.get_children():
            valores = self.tabla.item(item)['values']
            if estado == "Todas" or valores[1] == estado:
                self.tabla.reattach(item, "", tk.END)
            else:
                self.tabla.detach(item)
    
    def cargar_desde_csv(self):
        filename = filedialog.askopenfilename(
            title="Seleccionar archivo CSV",
            filetypes=(("CSV files", "*.csv"), ("All files", "*.*"))
        )
        if filename:
            with open(filename, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    nueva_encuesta = Encuesta(
                        titulo=row['titulo'],
                        descripcion=row['descripcion'],
                        creador=row['creador']
                    )
                    # Convertir string de preguntas a lista
                    preguntas = row['preguntas'].split('|')
                    for pregunta in preguntas:
                        nueva_encuesta.agregar_pregunta(pregunta, "multiple")
                    
                    nueva_encuesta.estado = row['estado']
                    VentanaGestionarEncuestas.agregar_encuesta(nueva_encuesta)
                self.cargar_encuestas()
