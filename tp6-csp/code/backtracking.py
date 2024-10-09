import tablero as tb

def resolverNReinasBacktracking(tablero, columna):
    size = len(tablero)
    estados_explorados = 0  # Contador de estados explorados
    
    if columna >= size:
        return tablero, 0, estados_explorados  # Retorna la solución con 0 conflictos
    
    for fila in range(size):
        estados_explorados += 1  # Incrementar el contador de estados explorados
        
        if tb.esValido(tablero, fila, columna):
            tablero[columna] = fila
            
            solucion, c, e = resolverNReinasBacktracking(tablero, columna + 1)
            estados_explorados += e  # Sumar estados explorados de la llamada recursiva
            
            if solucion is not None:
                return solucion, c, estados_explorados
            
            tablero[columna] = -1
    
    return None, 1, estados_explorados  # Incrementar conflictos si no hay solución


def NReinasBacktracking(size):
    tablero = [-1] * size  # Inicializa el tablero vacío
    return resolverNReinasBacktracking(tablero, 0)