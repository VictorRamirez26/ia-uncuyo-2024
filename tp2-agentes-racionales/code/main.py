import agente as a
import agenteReflexivo as arf
import agenteRandom as arnm
import environment as e
import pandas as pd
import random
import matplotlib.pyplot as plt
import lib_analisis as la

# Definimos los tamaños y los porcentajes de suciedad
sizes = [2, 4, 8, 16, 32, 64, 128]
dirty_rates = [0.1, 0.2, 0.4, 0.8]

# Convierto los resultados a DataFrames de pandas
results = la.resultados_agentes(sizes,dirty_rates)
df_reflexivo = pd.DataFrame(results[0])
df_random = pd.DataFrame(results[1])

# Guardo los resultados en archivos Excel separados
df_reflexivo.to_excel('C:/Users/victo/Desktop/Inteligencia Artificial/tp2-agentes-racionales/code/agente_reflexivo_resultados.xlsx', index=False)
df_random.to_excel('C:/Users/victo/Desktop/Inteligencia Artificial/tp2-agentes-racionales/code/agente_random_resultados.xlsx', index=False)

print("Los archivos Excel han sido generados exitosamente.")


# Cargar los datos desde los archivos Excel
df_reflexivo = pd.read_excel('C:/Users/victo/Desktop/Inteligencia Artificial/tp2-agentes-racionales/code/agente_reflexivo_resultados.xlsx')
df_random = pd.read_excel('C:/Users/victo/Desktop/Inteligencia Artificial/tp2-agentes-racionales/code/agente_random_resultados.xlsx')



for size in sizes:
    resultados = la.performance_promedio(df_reflexivo, df_random, f'{size}x{size}', dirty_rates)
    
    plt.plot(dirty_rates, resultados[0], label='Agente Reflexivo', marker='o', linestyle='--')
    plt.plot(dirty_rates, resultados[1], label='Agente Random', marker='o', linestyle='--')
    
    plt.title(f'Comparación de Performance para entorno {size}x{size}')
    plt.xlabel('Porcentaje de suciedad')
    plt.ylabel('Performance promedio')
    plt.legend()
    plt.grid(True)
    
    # Muestra el gráfico para el tamaño actual
    plt.show()
