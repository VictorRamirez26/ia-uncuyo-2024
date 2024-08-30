import gymnasium as gym
import map as map

e = map.Map(100,0.08) # (size , p_hole)
env = e.env # Me quedo con el entorno

# Información sobre el entorno
print("Número de estados:", env.observation_space.n)
print("Número de acciones:", env.action_space.n)

# Inicializar el entorno y obtener el estado inicial
state = env.reset()
print("Posición inicial del agente:", state[0])

# Simulación
done = truncated = False
step_count = 0
while not (done or truncated):
    action = env.action_space.sample()  # Acción aleatoria
    next_state, reward, done, truncated, _ = env.step(action)
    print(f"Paso {step_count}: Acción: {action}, Nuevo estado: {next_state}, Recompensa: {reward}")
    print(f"¿Ganó? (encontró el objetivo): {done}")
    print(f"¿Frenó? (alcanzó el máximo de pasos posible): {truncated}\n")
    state = next_state
    step_count += 1

# Cerrar el entorno al finalizar
env.close()
