# Consideraremos una clase Conexion que simula la apertura y cierre
# de una conexión a una base de datos:
class Conexion:
    def __init__(self, nombre):
        self.nombre = nombre
        print(f"Conexión a la base de datos '{self.nombre}' establecida.")

    def __del__(self):
        print(f"Conexión a la base de datos '{self.nombre}' cerrada.")

# Aquí, el constructor __init__ se encarga de establecer la conexión,
# mientras que el destructor __del__ se encarga de cerrarla.

# Al crear y eliminar instancias de Conexion, se pueden observar las acciones
# de los constructores y destructores:

mi_conexion = Conexion("BaseDatos1")
del mi_conexion

# La instancia mi_conexion de la clase Conexion se crea y luego se elimina.
# Esto desencadena primero el constructor y luego el destructor, gestionando
# adecuadamente la vida útil de la conexión.