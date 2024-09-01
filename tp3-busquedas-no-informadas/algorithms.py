import gymnasium as gym
import numpy as np
from collections import deque
import random

class Algorithm():
    @staticmethod
    def bfs(grid, start, goal):
        """ 
        grid: La matriz del entorno (custom_map)
        start: Tupla (x, y) de la posición inicial ('S')
        goal: Tupla (x, y) de la posición del objetivo ('G')
        
        return: Lista de tuplas que representan el camino desde el inicio al objetivo o None si no hay camino.
        """
        # Direcciones de movimiento: izquierda, abajo, derecha, arriba
        directions = [(0,-1), (1,0), (0,1), (-1,0)]

        # Cola de la forma: (current , path) donde path lleva una lista del camino recorrido
        queue = deque([(start, [start])])
        
        # Posiciones visitadas
        visited = set([start])
        
        while queue:
            (current, path) = queue.popleft()
            
            if current == goal:
                return path  # Devuelvo el camino desde S hasta G
            
            # Exploro los vecinos moviendome en las 4 direcciones
            for direction in directions:
                neighbor = (current[0] + direction[0], current[1] + direction[1])
                
                if (0 <= neighbor[0] < len(grid)) and (0 <= neighbor[1] < len(grid[0])):  # Verificar límites
                    # Me fijo q no sea un agujero y que no haya pasado por este camino
                    if neighbor not in visited and grid[neighbor[0]][neighbor[1]] in ('F', 'G'): 
                        queue.append((neighbor, path + [neighbor]))
                        visited.add(neighbor)
        
        return path  # No hay camino al objetivo
    
    @staticmethod 

    def dfs(grid, start, goal):
        """ 
        grid: La matriz del entorno (custom_map)
        start: Tupla (x, y) de la posición inicial ('S')
        goal: Tupla (x, y) de la posición del objetivo ('G')
        
        return: Lista de tuplas que representan el camino desde el inicio al objetivo o None si no hay camino.
        """
        # Direcciones de movimiento: izquierda, abajo, derecha, arriba
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

        # Pila para DFS: (current, path) donde path lleva una lista del camino recorrido
        stack = [(start, [start])]
        
        # Posiciones visitadas
        visited = set([start])
        
        while stack:
            current, path = stack.pop()
            
            if current == goal:
                return path  # Devuelvo el camino desde S hasta G
            
            # Exploro los vecinos moviéndome en las 4 direcciones pero en orden inverso asi explora en profunidad por izquierda primero
            for direction in reversed(directions):
                neighbor = (current[0] + direction[0], current[1] + direction[1])
                
                if (0 <= neighbor[0] < len(grid)) and (0 <= neighbor[1] < len(grid[0])):  # Verificar límites
                    # Me fijo que no sea un agujero y que no haya pasado por este camino
                    if neighbor not in visited and grid[neighbor[0]][neighbor[1]] in ('F', 'G'):
                        stack.append((neighbor, path + [neighbor]))
                        visited.add(neighbor)
        
        return path  # No hay camino al objetivo

