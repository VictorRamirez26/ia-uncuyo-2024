import gymnasium as gym
import map as map
import random
import algorithms as algo
import lib_analisis as la
import pandas as pd

"""
seed = random.randint(0, 1_000_000_000)
size = 100
p_hole = 0.08
start = (random.randint(0, size - 1), random.randint(0, size - 1))
end = (random.randint(0, size - 1), random.randint(0, size - 1))
e = map.Map(size, p_hole, start, end)
env = e.env  # Me quedo con el entorno
path , states = algo.Algorithm.a_star(e.grid , start,end)
print(f"{la.calculate_cost(path)} , cantidad de estados: {states}" )
"""

# Crear un DataFrame de los resultados
df = pd.DataFrame(la.init_algorithms())

# Guardar los resultados en un archivo Excel
df.to_excel("simulation_results.xlsx", index=False)

print("Simulaciones completadas y resultados guardados en simulation_results.xlsx")


# Recrear el escenario del entorno
#la.iniciarEnv(env , steps_bfs)
#la.iniciarEnv(env , steps_dfs)
#la.iniciarEnv(env , steps_dls)
#la.iniciarEnv(env,steps_ucs_e2)

