#1. Escriba un programa que muestre una partida de datos entre dos jugadores, se debe ingresar, la cantidad de turnos que se van a jugar, cada jugador tira un dado. Si un jugador saca un valor mayor que el otro, gana los puntos de ambos dados. Si los dos jugadores sacan el mismo valor, ninguno recibe puntos. Si al finalizar la partida hay un empate, ninguno gana la partida. Debe mostrar quien gana la partida, quien gana cada turno y la puntuacion acumulada por cada jugador.

import random

def tirar_dado():
    return random.randint(1, 6)

def jugar_partida(turnos):
    jugador1_puntos = 0
    jugador2_puntos = 0
    
    for turno in range(1, turnos+1):
        print(f"--- Turno {turno} ---")
        
        jugador1_dado = tirar_dado()
        jugador2_dado = tirar_dado()
        
        print(f"Jugador 1 tiró: {jugador1_dado}")
        print(f"Jugador 2 tiró: {jugador2_dado}")
        
        if jugador1_dado > jugador2_dado:
            jugador1_puntos += jugador1_dado + jugador2_dado
            print("Jugador 1 gana el turno.")
        elif jugador2_dado > jugador1_dado:
            jugador2_puntos += jugador1_dado + jugador2_dado
            print("Jugador 2 gana el turno.")
        else:
            print("Empate en el turno.")
        
        print(f"Puntuación acumulada:")
        print(f"Jugador 1: {jugador1_puntos}")
        print(f"Jugador 2: {jugador2_puntos}")
        print()
    
    if jugador1_puntos > jugador2_puntos:
        print("¡Jugador 1 gana la partida!")
    elif jugador2_puntos > jugador1_puntos:
        print("¡Jugador 2 gana la partida!")
    else:
        print("La partida termina en empate.")

# Inicio del programa
cantidad_turnos = int(input("Ingrese la cantidad de turnos que desea jugar: "))
jugar_partida(cantidad_turnos)