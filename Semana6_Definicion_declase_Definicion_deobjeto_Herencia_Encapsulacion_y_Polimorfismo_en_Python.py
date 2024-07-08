# Definición de la clase base Empleado
class Empleado:
    def __init__(self, nombre, salario):
        self._nombre = nombre  # Encapsulación
        self._salario = salario  # Encapsulación

    def obtener_nombre(self):
        return self._nombre

    def obtener_salario(self):
        return self._salario

    def calcular_pago(self):
        raise NotImplementedError("Método calcular_pago debe ser implementado en las clases derivadas")


# Clase derivada Gerente
class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self._departamento = departamento

    def calcular_pago(self):
        return self.obtener_salario() + 1000  # Bonus para gerentes


# Clase derivada Desarrollador
class Desarrollador(Empleado):
    def __init__(self, nombre, salario, lenguaje):
        super().__init__(nombre, salario)
        self._lenguaje = lenguaje

    def calcular_pago(self):
        return self.obtener_salario()  # No hay bonus específico para desarrolladores


# Función polimórfica
def imprimir_pago(empleado):
    print(f"Nombre: {empleado.obtener_nombre()} - Pago: ${empleado.calcular_pago()}")


# Función principal
if __name__ == "__main__":
    # Creación de instancias
    gerente1 = Gerente("Alice", 7000, "Ventas")
    desarrollador1 = Desarrollador("Bob", 6000, "Python")

    # Uso de métodos
    imprimir_pago(gerente1)  # Salida: Nombre: Alice - Pago: $7000
    imprimir_pago(desarrollador1)  # Salida: Nombre: Bob - Pago: $6000