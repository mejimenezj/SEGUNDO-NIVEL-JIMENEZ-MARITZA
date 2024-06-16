# Programación Tradicional
# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    for dia in range(7):  # Suponemos una semana de 7 días
        temp = float(input(f"Ingrese la temperatura para el día {dia + 1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio_semanal(temperaturas):
    if len(temperaturas) == 0:
        return 0
    return sum(temperaturas) / len(temperaturas)

# Función principal para ejecutar el programa
def main():
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio_semanal(temperaturas)
    print(f"El promedio de las temperaturas semanales es: {promedio:.2f}")

# Ejecutar el programa
if __name__ == "__main__":
    main()

#Programación Orientada a Objetos (POO)
class ClimaDiario:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperaturas(self):
        for dia in range(7):  # Suponemos una semana de 7 días
            temp = float(input(f"Ingrese la temperatura para el día {dia + 1}: "))
            self.temperaturas.append(temp)

    def calcular_promedio_semanal(self):
        if len(self.temperaturas) == 0:
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)

# Función principal para ejecutar el programa
def main():
    clima = ClimaDiario()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio_semanal()
    print(f"El promedio de las temperaturas semanales es: {promedio:.2f}")

