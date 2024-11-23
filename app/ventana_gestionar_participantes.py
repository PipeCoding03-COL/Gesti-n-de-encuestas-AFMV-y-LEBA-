import tkinter as tk
from tkinter import ttk
from app import participante
from dialogo_nuevo_participante import DialogoNuevoParticipante


class VentanaGestionarParticipantes(tk.Toplevel):
    participantes_lista = []
    
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Gestionar Participantes")
        self.geometry("800x600")
        # Global variable at module level
        PARTICIPANTES = []

        class VentanaGestionarParticipantes(tk.Toplevel):
            def __init__(self, parent):
                super().__init__(parent)
                self.title("Gestionar Participantes")
                self.geometry("800x600")
                print("Lista actual:", PARTICIPANTES)
                self.crear_widgets()
                self.actualizar_tabla()

            def crear_widgets(self):
                # Create table with correct columns
                self.tabla = ttk.Treeview(self, columns=("nombre", "email", "edad", "genero"), show="headings")
                self.tabla.heading("nombre", text="Nombre")
                self.tabla.heading("email", text="Email")
                self.tabla.heading("edad", text="Edad")
                self.tabla.heading("genero", text="Género")
                self.tabla.pack(fill="both", expand=True)

            def agregar_participante(self):
                dialogo = DialogoNuevoParticipante(self)
                self.wait_window(dialogo)
                if dialogo.participante:
                    PARTICIPANTES.append(dialogo.participante)
                    print("Participante agregado:", PARTICIPANTES)
                    self.actualizar_tabla()

            def actualizar_tabla(self):
                self.tabla.delete(*self.tabla.get_children())
                for participante in PARTICIPANTES:
                    self.tabla.insert("", "end", values=participante)
            self.tabla.insert("", "end", values=participante)