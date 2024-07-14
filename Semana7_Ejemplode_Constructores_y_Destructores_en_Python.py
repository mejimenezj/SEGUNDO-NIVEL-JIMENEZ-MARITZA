class FileHandler:
    def __init__(self, file_name, mode):
        """Constructor que inicializa y abre un archivo."""
        self.file_name = file_name
        self.mode = mode
        self.file = None
        try:
            self.file = open(self.file_name, self.mode)
            print(f"Archivo '{self.file_name}' abierto en modo '{self.mode}'.")
        except Exception as e:
            print(f"Error al abrir el archivo: {e}")

    def write_data(self, data):
        """Escribe datos en el archivo."""
        if self.file and not self.file.closed:
            self.file.write(data)
        else:
            print("El archivo no está abierto.")

    def read_data(self):
        """Lee datos del archivo."""
        if self.file and not self.file.closed:
            return self.file.read()
        else:
            print("El archivo no está abierto.")
            return None

    def __del__(self):
        """Destructor que cierra el archivo si está abierto."""
        if self.file and not self.file.closed:
            self.file.close()
            print(f"Archivo '{self.file_name}' cerrado.")

# Ejemplo de uso
file_handler = FileHandler('example.txt', 'w')
file_handler.write_data('Hola, mundo!')
del file_handler  # Esto llamará al destructor y cerrará el archivo