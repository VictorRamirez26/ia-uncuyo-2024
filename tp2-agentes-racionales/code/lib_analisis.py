import agente as a
import agenteReflexivo as arf
import agenteRandom as arnm
import environment as e
import pandas as pd
import random
import matplotlib.pyplot as plt

def resultados_agentes(sizes,dirty_rates):
    # Lista para almacenar los resultados del agente reflexivo
    results_reflexivo = []

    # Lista para almacenar los resultados del agente random
    results_random = []

    # Bucle para cada combinación de tamaño y porcentaje de suciedad
    for size in sizes:
        for rate in dirty_rates:
            for _ in range(10):  
                # Generar y guardar una semilla aleatoria
                seed = random.randint(0, 1000000)
                
                # Usar la semilla para el agente reflexivo
                random.seed(seed)  # Seteo la semilla
                entorno_reflexivo = e.Environment(size, size, rate)
                agenteReflexivo = arf.AgenteReflexivo(entorno_reflexivo)
                result_reflexivo = agenteReflexivo.think()  # Tupla con (performance , necessaryMoves)
                results_reflexivo.append({
                    'Size': f'{size}x{size}',
                    'Dirty Rate': rate,
                    'Performance': result_reflexivo[0],
                    'Necessary Moves': result_reflexivo[1]
                })
                
                # Usar la misma semilla para el agente random
                random.seed(seed)  # Reseteo la semilla para asegurar el mismo entorno
                entorno_random = e.Environment(size, size, rate)
                agenteRandom = arnm.AgenteRandom(entorno_random)
                result_random = agenteRandom.think()  # Tupla con (performance , necessaryMoves)
                results_random.append({
                    'Size': f'{size}x{size}',
                    'Dirty Rate': rate,
                    'Performance': result_random[0],
                    'Necessary Moves': result_random[1]
                })
    return results_reflexivo,results_random




def performance_promedio(df_1 , df_2 , size , dirty_rates):
    # Guardan el promedio de los 10 intentos
    promedios_1 = []
    promedios_2 = []

    # Guardamos el promedio para todos los porcentajes de suciedad
    for rate in dirty_rates:
        df_1_filtered = df_1[(df_1['Size'] == size) & (df_1['Dirty Rate'] == rate)]
        df_2_filtered = df_2[(df_2['Size'] == size) & (df_2['Dirty Rate'] == rate)]

        y_1 = df_1_filtered['Performance']
        y_2 = df_2_filtered['Performance']

        promedio_1 = sum(y_1)/len(y_1)
        promedio_2 = sum(y_2)/len(y_2)

        promedios_1.append(promedio_1)
        promedios_2.append(promedio_2)
    
    return promedios_1,promedios_2