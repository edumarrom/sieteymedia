# Siete y media: Juego de naipes español
## Por Eduardo Martínez Romero ([edumarrom](https://github.com/edumarrom/) en GitHub )
Es el primer juego que escribo en Python mediante la programación orientada a objetos. No está completamente pulido, y advierto que habrá más de un "gazapo", tanto a la hora de funcionar como en la forma en que ha sido escrito. El objetivo de escribir este juego era poner en práctica la materia estudiada en el segundo trimestre del módulo de programación del primer curso en Desarrollo de Aplicaciones Web.

### Sobre el juego:
Las siete y media es un juego de naipes español que consiste en obtener siete puntos y medio, o acercarse a ello lo más posible. Las cartas valen tantos puntos como su valor facial, excepto las figuras, que valen medio punto.

En esta adaptación del juego no existen las apuestas, sino que cada jugador tiene 6 puntos de vida. La banca reparte una carta a cada jugador y cada jugador, por turno, puede pedir cartas a la banca. Cuando todos los jugadores han jugado, gana la ronda aquel que tenga más puntos que los demás, sin pasar de siete y media. El ganador de cada ronda obtiene un punto de salud, mientras que si un jugador se pasa de siete puntos y medio, será penalizado restándole 2 puntos de salud. La partida termina cuando solo queda un jugador en pie.

Quizás lo más interesante de este programa sea la implementación del módulo *carta.py*, el cuál contiene las clases Carta y Naipe, siendo esta última la responsable de crear una baraja de naipes, mientras que la Clase carta implementa distintas formas de barajar el mazo, que simulan los movimientos que se realizan para permutar correctamente las cartas.

Si se observa el código, se puede observar contenido que finalmente no ha sido utilizado, pero puede resultar de interés en la realización de otros juegos de cartas.

### ¿Cómo jugar?
Clona el repositorio y ejecuta el módulo *principal.py*.

---
### Fuentes:
- [Siete y media (wikipedia.org)](https://es.wikipedia.org/wiki/Siete_y_media)
- [Baraja española (wikipedia.org)](https://es.wikipedia.org/wiki/Baraja_espa%C3%B1ola)
- [Riffle shuffle permutation (wikipedia.org)](https://en.wikipedia.org/wiki/Riffle_shuffle_permutation)
- [Shuffling (wikipedia.org)](https://en.wikipedia.org/wiki/Shuffling)
