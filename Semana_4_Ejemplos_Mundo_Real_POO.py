# sistema_reservas_Mundo_Real.py

class Habitacion:
    def __init__(self, numero, tipo, precio):
        """
        Inicializa una nueva instancia de la clase Habitacion.

        Args:
        numero (int): El número de la habitación.
        tipo (str): El tipo de habitación (por ejemplo, "simple", "doble").
        precio (float): El precio por noche de la habitación.
        """
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.esta_disponible = True

    def __str__(self):
        return f'Habitación {self.numero} ({self.tipo}) - Precio: {self.precio}'

    def reservar(self):
        """Marca la habitación como no disponible."""
        if self.esta_disponible:
            self.esta_disponible = False
        else:
            print(f'La habitación {self.numero} ya está reservada.')

    def liberar(self):
        """Marca la habitación como disponible."""
        if not self.esta_disponible:
            self.esta_disponible = True
        else:
            print(f'La habitación {self.numero} ya está disponible.')


class Reserva:
    def __init__(self, habitacion, nombre_cliente, noches):
        """
        Inicializa una nueva instancia de la clase Reserva.

        Args:
        habitacion (Habitacion): La habitación que se está reservando.
        nombre_cliente (str): El nombre del cliente que realiza la reserva.
        noches (int): El número de noches que el cliente se quedará.
        """
        self.habitacion = habitacion
        self.nombre_cliente = nombre_cliente
        self.noches = noches

    def calcular_total(self):
        """Calcula el total a pagar por la reserva."""
        return self.noches * self.habitacion.precio

    def confirmar_reserva(self):
        """Confirma la reserva y marca la habitación como no disponible."""
        self.habitacion.reservar()
        print(
            f'Reserva confirmada para {self.nombre_cliente} en la habitación {self.habitacion.numero} por {self.noches} noches. Total a pagar: {self.calcular_total()}.')

    def cancelar_reserva(self):
        """Cancela la reserva y marca la habitación como disponible."""
        self.habitacion.liberar()
        print(f'Reserva cancelada para {self.nombre_cliente} en la habitación {self.habitacion.numero}.')


class Hotel:
    def __init__(self, nombre):
        """
        Inicializa una nueva instancia de la clase Hotel.

        Args:
        nombre (str): El nombre del hotel.
        """
        self.nombre = nombre
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        """Agrega una habitación al hotel."""
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones_disponibles(self):
        """Muestra todas las habitaciones disponibles en el hotel."""
        disponibles = [str(hab) for hab in self.habitaciones if hab.esta_disponible]
        if disponibles:
            print('Habitaciones disponibles:')
            for hab in disponibles:
                print(hab)
        else:
            print('No hay habitaciones disponibles.')


# Ejemplo de uso
if __name__ == "__main__":
    # Crear un hotel
    hotel = Hotel("Hotel Python")

    # Agregar habitaciones al hotel
    hotel.agregar_habitacion(Habitacion(101, "simple", 50.0))
    hotel.agregar_habitacion(Habitacion(102, "doble", 80.0))
    hotel.agregar_habitacion(Habitacion(103, "suite", 150.0))

    # Mostrar habitaciones disponibles
    hotel.mostrar_habitaciones_disponibles()

    # Crear una reserva
    reserva1 = Reserva(hotel.habitaciones[0], "Juan Pérez", 3)
    reserva1.confirmar_reserva()

    # Mostrar habitaciones disponibles después de la reserva
    hotel.mostrar_habitaciones_disponibles()

    # Cancelar la reserva
    reserva1.cancelar_reserva()

    # Mostrar habitaciones disponibles después de cancelar la reserva
    hotel.mostrar_habitaciones_disponibles()