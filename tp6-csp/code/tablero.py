import random
def generarTablero(size):
    
    table = []
    for _ in range(size):
        row = random.randint(0,size-1)
        table.append(row)
    return table

def printTablero(table):
    size = len(table)
    
    # Recorre cada fila
    for row in range(size):
        line = ""
        # Recorre cada columna
        for col in range(size):
            if table[col] == row:
                line += "Q "  # Representa una reina
            else:
                line += ". "  # Representa un espacio vacío
        print(line)
    print("\n")

def esValido(tablero, fila, columna):
    # Verificar que no haya otra reina en la misma fila
    for i in range(columna):
        if tablero[i] == fila:
            return False
    
    # Verificar las diagonales
    for i in range(columna):
        if abs(tablero[i] - fila) == abs(i - columna):
            return False
    
    return True