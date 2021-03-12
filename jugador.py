from random import choice as aleatorio
from carta import Naipe

VIDA_INICIAL = 6

class Jugador:
    """
    Clase Jugador
    ---
    La clase Jugador representa a un jugador y almacena información \
    sobre éste, compuesta principalmente por su nombre, su salud y \
    su mano de cartas. Los jugadores pueden ser bots controlados por \
    el programa.
    """
    __ultimo = 0
    __jugadores = []

    def __init__(self, nombre, vida, bot):
        Jugador.__ultimo += 1
        if Jugador.comprobar_nombre(nombre) is True:
            self.__numero = self.__ultimo
            self.__nombre = nombre
            self.__vida = vida
            self.__bot = bot
            Jugador.__jugadores.append(self)
            self.__mano = []
        else:
            print('Lo sentimos, pero ya existe un jugador con el '\
                f'nombre "{nombre}".')

    def __repr__(self):
        return f"Jugador('{self.__nombre}', '{self.__vida}, {self.__bot}'')"

    def __str__(self):
        return f'{self.nombre()} | Salud: {self.vida()} | '\
            f'Mano({len(self.mano())}):\n {Naipe.mostrar_cartas(self.mano())}'

    @staticmethod
    def get_jugador(seleccion):
        """
        Devuelve un jugador existente en la lista, a partir de su nº.

        Parámetros:
            - seleccion: int -> El n-ésima jugador de la lista.
        """
        return Jugador.jugadores()[seleccion]

    @staticmethod
    def jugadores():
        """Devuelve la lista de jugadores."""
        return Jugador.__jugadores

    @staticmethod
    def limpiar_jugadores():
        """Elimina todos los jugadores de la lista."""
        Jugador.__jugadores = []

    @staticmethod
    def comprobar_nombre(nombre):
        """Comprueba si ya existe algun jugador con ese nombre."""
        resultado = True
        for jugador in Jugador.jugadores():
            if nombre == jugador.nombre():
                resultado = False
        return resultado

    @staticmethod
    def nombre_aleatorio():
        """Devuelve un nombre aleatorio de la lista de nombres."""
        nombres = (
            'Lucía', 'Roberto', 'Belén', 'Alicia', 'Juan', 'Paloma', \
            'Natalia', 'Josemi','Andrés', 'Isabel', 'Pablo','Álex', \
            'Vicenta', 'Marisa', 'Concha', 'Mauri', 'Fernando', 'Emilio', \
            'Mariano', 'Paco'
            )
        return aleatorio(nombres)

    @staticmethod
    def asignar_humanos(num_jugadores):
        """
        Creador interactivo de humanos. Solicita por entrada el \
            nombre del jugador.
        """
        for i in range(num_jugadores):
            try:
                nombre_jugador = str(input('¿Nombre del jugador?: '))
            except ValueError:
                print('Por favor, elige una opción válida.')
            Humano(nombre_jugador)

    @staticmethod
    def asignar_bots(num_bots):
        """
        Creador interactivo de bots. Asigna nombres de forma automática.
        """
        for i in range(num_bots):
            nombre = Jugador.nombre_aleatorio()
            while Jugador.comprobar_nombre(nombre) is not True:
                nombre = Jugador.nombre_aleatorio()
            Bot(nombre)

    def numero(self):
        """Devuelve el numero del jugador."""
        return self.__numero

    def nombre(self):
        """Devuelve el nombre del jugador."""
        return self.__nombre

    def vida(self):
        """Devuelve la salud del jugador."""
        return self.__vida

    def bot(self):
        """
        Devuelve True si el jugador es un bot, False en otro caso.
        """
        return self.__bot

    def mano(self):
        """Devuelve la mano del jugador."""
        return self.__mano

    def set_vida(self, vida):
        """Asigna un nuevo valor a la vida del jugador."""
        self.__vida = vida

    def set_mano(self, mano):
        """Asigna una nueva mano al jugador."""
        self.__mano = mano

    def recibir_mano(self, mano):
        """Recibe una mano de cartas."""
        self.__mano += mano

    def devolver_mano(self):
        """Devuelve las cartas de su mano a la baraja."""
        aux = Naipe.baraja()
        aux += self.mano()
        self.__mano = []
        Naipe.__baraja = aux

    def borrar_jugador(jugador):
        """Borra un jugador de la lista de jugadores."""
        Jugador.jugadores().remove(jugador)

class Humano(Jugador):
    """
    Clase Humano
    ---
    La clase Humano representa a un jugador humano de la partida. Se \
        espera que estos jugadores tomen decisiones propias.
    """
    def __init__(self, nombre):
        super().__init__(nombre, VIDA_INICIAL, False)

    def __str__(self):
        return f'Humano: {super().__str__()}'

class Bot(Jugador):
    """
    Clase Bot
    ---
    La clase Bot representa a un jugador de la partida, controlado \
        por la máquina.
    """
    def __init__(self, nombre):
        super().__init__(nombre, VIDA_INICIAL, True)

    def __str__(self):
        return f'BOT: {super().__str__()}'
