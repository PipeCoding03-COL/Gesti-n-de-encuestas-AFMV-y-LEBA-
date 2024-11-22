import tkinter as tk
from tkinter import ttk, messagebox
from ventana_gestionar_encuestas import VentanaGestionarEncuestas
from banco_preguntas import BancoPreguntas
from encuesta import Encuesta

class VentanaEdicion(tk.Toplevel):
    def __init__(self, parent, encuesta, indice):
        super().__init__(parent)
        self.title(f"Editar Encuesta: {encuesta.titulo}")
        self.geometry("1000x700")
        
        self.encuesta = encuesta
        self.indice = indice  # Guardamos el índice
        self.banco_preguntas = BancoPreguntas()
        self.preguntas_seleccionadas = []
        
        # Inicializar variables
        self.titulo_var = tk.StringVar(value=encuesta.titulo)
        self.categoria_var = tk.StringVar()
        
        self.crear_widgets()
        self.cargar_datos_encuesta()
    
    def crear_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self, padding="10")
        main_frame.pack(fill="both", expand=True)

        # Frame superior para información básica
        info_frame = ttk.LabelFrame(main_frame, text="Información de la Encuesta", padding="5")
        info_frame.pack(fill="x", pady=5)

        ttk.Label(info_frame, text="Título:").grid(row=0, column=0, sticky="w")
        self.titulo_entry = ttk.Entry(info_frame, width=50)
        self.titulo_entry.insert(0, self.encuesta.titulo)  # Insert title directly
        self.titulo_entry.grid(row=0, column=1, pady=5)

        ttk.Label(info_frame, text="Descripción:").grid(row=1, column=0, sticky="w")
        self.descripcion_text = tk.Text(info_frame, width=50, height=3)
        self.descripcion_text.grid(row=1, column=1, pady=5)

        # Frame contenedor para las dos secciones principales
        contenedor_frame = ttk.Frame(main_frame)
        contenedor_frame.pack(fill="both", expand=True, pady=5)

        # Frame izquierdo - Banco de preguntas
        self.banco_frame = ttk.LabelFrame(contenedor_frame, text="Banco de Preguntas", padding="5")
        self.banco_frame.pack(side="left", fill="both", expand=True, padx=5)

        # Filtros en banco_frame
        filtros_frame = ttk.Frame(self.banco_frame)
        filtros_frame.pack(fill="x", pady=5)
        ttk.Label(filtros_frame, text="Categoría:").pack(side="left")
        self.combo_categoria = ttk.Combobox(filtros_frame, textvariable=self.categoria_var)
        self.combo_categoria.pack(side="left", padx=5)

        # Cargar categorías en el combobox
        categorias = list(self.banco_preguntas.preguntas.keys())
        self.combo_categoria['values'] = categorias
        self.combo_categoria.set(categorias[0])  # Selecciona la primera categoría por defecto
        self.combo_categoria.bind('<<ComboboxSelected>>', self.actualizar_preguntas)

        # Lista de preguntas disponibles
        self.lista_preguntas = ttk.Treeview(self.banco_frame, columns=("texto", "tipo"), show="headings", height=10)
        self.lista_preguntas.heading("texto", text="Pregunta")
        self.lista_preguntas.heading("tipo", text="Tipo")
        self.lista_preguntas.column("texto", width=400, minwidth=300)
        self.lista_preguntas.column("tipo", width=100, minwidth=80)
        
        scrolly = ttk.Scrollbar(self.banco_frame, orient="vertical", command=self.lista_preguntas.yview)
        scrollx = ttk.Scrollbar(self.banco_frame, orient="horizontal", command=self.lista_preguntas.xview)
        self.lista_preguntas.configure(yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        
        self.lista_preguntas.pack(fill="both", expand=True)
        scrolly.pack(side="right", fill="y")
        scrollx.pack(side="bottom", fill="x")

        ttk.Button(self.banco_frame, text="Agregar Pregunta", command=self.agregar_pregunta).pack(pady=5)

        # Frame derecho - Preguntas seleccionadas
        self.preguntas_frame = ttk.LabelFrame(contenedor_frame, text="Preguntas de la Encuesta", padding="5")
        self.preguntas_frame.pack(side="right", fill="both", expand=True, padx=5)

        self.lista_seleccionadas = ttk.Treeview(self.preguntas_frame, columns=("texto", "tipo"), show="headings", height=10)
        self.lista_seleccionadas.heading("texto", text="Pregunta")
        self.lista_seleccionadas.heading("tipo", text="Tipo")
        self.lista_seleccionadas.column("texto", width=400, minwidth=300)
        self.lista_seleccionadas.column("tipo", width=100, minwidth=80)
        
        scrolly2 = ttk.Scrollbar(self.preguntas_frame, orient="vertical", command=self.lista_seleccionadas.yview)
        scrollx2 = ttk.Scrollbar(self.preguntas_frame, orient="horizontal", command=self.lista_seleccionadas.xview)
        self.lista_seleccionadas.configure(yscrollcommand=scrolly2.set, xscrollcommand=scrollx2.set)
        
        self.lista_seleccionadas.pack(fill="both", expand=True)
        scrolly2.pack(side="right", fill="y")
        scrollx2.pack(side="bottom", fill="x")

        # Botones para preguntas seleccionadas
        botones_frame = ttk.Frame(self.preguntas_frame)
        botones_frame.pack(fill="x", pady=5)
        ttk.Button(botones_frame, text="Editar Pregunta", command=self.editar_pregunta).pack(side="left", padx=5)
        ttk.Button(botones_frame, text="Eliminar Pregunta", command=self.eliminar_pregunta).pack(side="left")

        # Botones principales
        botones_main = ttk.Frame(main_frame)
        botones_main.pack(fill="x", pady=10)
        ttk.Button(botones_main, text="Guardar Cambios", command=self.guardar_cambios).pack(side="left", padx=5)
        ttk.Button(botones_main, text="Cancelar", command=self.destroy).pack(side="left")

        # Cargar preguntas iniciales
        self.actualizar_preguntas()


    def cargar_datos_encuesta(self):
        # Cargar título y descripción
        self.titulo_var.set(self.encuesta.titulo)
        self.descripcion_text.delete("1.0", tk.END)
        self.descripcion_text.insert("1.0", self.encuesta.descripcion)
        
        # Cargar preguntas existentes
        self.preguntas_seleccionadas = []
        for pregunta in self.encuesta.preguntas:
            self.preguntas_seleccionadas.append({
                'texto': pregunta['texto'],
                'tipo': pregunta['tipo'],
                'opciones': pregunta.get('opciones', [])
            })
        self.actualizar_lista_seleccionadas()

    def actualizar_preguntas(self, event=None):
        # Limpia la lista actual
        self.lista_preguntas.delete(*self.lista_preguntas.get_children())
        
        # Obtiene la categoría seleccionada del combobox
        categoria = self.combo_categoria.get()
        
        # Obtiene las preguntas de esa categoría
        preguntas = self.banco_preguntas.obtener_preguntas(categoria)
        
        # Muestra cada pregunta en la lista
        for pregunta in preguntas:
            texto_pregunta = pregunta['texto']  # Extraemos solo el texto
            tipo_pregunta = pregunta['tipo']    # Extraemos solo el tipo
            self.lista_preguntas.insert("", "end", values=(texto_pregunta, tipo_pregunta))


    def agregar_pregunta(self):
        seleccion = self.lista_preguntas.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione una pregunta")
            return
            
        item = self.lista_preguntas.item(seleccion[0])
        pregunta = {
            'texto': item['values'][0],
            'tipo': item['values'][1],
            'opciones': self.banco_preguntas.tipos_pregunta[item['values'][1]]['opciones']
        }
        self.preguntas_seleccionadas.append(pregunta)
        self.actualizar_lista_seleccionadas()

    def editar_pregunta(self):
        seleccion = self.lista_seleccionadas.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione una pregunta")
            return
            
        indice = self.lista_seleccionadas.index(seleccion[0])
        from ventana_personalizar_pregunta import VentanaPersonalizarPregunta
        VentanaPersonalizarPregunta(self, self.preguntas_seleccionadas[indice])
        self.actualizar_lista_seleccionadas()

    def eliminar_pregunta(self):
        seleccion = self.lista_seleccionadas.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione una pregunta")
            return
            
        indice = self.lista_seleccionadas.index(seleccion[0])
        self.preguntas_seleccionadas.pop(indice)
        self.actualizar_lista_seleccionadas()

    def actualizar_lista_seleccionadas(self):
        self.lista_seleccionadas.delete(*self.lista_seleccionadas.get_children())
        for pregunta in self.preguntas_seleccionadas:
            opciones = pregunta.get('opciones_personalizadas', 
                                  self.banco_preguntas.tipos_pregunta[pregunta['tipo']]['opciones'])
            self.lista_seleccionadas.insert("", "end", 
                                          values=(pregunta['texto'], 
                                                 pregunta['tipo'], 
                                                 ", ".join(opciones)))

    def guardar_cambios(self):
        if not self.titulo_var.get().strip():
            messagebox.showerror("Error", "El título es obligatorio")
            return
            
        if not self.preguntas_seleccionadas:
            messagebox.showerror("Error", "Debe tener al menos una pregunta")
            return

        # Actualizar los datos de la encuesta existente
        self.encuesta.titulo = self.titulo_entry.get()
        self.encuesta.descripcion = self.descripcion_text.get("1.0", tk.END).strip()
        self.encuesta.preguntas = self.preguntas_seleccionadas

        # Actualizar en la lista de encuestas
        VentanaGestionarEncuestas.encuestas[self.indice] = self.encuesta
        
        # Actualizar vista
        self.master.cargar_encuestas()
        messagebox.showinfo("Éxito", "Encuesta actualizada correctamente")
        self.destroy()
