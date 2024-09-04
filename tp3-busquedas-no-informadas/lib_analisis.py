

def iniciarEnv(env, steps):

    if steps is None:
        return 
    
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

        if i == 1000:
            print(f"¿Frenó? (alcanzó el máximo de pasos posible): {truncated}\n")
            break

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
            step_count += 1
            
        if done:
            break

    # Cerrar el entorno al finalizar
    env.close()

def calculate_cost(path):
    """
    Calcula el costo del camino según las especificaciones dadas.

    path: Lista de tuplas que representan el camino desde el inicio al objetivo.

    return: 
        - Costo con todas las direcciones con valor 1.
        - Costo con izquierda = 1, abajo = 2, derecha = 3 y arriba = 4.
    """

    if path is None: 
        return 0,0
    
    # Direcciones de movimiento con su respectivo costo
    direction_to_cost = {
        (0, -1): 1,  # Izquierda
        (1, 0): 2,   # Abajo
        (0, 1): 3,   # Derecha
        (-1, 0): 4   # Arriba
    }

    cost_uniform = len(path)-1  # Costo donde todas las direcciones valen 1
    cost_weighted = 0  # Costo según el valor de la dirección

    for i in range(len(path) - 1):
        current_pos = path[i]
        next_pos = path[i + 1]
        # Calcular la dirección del movimiento
        move = (next_pos[0] - current_pos[0], next_pos[1] - current_pos[1])

        # Sumar el costo para el movimiento actual
        cost_weighted += direction_to_cost.get(move, 0)  # Costo específico de la dirección

    return cost_uniform, cost_weighted
