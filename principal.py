from carta import  Naipe
from jugador import Jugador

_tuto = False    # El tutorial solo se preguntará en la primera partida.
_inicio = False
def principal():
    global tuto
    global _inicio
    print('\n¡Bienvenido de nuevo al juego de las siete y media!')
    tutorial()
    if _inicio is False:
        Naipe.generar_baraja()
        _inicio = True
    num_humanos = int(input('¿Cuántos vamos a jugar?: '))
    Jugador.asignar_humanos(num_humanos)
    jugar()

def jugar():
    """Gestiona la partida."""
    while Jugador.jugadores() != []:
        Naipe.barajar()
        repartir_mesa(1)
        for jugador in list(Jugador.jugadores()):
            turno(jugador)
            comprobar_fin_jugador(jugador)
        comprobar_fin_ronda()
        recoger_mesa()
        comprobar_fin_juego()

def turno(jugador):
    """
    Ejecuta el turno de un jugador.
    """
    print(f'\n¡Es el turno de {jugador.nombre()}!')
    # if jugador.bot() is True: Por el momento no hay bots
    correcto = False
    while not correcto:
        print(f'\n[{jugador.nombre()}] | Salud: [{jugador.vida()}] | Total: '\
            f'[{Naipe.sm_valores(jugador.mano())}] | '\
            f'Mano: {Naipe.mostrar_cartas(jugador.mano())}')
        if comprobar_pasada(jugador): break # De este modo, si el jugador se pasa de 7.5, no se le pedirán más cartas
        try:
            respuesta = input('¿Quieres otra carta (S/N)?: ').upper()
            if respuesta == 'S' or respuesta =='Y':
                jugador.recibir_mano(Naipe.repartir(1))
            elif respuesta == 'N':
                correcto = True
        except TypeError:
            print('Por favor, elige una opción válida.')

def comprobar_pasada(jugador):
    if Naipe.sm_valores(jugador.mano()) > 7.5:
        print (f'¡{jugador.nombre()} se ha pasado de las '\
            'siete y media y pierde 2 puntos de salud!')
        jugador.set_vida(jugador.vida() - 2)
        input('Pulsa una tecla para continuar.')
        return True
    else: return False

def comprobar_fin_jugador(jugador):
    if jugador.vida() <= 0:
        print (f'¡{jugador.nombre()} ha perdido!')
        Jugador.borrar_jugador(jugador)
        if len(jugador.jugadores()) <= 1:
            comprobar_fin_juego()
        input('Pulsa una tecla para continuar.')

def comprobar_fin_ronda():
    if Jugador.jugadores() == []: # Si no queda ningún jugador con vida
            finalizar()
    ganador = Jugador.get_jugador(0)
    for jugador in Jugador.jugadores():
        puntos_ganador = Naipe.sm_valores(ganador.mano())
        puntos_jugador = Naipe.sm_valores(jugador.mano())
        if puntos_jugador > 7.5: continue
        if puntos_ganador > 7.5 or puntos_ganador < puntos_jugador:
            ganador = jugador
    ganador.set_vida(ganador.vida() + 1)
    print(f'¡{ganador.nombre()} gana esta ronda con '\
        f'{Naipe.sm_valores(ganador.mano())} puntos y obtiene un punto '\
            'de salud!.')
    input('Pulsa una tecla para comenzar una nueva ronda.')

def comprobar_fin_juego():
    if len(Jugador.jugadores()) == 1:   # Si sólo queda un jugador
        print(f'¡{Jugador.get_jugador(0).nombre()} gana esta partida!')
        input('Pulsa una tecla para terminar.')
        Jugador.limpiar_jugadores()
        finalizar()

def repartir_mesa(num_cartas):
    for jugador in Jugador.jugadores():
        jugador.recibir_mano(Naipe.repartir(num_cartas))

def recoger_mesa():
    for jugador in Jugador.jugadores():
        jugador.devolver_mano()

def repetir():
    """Pregunta si quiere volver a jugar otra partida"""
    correcto = False
    respuesta = None
    while not correcto:
        try:
            respuesta = input('¿Te gustaría jugar de nuevo (S/N)?: ').upper()
            if respuesta == 'S' or respuesta =='Y':
                print('Repartidor.- Muy bien, volvamos a empezar entonces')
                return True
            elif respuesta == 'N':
                print('Repartidor.- De acuerdo. ¡Vuelve cuando quieras!')
                return False
        except ValueError:
            print('Por favor, elige una opción válida.')

def finalizar():
    """El repartidor pregunta al jugador si quiere volver a jugar."""
    print('\nRepartidor.- Bueno, esto ha sido todo por ahora.')
    decision = repetir()
    if decision == True:
        principal()
    else:
        print('(El repartidor se desvanece en la oscuridad.)')

def tutorial():
    """
    Pregunta si quiere que se le explique las reglas del juego.
    """
    global _tuto
    if _tuto == True:
        return
    else:
        correcto = False
        while not correcto:
            try:
                respuesta = input('¿Quieres que te explique las reglas del '\
                    'juego (S/N)?: ').upper()
                if respuesta == 'S' or respuesta =='Y':
                    explicar()
                    correcto = True
                elif respuesta == 'N':
                    correcto = True
            except TypeError:
                print('Por favor, elige una opción válida.')
        _tuto = True

def explicar():
    """Explica al jugador las reglas del juego."""
    correcto = False
    respuesta = ''
    print(f'\nBien, presta atención, seré breve: '\
        '\nEl juego consiste en obtener siete puntos y medio, o acercarse a '\
        'ello lo más posible. Las cartas valen tantos puntos como su valor '\
        'facial, excepto las figuras, que valen medio punto. '\
        '\n\
        \nLa banca reparte una carta a cada jugador y cada jugador, por '\
        'turno, puede pedir cartas a la banca. Cuando todos los jugadores '\
            'han jugado, gana la ronda aquel que tenga más puntos que los '\
            'demás, sin pasar de siete y media.'\
        '\n\
        \nEl ganador de cada ronda gana un punto de salud, mientras que si '\
        'un jugador se pasa de siete puntos y medio, será penalizado '\
        'restándole 2 puntos de salud. La partida termina cuando solo queda '\
            'un jugador en pie.')
    while not correcto:
        try:
            respuesta = input('¿Quieres que te lo repita (S/N)?: ').upper()
            if respuesta == 'S' or respuesta =='Y':
                explicar()
                correcto = True
            elif respuesta == 'N':
                correcto = True
        except ValueError:
            print('Por favor, elige una opción válida.')

if __name__ == "__main__":
    principal()
