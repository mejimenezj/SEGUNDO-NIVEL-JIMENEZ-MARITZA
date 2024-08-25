class Inventario:
    def __init__(self):
        self.productos = {}
        self.archivo_inventario = 'inventario.txt'
        self.cargar_inventario_desde_archivo()

    def agregar_producto(self, id_producto, nombre, cantidad):
        try:
            self.productos[id_producto] = {'nombre': nombre, 'cantidad': cantidad}
            self.guardar_inventario_en_archivo()
            print(f"Producto '{nombre}' añadido exitosamente al inventario.")
        except Exception as e:
            print(f"Error al añadir el producto: {e}")

    def actualizar_producto(self, id_producto, nombre=None, cantidad=None):
        try:
            if id_producto in self.productos:
                if nombre:
                    self.productos[id_producto]['nombre'] = nombre
                if cantidad is not None:
                    self.productos[id_producto]['cantidad'] = cantidad
                self.guardar_inventario_en_archivo()
                print(f"Producto '{id_producto}' actualizado exitosamente.")
            else:
                print("El producto no existe en el inventario.")
        except Exception as e:
            print(f"Error al actualizar el producto: {e}")

    def eliminar_producto(self, id_producto):
        try:
            if id_producto in self.productos:
                del self.productos[id_producto]
                self.guardar_inventario_en_archivo()
                print(f"Producto '{id_producto}' eliminado del inventario.")
            else:
                print("El producto no existe en el inventario.")
        except Exception as e:
            print(f"Error al eliminar el producto: {e}")

    def guardar_inventario_en_archivo(self):
        try:
            with open(self.archivo_inventario, 'w') as archivo:
                for id_producto, datos in self.productos.items():
                    archivo.write(f"{id_producto},{datos['nombre']},{datos['cantidad']}\n")
        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error al guardar el inventario en el archivo: {e}")

    def cargar_inventario_desde_archivo(self):
        try:
            with open(self.archivo_inventario, 'r') as archivo:
                for linea in archivo:
                    id_producto, nombre, cantidad = linea.strip().split(',')
                    self.productos[id_producto] = {'nombre': nombre, 'cantidad': int(cantidad)}
            print("Inventario cargado exitosamente desde el archivo.")
        except FileNotFoundError:
            print(f"Archivo '{self.archivo_inventario}' no encontrado. Se creará uno nuevo al guardar.")
        except PermissionError:
            print("Error: No tienes permisos para leer el archivo.")
        except Exception as e:
            print(f"Error al cargar el inventario desde el archivo: {e}")