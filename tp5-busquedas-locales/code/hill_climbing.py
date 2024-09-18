import tablero
import random
def generateNeighBors(column , table , neighbors):
    # Genero los vecinos para una columna en particular
    current_row = table[column]
    for row in range(len(table)):
        if (row != current_row):
            new_table = table.copy()
            new_table[column] = row
            neighbors.append(new_table)
    return neighbors

def generateAllNeighbors(table):
    # Genero los vecinos para todas las columnas
    size = len(table)
    neighbors = []
    for column in range(size):
        generateNeighBors(column,table,neighbors)
    return neighbors


def findBestNeighbord(table):

    neighbors = generateAllNeighbors(table)
    min_conflicts = sum(tablero.checkConflicts(table))
    best_neighbors = [table]

    for neighbor in neighbors:
        conflicts = sum(tablero.checkConflicts(neighbor))
        if conflicts < min_conflicts:
            best_neighbors = [neighbor]
            min_conflicts = conflicts
        elif conflicts == min_conflicts:
            best_neighbors.append(neighbor)

    # Elijo el vecino de manera aleatoria entre los mejores
    best_neighbor = random.choice(best_neighbors)
    return best_neighbor, min_conflicts

def hillClimbing(table):

    best_neighbor, min_conflicts = findBestNeighbord(table)
    moves = 1
    while min_conflicts > 0 and moves < 1000:
        best_neighbor, min_conflicts = findBestNeighbord(best_neighbor)
        moves += 1
    
    return best_neighbor , min_conflicts , moves