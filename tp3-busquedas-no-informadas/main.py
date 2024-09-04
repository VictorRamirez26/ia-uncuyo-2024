import gymnasium as gym
import map as map
import random
import algorithms as algo
import lib_analisis as la
# Algunos buenas seeds: 394375604 , 740166210 , 363178760 , 652117772 , 970737619, 158555495, 272572490, 23123578
seed = 652117772
print(seed)
random.seed(seed)

# Creo el entorno, la posicion inicial del agente y el objetivo
size = 30
p_hole = 0.08
start = (random.randint(0,size-1),random.randint(0,size-1))
end = (random.randint(0,size-1),random.randint(0,size-1))
e = map.Map(size, p_hole, start , end)  
env = e.env  # Me quedo con el entorno

# Aplico los algoritmos
steps_bfs = algo.Algorithm.bfs(e.grid, e.start, e.end)
#steps_dfs = algo.Algorithm.dfs(e.grid, e.start, e.end)
#steps_dls = algo.Algorithm.dfs_limited(e.grid, e.start, e.end,100)
#steps_ucs_e1 = algo.Algorithm.ucs_c1(e.grid, e.start, e.end)
steps_ucs_e2 = algo.Algorithm.ucs_c2(e.grid, e.start, e.end)

print(la.calculate_cost(steps_bfs))
#print(la.calculate_cost(steps_dfs))
#print(la.calculate_cost(steps_dls))
#print(la.calculate_cost(steps_ucs_e1))
print(la.calculate_cost(steps_ucs_e2))


# Información sobre el entorno
print("Número de estados:", env.observation_space.n)
print("Número de acciones:", env.action_space.n)

# Inicializar el entorno y obtener el estado inicial
state = env.reset()
print("Posición inicial del agente:", state[0])


#la.iniciarEnv(env , steps_bfs)
#la.iniciarEnv(env , steps_dfs)
#la.iniciarEnv(env , steps_dls)
#la.iniciarEnv(env,steps_ucs_e2)

