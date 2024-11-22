import tkinter as tk
from tkinter import ttk, messagebox
from banco_preguntas import BancoPreguntas

class VentanaPersonalizarPregunta(tk.Toplevel):
    def __init__(self, parent, pregunta):
        super().__init__(parent)
        self.title("Personalizar Pregunta")
        self.geometry("600x400")
        
        # Hacer la ventana modal
        self.transient(parent)
        self.grab_set()
        
        self.pregunta = pregunta
        self.resultado = None
        self.crear_widgets()
        
        # Centrar la ventana
        self.center_window()

    def center_window(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')

    def crear_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Texto de la pregunta
        ttk.Label(main_frame, text="Texto de la pregunta:").pack(pady=5)
        self.texto_pregunta = ttk.Entry(main_frame, width=50)
        self.texto_pregunta.insert(0, self.pregunta['texto'])
        self.texto_pregunta.pack(pady=5)

        # Tipo de pregunta
        ttk.Label(main_frame, text="Tipo de pregunta:").pack(pady=5)
        self.tipo_var = tk.StringVar(value='multiple')  # Forzamos un valor inicial
        self.combo_tipo = ttk.Combobox(main_frame, 
                                    textvariable=self.tipo_var,
                                    values=list(BancoPreguntas().tipos_pregunta.keys()),
                                    state="readonly")
        # Set initial value to match the question's type or first available option
        initial_type = self.pregunta.get('tipo') or 'multiple'
        self.combo_tipo.set(initial_type)
        self.combo_tipo.pack(pady=5)
        
        # Agregar una función trace al StringVar
        self.tipo_var.trace('w', lambda *args: self.actualizar_opciones())
        # Y mantener también el binding del combobox
        self.combo_tipo.bind('<<ComboboxSelected>>', self.actualizar_opciones)

        # Frame para opciones
        self.frame_opciones = ttk.LabelFrame(main_frame, 
                                            text="Opciones de respuesta",
                                            padding="10")
        self.frame_opciones.pack(pady=10, fill="x")
        
        # Inicializar las opciones
        self.opciones_entries = []
        self.actualizar_opciones()

        # Add at the end of crear_widgets():
        # Frame para botones
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=10)
        
        ttk.Button(button_frame, text="Guardar", command=self.guardar).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Cancelar", command=self.cancelar).pack(side="left", padx=5)


    def actualizar_opciones(self, event=None):
        # Obtener el tipo seleccionado directamente del combobox
        tipo_seleccionado = self.combo_tipo.get()  # Cambiamos self.tipo_var.get() por self.combo_tipo.get()
        print("Tipo seleccionado:", tipo_seleccionado)
    
        # Limpiar todas las opciones existentes
        for widget in self.frame_opciones.winfo_children():
            widget.destroy()
        self.opciones_entries.clear()

        banco = BancoPreguntas()
        print("Opciones actuales:", banco.tipos_pregunta[tipo_seleccionado]['opciones'])
    
        # Resto del código usando tipo_seleccionado...

        # Validar que haya un tipo seleccionado y que exista en el banco
        if not tipo_seleccionado or tipo_seleccionado not in banco.tipos_pregunta:
            return

        # Si es pregunta abierta
        if tipo_seleccionado == 'abierta':
            ttk.Label(self.frame_opciones, 
                    text="Esta pregunta permite texto libre como respuesta"
                    ).pack(pady=10)
            return

        # Crear frame para las opciones
        self.opciones_frame = ttk.Frame(self.frame_opciones)
        self.opciones_frame.pack(fill="x", expand=True)

        # Obtener las opciones del banco
        opciones = banco.tipos_pregunta[tipo_seleccionado]['opciones']

        # Crear los campos con las opciones
        for i, opcion in enumerate(opciones):
            frame = ttk.Frame(self.opciones_frame)
            frame.pack(fill="x", pady=2)

            ttk.Label(frame, text=f"Opción {i+1}:").pack(side="left")
            entry = ttk.Entry(frame, width=40)
            entry.insert(0, opcion)

            # Configurar readonly para tipos específicos
            if tipo_seleccionado in ['si_no', 'escala_5', 'escala_10']:
                entry.config(state='readonly')
    
            entry.pack(side="left", padx=5)
            self.opciones_entries.append(entry)

        # Botón de agregar solo para tipos que lo permiten
        if tipo_seleccionado not in ['si_no', 'escala_5', 'escala_10', 'abierta']:
            self.boton_agregar = ttk.Button(self.frame_opciones,
                                        text="+ Agregar Opción",
                                        command=self.agregar_opcion)
            self.boton_agregar.pack(pady=5)    
            
    def eliminar_opcion(self, frame, entry):
        self.opciones_entries.remove(entry)
        frame.destroy()

    def agregar_opcion(self):
        frame = ttk.Frame(self.opciones_frame)
        frame.pack(fill="x", pady=2)
        
        ttk.Label(frame, text=f"Opción {len(self.opciones_entries)+1}:").pack(side="left")
        entry = ttk.Entry(frame, width=40)
        entry.pack(side="left", padx=5)
        
        ttk.Button(frame, 
                  text="X", 
                  width=2,
                  command=lambda: self.eliminar_opcion(frame, entry)
                  ).pack(side="right")
        
        self.opciones_entries.append(entry)

    def restaurar_defaults(self):
        tipo_seleccionado = self.tipo_var.get()
        self.pregunta['opciones_personalizadas'] = None
        self.actualizar_opciones()

    def validar_datos(self):
        if not self.texto_pregunta.get().strip():
            messagebox.showerror("Error", "El texto de la pregunta no puede estar vacío")
            return False
        
        for entry in self.opciones_entries:
            if not entry.get().strip():
                messagebox.showerror("Error", "Las opciones no pueden estar vacías")
                return False
        return True

    def guardar(self):
        if not self.validar_datos():
            return
            
        opciones_personalizadas = [entry.get().strip() 
                                 for entry in self.opciones_entries]
        self.pregunta.update({
            'texto': self.texto_pregunta.get().strip(),
            'tipo': self.tipo_var.get(),
            'opciones_personalizadas': opciones_personalizadas
        })
        self.resultado = self.pregunta
        self.destroy()

    def cancelar(self):
        self.resultado = None
        self.destroy()
