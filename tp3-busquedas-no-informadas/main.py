import gymnasium as gym
import map as map
import random
import algorithms as algo
# Algunos buenas seeds: 394375604 , 740166210 , 363178760 , 652117772 , 970737619, 158555495, 272572490
seed = 740166210
print(seed)
random.seed(seed)

size = 20
p_hole = 0.08
start = (random.randint(0,size-1),random.randint(0,size-1))
end = (random.randint(0,size-1),random.randint(0,size-1))

e = map.Map(size, p_hole, start , end)  
env = e.env  # Me quedo con el entorno
steps = algo.Algorithm.bfs(e.grid, e.start, e.end)
#steps = algo.Algorithm.dfs(e.grid, e.start, e.end)

# Información sobre el entorno
print("Número de estados:", env.observation_space.n)
print("Número de acciones:", env.action_space.n)

# Inicializar el entorno y obtener el estado inicial
state = env.reset()
print("Posición inicial del agente:", state[0])

# Diccionario para traducir movimientos a acciones en el entorno
direction_to_action = {
    (0, -1): 0,  # Izquierda
    (1, 0): 1,   # Abajo
    (0, 1): 2,   # Derecha
    (-1, 0): 3  # Arriba
}

# Simulación usando steps
done = truncated = False
step_count = 0

for i in range(len(steps) - 1):
    current_pos = steps[i]
    next_pos = steps[i + 1]
    # Calcular la dirección del movimiento (Izq,Abajo,Derecha,Arriba)
    move = (next_pos[0] - current_pos[0], next_pos[1] - current_pos[1])
    # Obtener la acción correspondiente
    action = direction_to_action.get(move)
    
    if action is not None:
        next_state, reward, done, truncated, _ = env.step(action)
        print(f"Paso {step_count}: Acción: {action}, Nuevo estado: {next_state}, Recompensa: {reward}")
        print(f"¿Ganó? (encontró el objetivo): {done}")
        print(f"¿Frenó? (alcanzó el máximo de pasos posible): {truncated}\n")
        state = next_state
        step_count += 1
        
    if done or truncated:
        break

# Cerrar el entorno al finalizar
env.close()
