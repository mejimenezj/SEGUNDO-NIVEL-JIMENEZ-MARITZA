# calculations.py

"""
Este programa calcula el área de un círculo y un rectángulo, y convierte unidades de medida de pulgadas a centímetros.
"""

# Importar la biblioteca math para usar pi
import math


# Función para calcular el área de un círculo
def area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.

    :param radio: Radio del círculo (float)
    :return: Área del círculo (float)
    """
    return math.pi * (radio ** 2)


# Función para calcular el área de un rectángulo
def area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo dado su base y altura.

    :param base: Base del rectángulo (float)
    :param altura: Altura del rectángulo (float)
    :return: Área del rectángulo (float)
    """
    return base * altura


# Función para convertir pulgadas a centímetros
def pulgadas_a_centimetros(pulgadas):
    """
    Convierte una medida en pulgadas a centímetros.

    :param pulgadas: Medida en pulgadas (float)
    :return: Medida en centímetros (float)
    """
    return pulgadas * 2.54


# Ejemplo de uso de las funciones
if __name__ == "__main__":
    radio = 5.0
    base = 10.0
    altura = 4.0
    pulgadas = 12.0

    print(f"Área del círculo con radio {radio} es: {area_circulo(radio):.2f}")
    print(f"Área del rectángulo con base {base} y altura {altura} es: {area_rectangulo(base, altura):.2f}")
    print(f"{pulgadas} pulgadas son {pulgadas_a_centimetros(pulgadas):.2f} centímetros")