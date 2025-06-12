# esta versión es la base para trabajar en la evaluación III
# Agregar variables para el contador de victorias y empates
victorias_x = 0
victorias_o = 0
empates = 0
#borre la def repetida crear tablero
def crear_tablero():
    tablero = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]  
    return tablero 


def imprimir_tablero(tablero):
    fila = 0 
    while fila < 3:
        print(f"{tablero[fila][0]}|{tablero[fila][1]}|{tablero[fila][2]}")
        if fila < 2:  
            print("-" * 5)
        fila += 1  
#Borre la def repetida imprimir_tablero


def movimiento_jugador(tablero, jugador):
    while True:
        fila = int(input("Elige fila (0, 1, 2): "))
        columna = int(input("Elige columna (0, 1, 2): "))
        if tablero[fila][columna] == " ":
            tablero[fila][columna] = jugador
            break
        else:
            print("¡Casilla ocupada!")


def hay_ganador(tablero):
    # Verificar filas y columnas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != " ":
            return tablero[i][0] #se cambia para que devuelva el simbolo del jugador que gano
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != " ":
            return tablero[0][i] #aca igual  
    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
        return tablero[0][0]#aca tambien
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
        return tablero[0][2]#y aca lo mismo
    
    return None #No hay ganador


def tablero_lleno(tablero):
    for fila in tablero:
        if " " in fila:
            return False
    return True

#cambio el empate que estaba aqui para moverlo en juego completo


import random

def movimiento_ia(tablero):
    casillas_vacias = [(i, j) for i in range(3) for j in range(3) if tablero[i][j] == " "]
    if casillas_vacias:
        fila, columna = random.choice(casillas_vacias)
        tablero[fila][columna] = "O"

#Modificado en el juego completo

def jugada(): #le cambie el nombre a jugada porque se me hace mas comodo
    global victorias_x, victorias_o, empates
    tablero = crear_tablero()
    jugador_actual = "X"
    
    while True:
        imprimir_tablero(tablero)
        print(f"Turno de {jugador_actual}")
        if jugador_actual == "X":
            movimiento_jugador(tablero, jugador_actual)
        else:
            print("Turno de la IA (O)...")
            movimiento_ia(tablero)
        ganador = hay_ganador(tablero)#para que guarde x o 0 quien gana
        if ganador:
            print(f"¡{jugador_actual} ha ganado!")
            
            if ganador == "X":
                victorias_x += 1
            else:
                victorias_o += 1
            break

        if tablero_lleno(tablero):
            print("¡Empate!")
            empates += 1 # Se incrementa el contador
            break
 
        if(jugador_actual=="O"):
            jugador_actual="X"
        else:
            jugador_actual = "O"

#este para que repita hasta que el usuario quiera
def gato_juego():
    while True:
        jugada()
        #le pongo el marcador para que vea si quiere seguir o con eso esta listo
        print("\n--- MARCADOR ACTUAL ---")
        print(f"   Jugador (X): {victorias_x} victorias")
        print(f"   IA (O):      {victorias_o} victorias")
        print(f"   Empates:     {empates}")
        print("-----------------------\n")

        continuar = input("¿Jugar otra partida? (s(Si)/n(No)): ").lower() #lower para que si  lo coloca en mayuscula se ponga en minuscula
        #y por ultimo si no quiere continuar un mensjae de despedida
        if continuar != 's':
            print("Gracias por jugar! :D")
            break

# Llamo a la función principal para iniciar el juego
gato_juego()
#no se parq que estaban ese comentario asi que lo elimine