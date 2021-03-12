from random import shuffle as mezclar

class Carta:
    """
    Clase Carta
    ---
    La clase Carta representa y almacena las cartas en una baraja.
    La carta está compuesta por:
        - corta: str -> Descripción corta de la carta (ej: 'C10')
        - larga: str -> Descripción larga de la carta \
            (ej: 'Rey de copas')

    Ea la baraja, las cartas se identifican por:
        - int numero; Numero que define en que posición se encuentra \
            la carta dentro de la baraja.
        - Su valor, compuesto por una carta.

    """
    __baraja = []
    __ultima = 0

    # Métodos mágicos
    def __init__(self, corta, larga):
        """Constructor de la clase Carta"""
        Carta.__ultima += 1
        self.__numero = Carta.__ultima
        self.__corta = corta
        self.__larga = larga
        Carta.__baraja.append(self)

    def __repr__(self):
        return f"Carta('{self.corta()}', '{self.larga()}')"

    # Métodos estáticos
    @staticmethod
    def baraja():
        """Devuelve la baraja."""
        return Carta.__baraja

    @staticmethod
    def get_carta(seleccion):
        """
        Devuelve una carta existente en la baraja a partir de su \
            número.\n
        Parámetros:
            - seleccion: int -> La n-ésima carta de la baraja.
        """
        return Carta.baraja()[seleccion]

    @staticmethod
    def repartir(cantidad):
        """Reparte una cantidad de cartas de la baraja, retirandolas \
            de la misma y devolviéndolas."""
        mano = []
        while cantidad > 0:
            mano.append(Naipe.get_carta(0))
            del Naipe.baraja()[0]
            cantidad -= 1
        return mano

    @staticmethod
    def mostrar_cartas(cartas):
        """Devuelve una descripción completas de una lista de cartas \
            recibida."""
        resultado = ''
        for carta in cartas:
            resultado += (f'{carta.describir()}, ')
        return resultado

    @staticmethod
    def mostrar_baraja():
        """Devuelve una descripción completas de todas las cartas de \
            la baraja."""
        resultado = ''
        for carta in Carta.baraja():
            resultado += (f'{carta.describir()}, ')
        return resultado

    # Permutadores
    @staticmethod
    def barajar():
        """Mezcla la baraja como lo haría un crupier."""
        Naipe.lavar()
        Naipe.rifflear()
        Naipe.cortar()
        Naipe.rifflear()
        Naipe.cortar()
        Naipe.rifflear()

    @staticmethod
    def lavar():
        """Mezcla las cartas de la baraja de forma aleatoria."""
        mezclar(Carta.baraja())

    def cortar():
        """Hace tres montos, y los intercala con el fondo arriba."""
        baraja = Carta.baraja()
        resultado = []
        cima = baraja[:len(baraja)//3]
        base = baraja[-len(baraja)//3:]
        for carta in cima:
            baraja.remove(carta)
        for carta in base:
            baraja.remove(carta)
        resultado = cima + baraja + base
        Carta.__baraja = resultado

    @staticmethod
    def rifflear():
        """Separa la baraja en dos mitades y luego las intercala."""
        baraja = Carta.baraja()
        resultado = []
        pila1 = baraja[:len(baraja)//2]
        pila2 = baraja[-len(baraja)//2:]

        for i in range((len(baraja)//2)):
            pareja = [pila1[i], pila2[i]]
            resultado += pareja
        Carta.__baraja = resultado

    @staticmethod
    def arrastrar():
        """
        Mezcla las cartas, haciendo parejas con la cima y la base de \
            la baraja.
        """
        baraja = Carta.baraja()
        resultado = []

        for i in range((len(baraja)//2)):
            pareja = [baraja[i], baraja[-(i+1)]]
            resultado += pareja
        Carta.__baraja = resultado

    # Métodos selectores
    def numero(self):
        """Devuelve el numero de la carta."""
        return self.__numero

    def corta(self):
        """Devuelve una descripción (o denominación) de la carta."""
        return self.__corta

    def larga(self):
        """Devuelve una descripción larga de la carta."""
        return self.__larga

    # Otros métodos:
    def describir(self):
        """
        Devuelve una descripción completa de una carta de la baraja.\n
        Parámetros:
            - seleccion: int -> La n-ésima carta de la baraja.
        """
        return f'[{self.corta()}]: {self.larga()}'

class Naipe(Carta):
    """
    Clase Naipe
    ---
    La clase Naipe representa cartas de naipes de la baraja española, \
        las cuáles se identifican por su palo y su valor.
    """

    # Métodos mágicos
    def __init__(self, palo, valor):
        """Constrctor de la clase Naipe. Subclase de la clase Carta."""
        super().__init__(Naipe.generar_corta(palo, valor) \
            , Naipe.generar_larga(palo, valor))
        self.__palo = palo
        self.__valor = valor

    def __repr__(self):
        return f"Naipe('{self.palo()}', '{self.valor()}')"

    # Métodos estáticos
    @staticmethod
    def generar_baraja():
        """Genera una baraja de naipes española de 40 cartas."""
        palos = ['Oros', 'Copas', 'Espadas', 'Bastos']
        valores = list(range(1, 11))[::-1]
        for palo in palos[::-1]:
            for valor in valores:
                Naipe(palo, valor)

    @staticmethod
    def generar_corta(palo, valor):
        """
        Genera una decripción corta de un naipe, a partir de su
            palo y valor.\n
        La descripción corta de un naipe tiene esta composición:\n
            - El primer caracter del palo : 'Bastos'[0] -> 'B'
            - El literal del valor : 7 -> '7' \
            Ejemplo: 'Rey de Bastos' ->'B10'\n
        """
        palo = palo[0]
        valor = str(valor)
        return palo + valor

    @staticmethod
    def generar_larga(palo, valor):
        """
        Genera una decripción larga de un naipe, a partir de su \
            palo y valor.\n
        La descripción larga se trata de un literal en lenguaje \
            natural que describe a la carta.
        Ejemplo: Naipe('Copas', 8) -> 'Sota de Copas'.
        """
        literales = ['Uno', 'Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis', \
            'Siete','Sota', 'Caballero', 'Rey']
        return f'{literales[valor-1]} de {palo}'

    # Métodos selectores
    def palo(self):
        """"Devuelve el palo de un naipe."""
        return self.__palo

    def valor(self):
        """Devuelve el valor de un naipe."""
        return self.__valor

    # Otros métodos
    def comparar_naipes(naipe1, naipe2):
        """Compara dos cartas y devuelve la de valor superior."""
        if naipe1.valor() > naipe2.valor():
            return naipe1
        else: return naipe2

    def sm_valores(naipes):
        """Valores del 7 y medio."""
        total = 0
        for naipe in naipes:
            if naipe.valor() in list(range(8, 11)):
                total += 0.5
            else:
                total += naipe.valor()
        return total

# Demostración:
if __name__ == "__main__":
    print('Esto es una pequeña demostración de que cómo funciona la clase '\
     'Carta y, en especial, la subclase Naipe.\n')
    Naipe.generar_baraja()
    print('Primero vamos a desempolvar la baraja, y vamos a poner todas '\
        f'nuestras cartas boca arriba:\n{Naipe.mostrar_baraja()}\n')

    print('Impecable y ordenada. Un detalle interesante es que puedo '\
        'obtener en todo momento una carta a partir de su posición. Por '\
        f'ejemplo, la carta en la posición 28 es: {Naipe.get_carta(28)}\n')
    print(f'O mejor aún, podemos obtener una descripción literal de que '\
        'carta se trata, por ejemplo, de la carta 17: '\
        f'{Naipe.get_carta(17).describir()}\n')

    print('También podemos hacer algo muy interesante. Comparar dos cartas. '\
        'Comparamos sus valores y nos devuelve la de mayor valor.')
    print('Vamos por ejemplo a comparar las dos cartas que hemos obervado '\
        'antes, la sota de espadas y el 7 de copas: '\
        f'{Naipe.comparar_naipes(Naipe.get_carta(28), Naipe.get_carta(17))}')
    print('Como era de esperar, nos devuelve la sota de Espadas, por tener '\
        'un valor mayor. (8 > 7)')
    # Más adelante incluiré el factor de la "vira", que hara que un palo \
        # tenga mayor valor que el resto de naipes

    print('Ahora vamos a barajar las cartas cuidadosamente...')
    Naipe.barajar()
    print('Y tras barajar, la carta de la posición 28 ya no es la sota de '\
        f'espadas, ahora es: {Naipe.get_carta(28).describir()}\n')
    print('Volvamos a ver la baraja para confirmar que está completamente '\
        f'mezlcada:\n{Naipe.mostrar_baraja()}\n')

    """
    Repartiremos las 3 cartas primeras cartas que se encuentren en la \
        cima de la baraja y por consiguiente son retiradas de la \
        baraja. Por el momento estas cartas no van a ningún sitio, \
        pero pretendo que la clase Jugador las reciba y guarde con el \
        nombe de "mano".
    """

    print('Vamos a repartir las tres primeras cartas que hay arriba de la '\
        f'baraja:\n{Naipe.repartir(3)}\n')
    print('Ahora si volvemos a ver una vez más la baraja, podremos ver que '\
        f'esas 3 cartas ya no se encuentran:\n{Naipe.mostrar_baraja()}\n')
