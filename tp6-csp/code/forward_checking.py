import tablero as tb
def forwardChecking(tablero, columna, dominios):
    size = len(tablero)
    estados_explorados = 0  # Contador de estados explorados

    if columna >= size:
        return tablero, 0, estados_explorados  # Retorna la solución con 0 conflictos
    
    for fila in dominios[columna][:]:
        estados_explorados += 1  # Incrementar el contador de estados explorados
        
        if tb.esValido(tablero, fila, columna):
            tablero[columna] = fila
            
            nuevoDominio = [list(d) for d in dominios]
            for col in range(columna + 1, size):
                if fila in nuevoDominio[col]:
                    nuevoDominio[col].remove(fila)
                diagonal1 = fila + (col - columna)
                diagonal2 = fila - (col - columna)
                if diagonal1 in nuevoDominio[col]:
                    nuevoDominio[col].remove(diagonal1)
                if diagonal2 in nuevoDominio[col]:
                    nuevoDominio[col].remove(diagonal2)
            
            solucion, c, e = forwardChecking(tablero, columna + 1, nuevoDominio)
            estados_explorados += e  # Sumar estados explorados de la llamada recursiva
            
            if solucion is not None:
                return solucion, c, estados_explorados
            
            tablero[columna] = -1
    
    return None, 1, estados_explorados  # Incrementar conflictos si no hay solución


def NReinasForwardChecking(size):
    tablero = [-1] * size
    dominios = [list(range(size)) for _ in range(size)]
    return forwardChecking(tablero, 0, dominios)