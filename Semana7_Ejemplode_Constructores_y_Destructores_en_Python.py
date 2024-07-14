# Definición de una clase Persona que utiliza constructor y destructor
class Persona:
    # Constructor: Inicializa los atributos nombre y edad
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print(f"Persona {self.nombre}, de {self.edad} años, ha sido creada.")

    # Método para mostrar información de la persona
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

    # Destructor: Realiza una acción de limpieza (en este caso, solo imprime un mensaje)
    def __del__(self):
        print(f"Persona {self.nombre}, de {self.edad} años, ha sido destruida.")


# Función principal para demostrar el uso de la clase Persona
def main():
    # Crear una instancia de Persona
    persona1 = Persona("Alice", 30)
    # Mostrar la información de la persona
    persona1.mostrar_info()

    # Crear otra instancia de Persona
    persona2 = Persona("Bob", 25)
    # Mostrar la información de la persona
    persona2.mostrar_info()

    # Eliminar la instancia persona2 explícitamente
    del persona2

    # La instancia persona1 será destruida automáticamente al finalizar el programa


# Ejecutar la función principal
if __name__ == "__main__":
    main()