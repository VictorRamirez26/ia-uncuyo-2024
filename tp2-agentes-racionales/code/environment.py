import random
class Environment:
    def __init__(self,sizeX,sizeY,dirty_rate):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.dirty = round(sizeX*sizeY*dirty_rate) # Número de casillas sucias
        self.grid = self.create_grid() # Creo la tabla con todos ceros
        self.dirty_grid() # LLeno de suciedad casillas random
    
    def create_grid(self):
        # Crea una matriz (lista de listas) llena de ceros
        return [[0 for _ in range(self.sizeY)] for _ in range(self.sizeX)]

    def dirty_grid(self):
        for _ in range(self.dirty):
            pos_x = random.randint(0, self.sizeX - 1)
            pos_y = random.randint(0, self.sizeY - 1)
            self.grid[pos_x][pos_y] = 1  # Marco la casilla como sucia 
    

    def is_dirty(self, posX, posY):
        if self.grid[posX][posY] == 1:
            return True
        
    def get_dirty(self):
        return self.dirty
        
    def print_environment(self):
        # Imprimo la matriz (entorno)
        for row in self.grid:
            print(" ".join(str(cell) for cell in row))
         
    def acceptAction(self, action, x, y):
        # Posibles movimientos
        moves = {
            "Arriba": (1, 0),
            "Abajo": (-1, 0),
            "Derecha": (0, 1),
            "Izquierda": (0, -1)
        }
        
        if action in moves:
            movX, movY = moves[action] 
            new_x, new_y = x + movX, y + movY
            
            # Verifico que no me salga de la matriz
            return (0 <= new_x < self.sizeX) and (0 <= new_y < self.sizeY)
        
        elif action == "Limpiar":
            if self.is_dirty(x, y):
                self.grid[x][y] = 0
                self.dirty -= 1
                return True
            return False
        
        return False   

