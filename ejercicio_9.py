# 19. Escribe un programa de un juego de dados. El juego permite jugar a dos jugadores y consiste en implementar la siguiente dinamica: 
# 1. Se lanza un dado, y el numeroq que sale es el objetivo de la partida.
# 2. Por orden, los dos jugadores lanzan dos dados cada uno. Gana la partida el jugador que la suma de los dados que ha lanzado coincide con el objetivo. Podemos gnar los dos, uno o ninguno.
# 3. El juego finaliza cuando un jugador gane 2 partidas. El programa debe implementar el juego descrito y cada partida, el programa preguntara si deseas continuar o parar el juego.
# El juego finaliza cuando uno de los dos jugadores gane o bien cuando se indica que no se quiere jugar mas. Tenga en cuenta que el programa al principio pide el nombre de los dos jugadores y muestra la informacion partida a partida indicando el numero de partidas, el objetivo de la partida, que dados han sacado cada jugador y quien gane la partida y al final del juego indica quien ha ganado y cuantas partidas han jugado. 

from random import *

nameP1 = input("Inserte el nombre del jugador 1")  # Solicita el nombre del jugador 1 al usuario
nameP2 = input("Inserte el nombre del jugador 2")  # Solicita el nombre del jugador 2 al usuario

gameWinP1 = 0  # Inicializa las victorias del jugador 1 en 0
gameWinP2 = 0  # Inicializa las victorias del jugador 2 en 0

numGame = 1  # Inicializa el número de juego en 1

continueGame = True  # Establece la variable para continuar el juego en True

while (gameWinP1 < 2 and gameWinP2 < 2) and continueGame:  # Bucle principal del juego

    print("Partida nº ", numGame)  # Imprime el número de partida actual
    objetivo = randint(1, 6)  # Genera un número objetivo aleatorio entre 1 y 6

    print("El objetivo es ", objetivo)  # Imprime el objetivo de la partida

    num1P1 = randint(1, 6)  # Genera el primer número aleatorio para el jugador 1
    num2P1 = randint(1, 6)  # Genera el segundo número aleatorio para el jugador 1
    sumaP1 = num1P1 + num2P1  # Calcula la suma de los números del jugador 1

    num1P2 = randint(1, 6)  # Genera el primer número aleatorio para el jugador 2
    num2P2 = randint(1, 6)  # Genera el segundo número aleatorio para el jugador 2
    sumaP2 = num1P2 + num2P2  # Calcula la suma de los números del jugador 2

    print("El jugador ", nameP1, " ha sacado ", num1P1, " y ", num2P1)  # Imprime los números obtenidos por el jugador 1
    print("El jugador ", nameP2, " ha sacado ", num1P2, " y ", num2P2)  # Imprime los números obtenidos por el jugador 2

    numWinners = 0  # Inicializa el contador de jugadores ganadores en 0
    if sumaP1 == objetivo:  # Comprueba si la suma del jugador 1 es igual al objetivo
        numWinners = numWinners + 1  # Incrementa el contador de jugadores ganadores en 1
        gameWinP1 = gameWinP1 + 1  # Incrementa las victorias del jugador 1 en 1

    if sumaP2 == objetivo:  # Comprueba si la suma del jugador 2 es igual al objetivo
        numWinners = numWinners + 1  # Incrementa el contador de jugadores ganadores en 1
        gameWinP2 = gameWinP2 + 1  # Incrementa las victorias del jugador 2 en 1

    if numWinners == 2:  # Si ambos jugadores han ganado
        print("Han ganado los dos")
    elif numWinners == 1:  # Si solo un jugador ha ganado
        if sumaP1 == objetivo:  # Si el jugador 1 ha ganado
            print("Ha ganado el jugador ", nameP1)
        if sumaP2 == objetivo:  # Si el jugador 2 ha ganado
            print("Ha ganado el jugador ", nameP2)
    else:  # Si nadie ha ganado
        print("No ha ganado nadie")

    continueGame = input("¿Quieres continuar? (S/N)") == "S"  # Pregunta al usuario si desea continuar el juego

    numGame = numGame + 1  # Incrementa el número de juego en 1

print("Juego terminado")
print("Se han jugado ", numGame, " partidas")  # Imprime el número total de partidas jugadas

if gameWinP1 == 2:  # Si el jugador 1 ha ganado 2 partidas
    print("Gana ", nameP1)
if gameWinP2 == 2:  # Si el jugador 2 ha ganado 2 partidas
    print("Gana ", nameP2)
