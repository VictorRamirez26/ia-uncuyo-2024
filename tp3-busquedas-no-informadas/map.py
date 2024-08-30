import gymnasium as gym
import numpy as np

class Map():
    def __init__(self, size , p_hole):
        self.size = size 
        self.p_hole = p_hole
        custom_map = self.generate_custom_map(size,p_hole)
        self.env = gym.make('FrozenLake-v1', desc=custom_map, is_slippery=False, render_mode='human')
        self.env = gym.wrappers.TimeLimit(self.env, max_episode_steps=1000) # Máximo 1000 acciones

    def generate_custom_map(self, size, p_hole):
        """
        size: Tamaño del mapa (por ejemplo, 100 para un mapa de 100x100)
        p_hole: Probabilidad de que una celda sea un agujero (valor entre 0 y 1)
        
        return: Lista de cadenas que representan el mapa
        """
        map_array = np.random.choice(['F', 'H'], size=(size, size), p=[1 - p_hole, p_hole])
        
        # Asegurar que la posición inicial y la meta no sean agujeros
        map_array[0, 0] = 'S'
        map_array[-1, -1] = 'G'
        
        # Convierto el mapa a la lista de cadenas que requiere FrozenLake
        return [''.join(row) for row in map_array]