import gymnasium as gym
import map as map
import random
import algorithms as algo
import lib_analisis as la
import pandas as pd
import time

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

def init_algorithms():
    # Inicializar listas para almacenar resultados
    results = []

    # Realizar 30 simulaciones
    for simulation in range(30):
        # Generar seed aleatoria
        seed = random.randint(0, 1_000_000_000)
        print(f"Simulación {simulation + 1}, Seed: {seed}")
        random.seed(seed)

        # Crear el entorno, la posición inicial del agente y el objetivo
        size = 100
        p_hole = 0.08
        start = (random.randint(0, size - 1), random.randint(0, size - 1))
        end = (random.randint(0, size - 1), random.randint(0, size - 1))
        e = map.Map(size, p_hole, start, end)

        # Diccionario para almacenar resultados por simulación
        simul_result = {
            "seed": seed
        }

        # Aplicar los algoritmos
        for algo_name, algorithm in {
            "BFS": algo.Algorithm.bfs,
            "DFS": algo.Algorithm.dfs,
            "DLS": lambda g, s, e: algo.Algorithm.dfs_limited(g, s, e, 100),
            "UCS E1": algo.Algorithm.ucs_c1,
            "UCS E2": algo.Algorithm.ucs_c2,
            "A star": algo.Algorithm.a_star,
        }.items():
            # Medir el tiempo de ejecución
            start_time = time.time()
            
            # Ejecutar el algoritmo
            steps, num_states = algorithm(e.grid, e.start, e.end)
            
            # Medir el tiempo final
            end_time = time.time()
            
            # Calcular el tiempo de ejecución
            execution_time = end_time - start_time

            # Calcular el costo
            cost_1, cost_2 = la.calculate_cost(steps)
            
            # Comprobar si se encontró la solución
            found_solution = e.end in steps if steps else False
            
            
            # Guardar resultados
            simul_result["algorithm"] = algo_name
            simul_result["num_states"] = num_states
            simul_result["cost_e1"] = cost_1
            simul_result["cost_e2"] = cost_2
            simul_result["found_solution"] = found_solution
            simul_result["execution_time"] = execution_time  # Agregar el tiempo de ejecución

            # Agregar el resultado de esta simulación a la lista
            results.append(simul_result.copy())

    return results