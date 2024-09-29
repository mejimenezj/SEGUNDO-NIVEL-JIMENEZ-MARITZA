import tkinter as tk
from tkinter import messagebox


class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        # Campo de entrada para nuevas tareas
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.grid(row=0, column=0, padx=15, pady=15)
        self.task_entry.bind("<Return>", self.add_task)  # Agregar tarea con la tecla Enter

        # Botones
        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=12, pady=12)

        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.grid(row=1, column=1, padx=10, pady=10)

        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=10, pady=10)

        # Lista de tareas
        self.task_listbox = tk.Listbox(root, height=10, width=40, selectmode=tk.SINGLE)
        self.task_listbox.grid(row=1, column=0, rowspan=2, padx=10, pady=10)
        self.task_listbox.bind("<Double-1>", self.complete_task)  # Doble clic para marcar tarea como completada

    def add_task(self, event=None):
        task = self.task_entry.get()
        if task != "":
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía")

    def complete_task(self, event=None):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task_text = self.task_listbox.get(selected_task_index)
            if not task_text.startswith("[Completada] "):
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(selected_task_index, "[Completada] " + task_text)
            else:
                messagebox.showinfo("Información", "La tarea ya está completada")
        except IndexError:
            messagebox.showwarning("Advertencia", "No se ha seleccionado ninguna tarea")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Advertencia", "No se ha seleccionado ninguna tarea")


# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()