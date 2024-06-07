class Ser:
    def __init__(self, nombre, poder, agilidad, defensa, vitalidad):
        self.nombre = nombre
        self.poder = poder
        self.agilidad = agilidad
        self.defensa = defensa
        self.vitalidad = vitalidad

    def mostrar_atributos(self):
        print(f"{self.nombre}:")
        print(f"  - Poder: {self.poder}")
        print(f"  - Agilidad: {self.agilidad}")
        print(f"  - Defensa: {self.defensa}")
        print(f"  - Vitalidad: {self.vitalidad}")

    def subir_nivel(self, aumento_poder, aumento_agilidad, aumento_defensa):
        self.poder += aumento_poder
        self.agilidad += aumento_agilidad
        self.defensa += aumento_defensa

    def esta_vivo(self):
        return self.vitalidad > 0

    def morir(self):
        self.vitalidad = 0
        print(f"{self.nombre} ha muerto.")

    def atacar(self, enemigo):
        daño = self.poder - enemigo.defensa
        if daño > 0:
            enemigo.vitalidad -= daño
            print(f"{self.nombre} ha infligido {daño} puntos de daño a {enemigo.nombre}.")
        else:
            print(f"El ataque de {self.nombre} no ha tenido efecto.")

        if not enemigo.esta_vivo():
            enemigo.morir()

class Berserker(Ser):
    def __init__(self, nombre, poder, agilidad, defensa, vitalidad, hacha):
        super().__init__(nombre, poder, agilidad, defensa, vitalidad)
        self.hacha = hacha

    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Espada de Fuego, daño 12. (2) Hacha de Trueno, daño 15)\n"))
        if opcion == 6:
            self.hacha = 10
        elif opcion == 4:
            self.hacha = 20
        else:
            print("Número de arma incorrecto.")

    def mostrar_atributos(self):
        super().mostrar_atributos()
        print(f"  - Arma: Hacha (daño {self.hacha})")

    def atacar(self, enemigo):
        daño = self.poder * self.hacha - enemigo.defensa
        super().atacar(enemigo, daño)

class Hechicero(Ser):
    def __init__(self, nombre, poder, agilidad, defensa, vitalidad, grimorio):
        super().__init__(nombre, poder, agilidad, defensa, vitalidad)
        self.grimorio = grimorio

    def mostrar_atributos(self):
        super().mostrar_atributos()
        print(f"  - Grimorio: {self.grimorio}")

    def atacar(self, enemigo):
        daño = self.poder * self.grimorio - enemigo.defensa
        super().atacar(enemigo, daño)

def combate(jugador1, jugador2):
    turno = 0
    while jugador1.esta_vivo() and jugador2.esta_vivo():
        print(f"\nTurno {turno}")
        print(f">>> Acción de {jugador1.nombre}:")
        jugador1.atacar(jugador2)

        print(f">>> Acción de {jugador2.nombre}:")
        jugador2.atacar(jugador1)

        turno += 1

    if jugador1.esta_vivo():
        print(f"\n¡{jugador1.nombre} ha ganado!")
    elif jugador2.esta_vivo():
        print(f"\n¡{jugador2.nombre} ha ganado!")
    else:
        print("\n¡Empate!")

# Ejemplo de uso
guerrero = Berserker("Guts", 20, 12, 4, 110, 11)
hechicera = Hechicero("Yennefer", 13, 22, 8, 100, 6)

# Mostrar atributos de los personajes
guerrero.mostrar_atributos()
hechicera.mostrar_atributos()

# Combate entre los personajes