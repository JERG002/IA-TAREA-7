import math

X = "X"
O = "O"
EMPTY = None

def ImprimirTablero(tablero):
    for fila in tablero:
        print("| ", end="")
        for celda in fila:
            if celda is None:
                print(" ", end=" | ")
            else:
                print(celda, end=" | ")
        print()
        print("-" * 13)


def Ganador(tablero):
    for fila in tablero:
        if fila.count(fila[0]) == len(fila) and fila[0] is not None:
            return fila[0]
    # Check columns
    for col in range(len(tablero)):
        if tablero[0][col] == tablero[1][col] == tablero[2][col] and tablero[0][col] is not None:
            return tablero[0][col]
    # Check diagonals
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] is not None:
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] is not None:
        return tablero[0][2]
    # No Ganador
    return None

# Returns True if the tablero is TableroLLeno
def TableroLLeno(tablero):
    for fila in tablero:
        for celda in fila:
            if celda == EMPTY:
                return False
    return True

# Returns a list of (fila, col) tuples for empty celdas
def EspaciosVacios(tablero):
    celdas = []
    for fila in range(len(tablero)):
        for col in range(len(tablero)):
            if tablero[fila][col] == EMPTY:
                celdas.append((fila, col))
    return celdas

# Evaluars the tablero
def Evaluar(tablero):
    if Ganador(tablero) == X:
        return 1
    elif Ganador(tablero) == O:
        return -1
    else:
        return 0

# Minimax algorithm
def minimax(tablero, profundidad, jugador):
    if jugador == X:
        best = [-1, -1, -math.inf]
    else:
        best = [-1, -1, math.inf]

    if profundidad == 0 or TableroLLeno(tablero):
        score = Evaluar(tablero)
        return [-1, -1, score]

    for celda in EspaciosVacios(tablero):
        fila, col = celda
        tablero[fila][col] = jugador
        if jugador == X:
            score = minimax(tablero, profundidad - 1, O)
        else:
            score = minimax(tablero, profundidad - 1, X)
        tablero[fila][col] = EMPTY
        score[0], score[1] = fila, col

        if jugador == X:
            if score[2] > best[2]:
                best = score
        else:
            if score[2] < best[2]:
                best = score

    return best

# Main function
def main():
    tablero = [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
    print("Tic Tac Toe")
    print("------------")
    ImprimirTablero(tablero)
    while not TableroLLeno(tablero):
        fila = int(input("Ingrese numero de fila (0-2): "))
        col = int(input("Ingrese numero de columna (0-2): "))
        if tablero[fila][col] != EMPTY:
            print("Movimiento invalido")
            continue
        tablero[fila][col] = X
        ImprimirTablero(tablero)
        if Ganador(tablero) == X:
            print("Has ganado!")
            return
        elif TableroLLeno(tablero):
            print("Empate!")
            return
        print("Turno de la computadora")
        fila, col, score = minimax(tablero, 4, O)
        tablero[fila][col] = O
        ImprimirTablero(tablero)
        if Ganador(tablero) == O:
            print("La computadora gana!")
            return
        elif TableroLLeno(tablero):
            print("Empate!")
            return
    

main()