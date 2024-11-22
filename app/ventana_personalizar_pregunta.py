import tkinter as tk
from tkinter import ttk
from banco_preguntas import BancoPreguntas

class VentanaPersonalizarPregunta(tk.Toplevel):
    def __init__(self, parent, pregunta):
        super().__init__(parent)
        self.title("Personalizar Pregunta")
        self.geometry("600x400")
        
        self.pregunta = pregunta
        self.crear_widgets()

    def crear_widgets(self):
        # Texto de la pregunta
        ttk.Label(self, text="Texto de la pregunta:").pack(pady=5)
        self.texto_pregunta = ttk.Entry(self, width=50)
        self.texto_pregunta.insert(0, self.pregunta['texto'])
        self.texto_pregunta.pack(pady=5)

        # Tipo de pregunta
        ttk.Label(self, text="Tipo de pregunta:").pack(pady=5)
        self.tipo_var = tk.StringVar(value=self.pregunta['tipo'])
        self.combo_tipo = ttk.Combobox(self, textvariable=self.tipo_var)
        self.combo_tipo['values'] = list(BancoPreguntas().tipos_pregunta.keys())
        self.combo_tipo.pack(pady=5)
        self.combo_tipo.bind('<<ComboboxSelected>>', self.actualizar_opciones)

        # Frame para opciones
        self.frame_opciones = ttk.LabelFrame(self, text="Opciones de respuesta", padding="10")
        self.frame_opciones.pack(pady=10, fill="x", padx=10)
        
        self.opciones_entries = []
        self.actualizar_opciones()

        # Botones
        ttk.Button(self, text="Guardar", command=self.guardar).pack(pady=10)
        ttk.Button(self, text="Cancelar", command=self.destroy).pack(pady=5)

    def actualizar_opciones(self, event=None):
        # Limpiar opciones anteriores
        for widget in self.frame_opciones.winfo_children():
            widget.destroy()
        self.opciones_entries.clear()

        tipo_seleccionado = self.tipo_var.get()
        opciones_default = BancoPreguntas().tipos_pregunta[tipo_seleccionado]['opciones']
        
        for i, opcion in enumerate(opciones_default):
            frame = ttk.Frame(self.frame_opciones)
            frame.pack(fill="x", pady=2)
            
            ttk.Label(frame, text=f"Opción {i+1}:").pack(side="left")
            entry = ttk.Entry(frame, width=40)
            entry.insert(0, opcion)
            entry.pack(side="left", padx=5)
            self.opciones_entries.append(entry)

    def guardar(self):
        opciones_personalizadas = [entry.get() for entry in self.opciones_entries]
        self.pregunta.update({
            'texto': self.texto_pregunta.get(),
            'tipo': self.tipo_var.get(),
            'opciones_personalizadas': opciones_personalizadas
        })
        self.destroy()
