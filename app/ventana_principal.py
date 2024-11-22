import tkinter as tk
from tkinter import ttk
from ventana_encuesta import VentanaEncuesta
from ventana_participantes import VentanaParticipantes
from ventana_gestionar_encuestas import VentanaGestionarEncuestas

class VentanaPrincipal:
    """Ventana principal de la aplicación"""
    
    def __init__(self, root):
        self.root = root
        self.crear_menu()
        self.crear_widgets()
        
    def crear_menu(self):
        """Crea la barra de menú principal"""
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)
        
        # Menú Archivo
        archivo_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Archivo", menu=archivo_menu)
        archivo_menu.add_command(label="Nueva Encuesta", command=self.nueva_encuesta)
        archivo_menu.add_command(label="Salir", command=self.root.quit)
        
    def crear_widgets(self):
        """Crea los widgets principales"""
        # Frame principal
        self.frame_principal = ttk.Frame(self.root, padding="10")
        self.frame_principal.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Botones principales
        ttk.Button(self.frame_principal, text="Gestionar Encuestas", 
                  command=self.gestionar_encuestas).grid(row=0, column=0, pady=10)
        ttk.Button(self.frame_principal, text="Gestionar Participantes", 
                  command=self.gestionar_participantes).grid(row=1, column=0, pady=10)
        
    def nueva_encuesta(self):
        """Abre la ventana de nueva encuesta"""
        VentanaEncuesta(self.root)
        
    def gestionar_encuestas(self):
        """Abre la ventana de gestión de encuestas"""
        VentanaGestionarEncuestas(self.root)
        
    def gestionar_participantes(self):
        """Abre la ventana de gestión de participantes"""
        VentanaParticipantes(self.root)
