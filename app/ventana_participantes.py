import csv
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from gestor_datos import GestorDatos

class VentanaParticipantes(tk.Toplevel):
    """Ventana para gestionar participantes"""
    
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Gestión de Participantes")
        self.geometry("800x600")
        self.participantes = []
        self.crear_widgets()
        
    def crear_widgets(self):
        """Crea los widgets de la ventana"""
        # Frame principal
        self.frame = ttk.Frame(self, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Botones de acción
        frame_botones = ttk.Frame(self.frame)
        frame_botones.grid(row=0, column=0, columnspan=2, pady=10)
        
        ttk.Button(frame_botones, text="Importar CSV", 
                  command=self.importar_csv).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_botones, text="Agregar Participante", 
                  command=self.agregar_participante).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_botones, text="Eliminar Seleccionados", 
                  command=self.eliminar_seleccionados).pack(side=tk.LEFT, padx=5)
        
        # Tabla de participantes
        self.crear_tabla()
        
        # Filtros
        frame_filtros = ttk.LabelFrame(self.frame, text="Filtros", padding="5")
        frame_filtros.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        ttk.Label(frame_filtros, text="Edad:").grid(row=0, column=0, padx=5)
        self.edad_var = tk.StringVar()
        ttk.Entry(frame_filtros, textvariable=self.edad_var).grid(row=0, column=1, padx=5)
        
        ttk.Label(frame_filtros, text="Género:").grid(row=0, column=2, padx=5)
        self.genero_var = tk.StringVar()
        ttk.Combobox(frame_filtros, textvariable=self.genero_var,
                    values=["", "Masculino", "Femenino", "Otro"]).grid(row=0, column=3, padx=5)
        
        ttk.Button(frame_filtros, text="Aplicar Filtros", 
                  command=self.aplicar_filtros).grid(row=0, column=4, padx=5)
        
    def crear_tabla(self):
        """Crea la tabla de participantes"""
        # Frame para la tabla
        frame_tabla = ttk.Frame(self.frame)
        frame_tabla.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Crear Treeview
        columnas = ("nombre", "email", "edad", "genero")
        self.tabla = ttk.Treeview(frame_tabla, columns=columnas, show='headings')
        
        # Configurar encabezados
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("email", text="Email")
        self.tabla.heading("edad", text="Edad")
        self.tabla.heading("genero", text="Género")
        
        # Configurar columnas
        self.tabla.column("nombre", width=200)
        self.tabla.column("email", width=200)
        self.tabla.column("edad", width=100)
        self.tabla.column("genero", width=100)
        
        # Scrollbars
        scroll_y = ttk.Scrollbar(frame_tabla, orient=tk.VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scroll_y.set)
        
        # Ubicar elementos
        self.tabla.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scroll_y.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
    def importar_csv(self):
        """Importa participantes desde un archivo CSV"""
        archivo = filedialog.askopenfilename(
            filetypes=[("Archivos CSV", "*.csv")]
        )
        if archivo:
            datos = GestorDatos.importar_csv(archivo)
            self.cargar_participantes(datos)
            messagebox.showinfo("Éxito", "Participantes importados correctamente")
            
    def cargar_participantes(self, datos):
        """Carga los participantes en la tabla"""
        # Limpiar tabla actual
        for item in self.tabla.get_children():
            self.tabla.delete(item)
            
        # Insertar nuevos datos
        for participante in datos:
            self.tabla.insert("", tk.END, values=(
                participante.get("nombre", ""),
                participante.get("email", ""),
                participante.get("edad", ""),
                participante.get("genero", "")
            ))
            
    def agregar_participante(self):
        """Abre diálogo para agregar nuevo participante"""
        dialogo = DialogoNuevoParticipante(self)
        self.wait_window(dialogo)
        if dialogo.participante:
            self.tabla.insert("", tk.END, values=dialogo.participante)
            
    def eliminar_seleccionados(self):
        """Elimina los participantes seleccionados"""
        seleccionados = self.tabla.selection()
        if seleccionados:
            if messagebox.askyesno("Confirmar", "¿Desea eliminar los participantes seleccionados?"):
                for item in seleccionados:
                    self.tabla.delete(item)
                    
    def aplicar_filtros(self):
        """Aplica los filtros seleccionados a la tabla"""
        edad_filtro = self.edad_var.get()
        genero_filtro = self.genero_var.get()
        
        # Mostrar todos los items
        for item in self.tabla.get_children():
            self.tabla.detach(item)
            
        # Aplicar filtros
        for item in self.tabla.get_children(""):
            valores = self.tabla.item(item)['values']
            mostrar = True
            
            if edad_filtro and str(valores[2]) != edad_filtro:
                mostrar = False
            if genero_filtro and valores[3] != genero_filtro:
                mostrar = False
                
            if mostrar:
                self.tabla.reattach(item, "", tk.END)

class DialogoNuevoParticipante(tk.Toplevel):
    """Diálogo para agregar un nuevo participante"""
    
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Nuevo Participante")
        self.geometry("400x300")
        self.resizable(False, False)
        self.participante = None
        
        # Hacer modal
        self.transient(parent)
        self.grab_set()
        
        self.crear_widgets()
        self.center_window()
        
    def crear_widgets(self):
        """Crea los widgets del diálogo"""
        frame = ttk.Frame(self, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Campos de entrada
        ttk.Label(frame, text="Nombre:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.nombre_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.nombre_var, width=30).grid(row=0, column=1, pady=5)
        
        ttk.Label(frame, text="Email:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.email_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.email_var, width=30).grid(row=1, column=1, pady=5)
        
        ttk.Label(frame, text="Edad:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.edad_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.edad_var, width=30).grid(row=2, column=1, pady=5)
        
        ttk.Label(frame, text="Género:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.genero_var = tk.StringVar()
        ttk.Combobox(frame, textvariable=self.genero_var, 
                    values=["Masculino", "Femenino", "Otro"], 
                    width=27).grid(row=3, column=1, pady=5)
        
        # Botones
        frame_botones = ttk.Frame(frame)
        frame_botones.grid(row=4, column=0, columnspan=2, pady=20)
        
        ttk.Button(frame_botones, text="Guardar", 
                  command=self.guardar).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_botones, text="Cancelar", 
                  command=self.destroy).pack(side=tk.LEFT, padx=5)
        
    def guardar(self):
        """Guarda los datos del nuevo participante"""
        if self.validar_datos():
            self.participante = (
                self.nombre_var.get(),
                self.email_var.get(),
                self.edad_var.get(),
                self.genero_var.get()
            )
            self.destroy()
            
    def validar_datos(self):
        """Valida los datos ingresados"""
        if not self.nombre_var.get() or not self.email_var.get():
            messagebox.showerror("Error", "Nombre y email son obligatorios")
            return False
        try:
            if self.edad_var.get():
                edad = int(self.edad_var.get())
                if edad < 0 or edad > 120:
                    raise ValueError
        except ValueError:
            messagebox.showerror("Error", "La edad debe ser un número válido")
            return False
        return True
        
    def center_window(self):
        """Centra la ventana en la pantalla"""
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')
