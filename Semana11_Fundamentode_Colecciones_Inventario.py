class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.get_id() in self.productos:
            print(f"Error: Ya existe un producto con ID {producto.get_id()}.")
        else:
            self.productos[producto.get_id()] = producto
            print("Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            print("Producto actualizado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        encontrados = [producto for producto in self.productos.values() if producto.get_nombre().lower() == nombre.lower()]
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(producto)

    def guardar_en_archivo(self, nombre_archivo):
        with open(nombre_archivo, 'wb') as archivo:
            (self.productos, archivo)
            print("Inventario guardado correctamente.")

    def cargar_desde_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'rb') as archivo:
                (self.productos)
                print("Inventario cargado correctamente.")
        except FileNotFoundError:
            print("Error: Archivo no encontrado.")

            {
                "001": {
                    "id_producto": "001",
                    "nombre": "Vino",
                    "cantidad": 50,
                    "precio": 0.10
                },
                "002": {
                    "id_producto": "002",
                    "nombre": "Lenteja",
                    "cantidad": 60,
                    "precio": 0.7
                },
                "003": {
                    "id_producto": "003",
                    "nombre": "Golosinas",
                    "cantidad": 40,
                    "precio": 0.05
                },
                "004": {
                    "id_producto": "004",
                    "nombre": "Leche",
                    "cantidad": 20,
                    "precio": 0.45
                }
            }
