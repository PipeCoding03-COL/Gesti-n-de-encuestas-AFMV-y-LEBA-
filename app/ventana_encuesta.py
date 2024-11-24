import tkinter as tk
from tkinter import ttk, messagebox
from ventana_personalizar_pregunta import VentanaPersonalizarPregunta
from encuesta import Encuesta
from banco_preguntas import BancoPreguntas
from ventana_gestionar_encuestas import VentanaGestionarEncuestas

class VentanaEncuesta(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Nueva Encuesta")
        self.geometry("800x600")        
        self.banco_preguntas = BancoPreguntas()
        self.preguntas_seleccionadas = []
        
        # Inicializa la variable con StringVar()
        self.titulo_var = tk.StringVar(self)  # Añadimos 'self' como master
        self.categoria_var = tk.StringVar()
        
        self.crear_widgets()

    def crear_widgets(self):
        # Frame principal con dos columnas
        main_frame = ttk.Frame(self, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Columna izquierda - Información básica y banco de preguntas
        left_frame = ttk.Frame(main_frame)
        left_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5)

        # Información básica
        info_frame = ttk.LabelFrame(left_frame, text="Información de la Encuesta", padding="5")
        info_frame.pack(fill="x", pady=5)

        ttk.Label(info_frame, text="Título:").grid(row=0, column=0, sticky=tk.W)
        # Modifica el Entry para asegurar la conexión
        titulo_entry = ttk.Entry(info_frame, textvariable=self.titulo_var, width=50)
        titulo_entry.grid(row=0, column=1, pady=5)
        ttk.Label(info_frame, text="Descripción:").grid(row=1, column=0, sticky=tk.W)
        self.descripcion_text = tk.Text(info_frame, width=50, height=3)
        self.descripcion_text.grid(row=1, column=1, pady=5)

        # Banco de preguntas
        banco_frame = ttk.LabelFrame(left_frame, text="Banco de Preguntas", padding="5")
        banco_frame.pack(fill="both", expand=True, pady=5)

        # Filtros
        filtros_frame = ttk.Frame(banco_frame)
        filtros_frame.pack(fill="x", pady=5)

        ttk.Label(filtros_frame, text="Categoría:").pack(side=tk.LEFT)
        self.combo_categoria = ttk.Combobox(filtros_frame, 
                                          textvariable=self.categoria_var,
                                          values=self.banco_preguntas.obtener_categorias(),
                                          state="readonly")  # Añadimos state="readonly"
        self.combo_categoria.pack(side=tk.LEFT, padx=5)
        self.combo_categoria.bind('<<ComboboxSelected>>', lambda event: self.actualizar_preguntas())

        ttk.Label(filtros_frame, text="Tipo:").pack(side=tk.LEFT, padx=5)
        self.tipo_var = tk.StringVar()
        self.combo_tipo = ttk.Combobox(filtros_frame, 
                                     textvariable=self.tipo_var,
                                     values=list(self.banco_preguntas.tipos_pregunta.keys()),
                                     state="readonly")  # Añadimos state="readonly"
        self.combo_tipo.pack(side=tk.LEFT)
        self.combo_tipo.bind('<<ComboboxSelected>>', lambda event: self.actualizar_preguntas())

        # Lista de preguntas disponibles
        self.lista_preguntas = ttk.Treeview(banco_frame, columns=("texto", "tipo"), show="headings")
        self.lista_preguntas.heading("texto", text="Pregunta")
        self.lista_preguntas.heading("tipo", text="Tipo")
        self.lista_preguntas.pack(fill="both", expand=True, pady=5)

        ttk.Button(banco_frame, text="Agregar Pregunta", 
                  command=self.agregar_pregunta).pack(pady=5)

        # Columna derecha - Preguntas seleccionadas
        right_frame = ttk.LabelFrame(main_frame, text="Preguntas Seleccionadas", padding="5")
        right_frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5)

        # Lista de preguntas seleccionadas
        self.lista_seleccionadas = ttk.Treeview(right_frame, 
                                               columns=("texto", "tipo", "opciones"),
                                               show="headings")
        self.lista_seleccionadas.heading("texto", text="Pregunta")
        self.lista_seleccionadas.heading("tipo", text="Tipo")
        self.lista_seleccionadas.heading("opciones", text="Opciones")
        self.lista_seleccionadas.pack(fill="both", expand=True, pady=5)

        # Botones de acción para preguntas seleccionadas
        botones_frame = ttk.Frame(right_frame)
        botones_frame.pack(fill="x", pady=5)

        ttk.Button(botones_frame, text="Personalizar", 
                  command=self.personalizar_pregunta).pack(side=tk.LEFT, padx=5)
        ttk.Button(botones_frame, text="Eliminar", 
                  command=self.eliminar_pregunta).pack(side=tk.LEFT)

        # Botones principales
        botones_main = ttk.Frame(main_frame)
        botones_main.grid(row=1, column=0, columnspan=2, pady=10)

        ttk.Button(botones_main, text="Guardar Encuesta", 
                  command=self.guardar_encuesta).pack(side=tk.LEFT, padx=5)
        ttk.Button(botones_main, text="Cancelar", 
                  command=self.destroy).pack(side=tk.LEFT)
        
        # Añadir esta línea al final del método
        self.actualizar_preguntas()
        
    def actualizar_preguntas(self, event=None):
        # Limpiamos la lista actual
        self.lista_preguntas.delete(*self.lista_preguntas.get_children())
        
        # Obtenemos los valores seleccionados
        categoria = self.combo_categoria.get()  # Cambiamos a usar get() directamente del combo
        tipo_filtro = self.combo_tipo.get()    # Cambiamos a usar get() directamente del combo
        
        # Obtenemos las preguntas de la categoría seleccionada
        if categoria:
            preguntas = self.banco_preguntas.obtener_categoria(categoria)
            for pregunta in preguntas:
                if not tipo_filtro or pregunta['tipo'] == tipo_filtro:
                    self.lista_preguntas.insert("", "end", 
                                              values=(pregunta['texto'], pregunta['tipo']))

        # Forzamos la actualización visual
        self.lista_preguntas.update()
    def agregar_pregunta(self):
        seleccion = self.lista_preguntas.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione una pregunta", parent=self)
            return
            
        item = self.lista_preguntas.item(seleccion[0])
        pregunta = {
            'texto': item['values'][0],
            'tipo': item['values'][1],
            'opciones': self.banco_preguntas.tipos_pregunta[item['values'][1]]['opciones']
        }
        
        self.preguntas_seleccionadas.append(pregunta)
        self.actualizar_lista_seleccionadas()

    def personalizar_pregunta(self):
        seleccion = self.lista_seleccionadas.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione una pregunta")
            return
            
        indice = self.lista_seleccionadas.index(seleccion[0])
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

    def guardar_encuesta(self):        
        titulo = self.titulo_var.get().strip()
        if not titulo:
            messagebox.showerror("Error", "El título es obligatorio")
            return
            
        if not self.preguntas_seleccionadas:
            messagebox.showerror("Error", "Debe seleccionar al menos una pregunta")
            return
            
        nueva_encuesta = Encuesta(
            titulo=titulo,
            descripcion=self.descripcion_text.get("1.0", tk.END).strip(),
            creador="usuario_actual"
        )
        
        for pregunta in self.preguntas_seleccionadas:
            nueva_encuesta.agregar_pregunta(pregunta['texto'], pregunta['tipo'])
            
        VentanaGestionarEncuestas.agregar_encuesta(nueva_encuesta)
        self.parent.cargar_encuestas()  # Add this line to refresh the surveys list
        self.destroy()
