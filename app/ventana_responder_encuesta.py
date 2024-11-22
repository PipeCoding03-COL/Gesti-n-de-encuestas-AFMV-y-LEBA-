import tkinter as tk
from tkinter import ttk, messagebox

class VentanaResponderEncuesta(tk.Toplevel):
    def __init__(self, parent, encuesta):
        super().__init__(parent)
        self.title(f"Responder: {encuesta.titulo}")
        self.geometry("800x600")
        
        self.encuesta = encuesta
        self.respuestas = {}
        
        self.crear_widgets()

    def crear_widgets(self):
        main_frame = ttk.Frame(self, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Información de la encuesta
        ttk.Label(main_frame, text=self.encuesta.titulo, 
                 font=('Helvetica', 14, 'bold')).grid(row=0, column=0, pady=10)
        ttk.Label(main_frame, text=self.encuesta.descripcion).grid(row=1, column=0, pady=5)

        # Frame para preguntas
        preguntas_frame = ttk.Frame(main_frame)
        preguntas_frame.grid(row=2, column=0, pady=10)

        # Crear widgets para cada pregunta
        for i, pregunta in enumerate(self.encuesta.preguntas):
            frame_pregunta = ttk.LabelFrame(preguntas_frame, text=f"Pregunta {i+1}", padding="5")
            frame_pregunta.grid(row=i, column=0, pady=5, sticky=(tk.W, tk.E))

            ttk.Label(frame_pregunta, text=pregunta['pregunta']).grid(row=0, column=0, pady=5)
            
            if pregunta['tipo'] == 'multiple':
                var = tk.StringVar()
                self.respuestas[pregunta['id']] = var
                
                opciones = pregunta.get('opciones', ['1', '2', '3', '4', '5'])
                for j, opcion in enumerate(opciones):
                    ttk.Radiobutton(frame_pregunta, text=opcion, 
                                  variable=var, value=opcion).grid(row=j+1, column=0, pady=2)

        # Botones
        botones_frame = ttk.Frame(main_frame)
        botones_frame.grid(row=3, column=0, pady=20)

        ttk.Button(botones_frame, text="Enviar Respuestas", 
                  command=self.enviar_respuestas).pack(side=tk.LEFT, padx=5)
        ttk.Button(botones_frame, text="Cancelar", 
                  command=self.destroy).pack(side=tk.LEFT, padx=5)

    def enviar_respuestas(self):
        # Verificar que todas las preguntas estén respondidas
        for pregunta_id, var in self.respuestas.items():
            if not var.get():
                messagebox.showerror("Error", "Por favor responda todas las preguntas")
                return

        # Registrar respuestas
        for pregunta_id, var in self.respuestas.items():
            self.encuesta.registrar_respuesta("participante_actual", pregunta_id, var.get())

        messagebox.showinfo("Éxito", "Respuestas enviadas correctamente")
        self.destroy()
