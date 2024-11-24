import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from dialogo_nuevo_participante import DialogoNuevoParticipante
from gestor_datos import GestorDatos

#Ventana para gestionar participantes
class VentanaParticipantes(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Gestión de Participantes")
        self.geometry("800x600")
        self.participantes = []
        self.crear_widgets()
    
    # Crea los widgets de la ventana
    def crear_widgets(self):
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
    
    # Crea la tabla de participantes
    def crear_tabla(self):
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
    
    # Importa participantes desde un archivo CSV
    def importar_csv(self):
        archivo = filedialog.askopenfilename(
            filetypes=[("Archivos CSV", "*.csv")]
        )
        if archivo:
            datos = GestorDatos.importar_csv(archivo)
            self.cargar_participantes(datos)
            messagebox.showinfo("Éxito", "Participantes importados correctamente")
    
    # Carga los participantes en la tabla
    def cargar_participantes(self, datos):
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
    
    # Abre diálogo para agregar nuevo participante
    def agregar_participante(self):
        dialogo = DialogoNuevoParticipante(self)
        self.wait_window(dialogo)
        if dialogo.participante:
            self.tabla.insert("", tk.END, values=dialogo.participante)
            
    # Elimina los participantes seleccionados
    def eliminar_seleccionados(self):
        seleccionados = self.tabla.selection()
        if seleccionados:
            if messagebox.askyesno("Confirmar", "¿Desea eliminar los participantes seleccionados?"):
                for item in seleccionados:
                    self.tabla.delete(item)
                    
    # Aplica los filtros seleccionados a la tabla
    def aplicar_filtros(self):
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

