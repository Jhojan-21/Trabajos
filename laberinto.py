
laberinto = [
    ['F', 1, 1, 3, 0, 1, 1, 1, 4],
    [3, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 3, 1, 1],
    [3, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 3, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 4],
    ['I', 1, 3, 1, 0, 1, 1, 1, 1]
]

FILAS = len(laberinto)
COLUMNAS = len(laberinto[0])
PUNTOS_MINIMOS = 23

# Movimientos: arriba, derecha, abajo e izquierda

movimientos = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
]


def imprimir_laberinto(matriz):
    for fila in matriz:
        print(" ".join(f"{celda:>2}" for celda in fila))


def buscar_inicio():
    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            if laberinto[fila][columna] == 'I':
                return fila, columna
    return None


def resolver(fila, columna, puntos, camino, visitadas):
    # Si llegamos a la meta, verificamos los puntos
    if laberinto[fila][columna] == 'F':
        if puntos >= PUNTOS_MINIMOS:
            return True
        return False

    # Probamos los cuatro movimientos posibles
    for df, dc in movimientos:
        nueva_fila = fila + df
        nueva_columna = columna + dc

        if not (0 <= nueva_fila < FILAS and
                0 <= nueva_columna < COLUMNAS):
            continue

        posicion = (nueva_fila, nueva_columna)
        celda = laberinto[nueva_fila][nueva_columna]

        # No atravesamos paredes ni repetimos casillas
        if celda == 0 or posicion in visitadas:
            continue

        # Sumamos el valor de la casilla recorrida
        nuevos_puntos = puntos
        if isinstance(celda, int):
            nuevos_puntos += celda

        # Seguimos
        camino.append(posicion)
        visitadas.add(posicion)

        if resolver(
            nueva_fila,
            nueva_columna,
            nuevos_puntos,
            camino,
            visitadas
        ):
            return True

        # BACKTRACKING: Retrocedemos si no funciona
        camino.pop()
        visitadas.remove(posicion)

    return False


def main():
    print("LABERINTO ORIGINAL")
    imprimir_laberinto(laberinto)

    inicio = buscar_inicio()

    if inicio is None:
        print("No se encontró el inicio.")
        return

    camino = [inicio]
    visitadas = {inicio}

    if resolver(inicio[0], inicio[1], 0, camino, visitadas):
        print("\n¡SOLUCIÓN ENCONTRADA!")
        print("Puntos obtenidos:", sum(
            laberinto[f][c]
            for f, c in camino
            if isinstance(laberinto[f][c], int)
        ))

        print("\nCamino recorrido (fila, columna):")
        print(" -> ".join(str(posicion) for posicion in camino))

        # Mostramos el camino sobre una copia del laberinto
        resultado = [fila[:] for fila in laberinto]

        for f, c in camino:
            if resultado[f][c] not in ('I', 'F'):
                resultado[f][c] = '*'

        print("\nLABERINTO CON EL CAMINO (*):")
        imprimir_laberinto(resultado)
    else:
        print("\nNo existe un camino válido con al menos",
              PUNTOS_MINIMOS, "puntos.")


if __name__ == "__main__":
    main()
