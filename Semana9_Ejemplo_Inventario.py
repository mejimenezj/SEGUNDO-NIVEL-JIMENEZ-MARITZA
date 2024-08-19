class Inventario:
    def __init__(self):
        self.productos = []

    def añadir_producto(self, producto):
        if self.buscar_por_id(producto.get_id_producto()):
            print("Error: El ID del producto ya existe.")
        else:
            self.productos.append(producto)
            print("Producto añadido exitosamente.")

    def eliminar_producto(self, id_producto):
        producto = self.buscar_por_id(id_producto)
        if producto:
            self.productos.remove(producto)
            print("Producto eliminado exitosamente.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        producto = self.buscar_por_id(id_producto)
        if producto:
            if nueva_cantidad is not None:
                producto.set_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                producto.set_precio(nuevo_precio)
            print("Producto actualizado exitosamente.")
        else:
            print("Producto no encontrado.")

    def buscar_por_id(self, id_producto):
        for producto in self.productos:
            if producto.get_id_producto() == id_producto:
                return producto
        return None

    def buscar_por_nombre(self, nombre):
        productos_encontrados = [producto for producto in self.productos if nombre.lower() in producto.get_nombre().lower()]
        return productos_encontrados

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            for producto in self.productos:
                print(producto)