import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re

class AgendaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MI AGENDA PERSONALIZADA")
        self.geometry("700x400")  # Tamaño de la ventana

        # Frame para la lista de eventos
        self.frame_eventos = ttk.Frame(self)
        self.frame_eventos.pack(fill="both", expand=True)

        # Treeview para mostrar los eventos
        self.tree = ttk.Treeview(self.frame_eventos, columns=("fecha", "hora", "descripcion"), show="headings")
        self.tree.heading("fecha", text="FECHA")
        self.tree.heading("hora", text="HORA")
        self.tree.heading("descripcion", text="DESCRIPCIÓN")
        self.tree.column("fecha", width=200)
        self.tree.column("hora", width=100)
        self.tree.column("descripcion", width=300)
        self.tree.pack(fill="both", expand=True)

        # Frame para los campos de entrada y botones
        self.frame_entrada = ttk.Frame(self)
        self.frame_entrada.pack(fill="x", pady=20)

        # Campos de entrada
        ttk.Label(self.frame_entrada, text="Fecha (dd/mm/aaaa):").grid(row=0, column=0, padx=5)
        self.entrada_fecha = ttk.Entry(self.frame_entrada)
        self.entrada_fecha.grid(row=0, column=1, padx=5)

        ttk.Label(self.frame_entrada, text="Hora (hh:mm):").grid(row=1, column=0, padx=5)
        self.entrada_hora = ttk.Entry(self.frame_entrada)
        self.entrada_hora.grid(row=1, column=1, padx=5)

        ttk.Label(self.frame_entrada, text="Descripción:").grid(row=2, column=0, padx=5)
        self.entrada_descripcion = ttk.Entry(self.frame_entrada, width=50)
        self.entrada_descripcion.grid(row=2, column=1, padx=5)

        # Botones
        self.boton_agregar = ttk.Button(self.frame_entrada, text="Agregar Evento")
        self.boton_agregar.grid(row=3, column=0, columnspan=2, pady=5)
        self.boton_eliminar = ttk.Button(self.frame_entrada, text="Eliminar Evento")
        self.boton_eliminar.grid(row=4, column=0, columnspan=2, pady=5)

        # Asignar comandos a los botones
        self.boton_agregar.config(command=self.agregar_evento)
        self.boton_eliminar.config(command=self.eliminar_evento)

    def validar_fecha(self, fecha):
        # Validar que la fecha esté en formato dd/mm/aaaa
        patron_fecha = r"\b(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}\b"
        return re.match(patron_fecha, fecha)

    def validar_hora(self, hora):
        # Validar que la hora esté en formato hh:mm (24 horas)
        patron_hora = r"\b([01][0-9]|2[0-3]):([0-5][0-9])\b"
        return re.match(patron_hora, hora)

    def agregar_evento(self):
        # Obtener datos de los campos de entrada
        fecha = self.entrada_fecha.get()
        hora = self.entrada_hora.get()
        descripcion = self.entrada_descripcion.get()

        # Verificar que los campos no estén vacíos
        if fecha and hora and descripcion:
            # Validar el formato de la fecha y hora
            if not self.validar_fecha(fecha):
                messagebox.showerror("Fecha incorrecta", "Ingrese una fecha válida en el formato dd/mm/aaaa.")
                return

            if not self.validar_hora(hora):
                messagebox.showerror("Hora incorrecta", "Ingrese una hora válida en el formato hh:mm.")
                return

            # Agregar un nuevo evento al Treeview
            self.tree.insert("", "end", values=(fecha, hora, descripcion))

            # Mostrar mensaje de confirmación
            messagebox.showinfo("Evento agregado", "El evento ha sido agregado correctamente.")

            # Limpiar campos de entrada
            self.entrada_fecha.delete(0, tk.END)
            self.entrada_hora.delete(0, tk.END)
            self.entrada_descripcion.delete(0, tk.END)
        else:
            messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos.")

    def eliminar_evento(self):
        # Obtener el evento seleccionado
        selected_item = self.tree.selection()

        if selected_item:
            # Mostrar un diálogo de confirmación
            confirm = messagebox.askyesno("Eliminar evento", "¿Está seguro de que desea eliminar este evento?")
            if confirm:
                # Eliminar el evento del Treeview
                self.tree.delete(selected_item)
        else:
            messagebox.showwarning("Seleccionar evento", "Por favor, seleccione un evento para eliminar.")


# Crear una instancia de la aplicación y ejecutarla
app = AgendaApp()
app.mainloop()