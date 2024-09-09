class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo_autor = (titulo, autor)  # Tupla inmutable para título y autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"Título: {self.titulo_autor[0]}, Autor: {self.titulo_autor[1]}, Categoría: {self.categoria}, ISBN: {self.isbn}"

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista para almacenar los libros prestados

    def __str__(self):
        return f"Nombre: {self.nombre}, ID: {self.id_usuario}"

class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario para almacenar libros por ISBN
        self.usuarios = set()  # Conjunto para almacenar IDs de usuarios únicos

    def agregar_libro(self, libro):
        self.libros[libro.isbn] = libro

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
        else:
            print("Libro no encontrado.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios:
            self.usuarios.add(usuario.id_usuario)
            print(f"Usuario {usuario.nombre} registrado exitosamente.")
        else:
            print("El ID de usuario ya existe.")

    def prestar_libro(self, usuario, isbn):
        if isbn in self.libros:
            libro = self.libros.pop(isbn)
            usuario.libros_prestados.append(libro)
            print(f"Libro '{libro.titulo_autor[0]}' prestado exitosamente.")
        else:
            print("Libro no encontrado.")

    def buscar_libro(self, termino_busqueda):
        resultados = []
        for libro in self.libros.values():
            if termino_busqueda.lower() in libro.titulo_autor[0].lower() or \
               termino_busqueda.lower() in libro.titulo_autor[1].lower() or \
               termino_busqueda.lower() in libro.categoria.lower():
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, usuario):
        for libro in usuario.libros_prestados:
            print(libro)

# Ejemplo de uso
biblioteca = Biblioteca()

# Crear libros y usuarios
libro1 = Libro("El Quijote", "Miguel de Cervantes", "Literatura", "12345")
usuario1 = Usuario("Pablo Mendienta", 1)

# Agregar libro y registrar usuario
biblioteca.agregar_libro(libro1)
biblioteca.registrar_usuario(usuario1)

# Prestar libro
biblioteca.prestar_libro(usuario1, "12345")

# Buscar libros
resultados = biblioteca.buscar_libro("Cervantes")
for libro in resultados:
    print(libro)

# Listar libros prestados por un usuario
biblioteca.listar_libros_prestados(usuario1)