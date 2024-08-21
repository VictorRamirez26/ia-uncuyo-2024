import agente as a
import agenteReflexivo as ar
import environment as e
import pandas as pd

# Definimos los tamaños y los porcentajes de suciedad
sizes = [2, 4, 8, 16, 32, 64, 128]
dirty_rates = [0.1, 0.2, 0.4, 0.8]

# Lista para almacenar los resultados
results = []

# Bucle para cada combinación de tamaño y porcentaje de suciedad
for size in sizes:
    for rate in dirty_rates:
        for _ in range(10):  # Repetimos 10 veces cada combinación
            entorno = e.Environment(size, size, rate)
            agenteReflexivo = ar.AgenteReflexivo(entorno)
            result = agenteReflexivo.think()  # Tupla con (performance , necessaryMoves)
            
            # Agregamos el resultado a la lista
            results.append({
                'Size': f'{size}x{size}',
                'Dirty Rate': rate,
                'Performance': result[0],
                'Necessary Moves': result[1]
            })

# Convierto los resultados a un DataFrame de pandas
df = pd.DataFrame(results)

# Guardo los resultados en un archivo Excel
df.to_excel('C:/Users/victo/Desktop/Inteligencia Artificial/tp2-agentes-racionales/code/agente_reflexivo_resultados.xlsx', index=False)


print("El archivo Excel ha sido generado exitosamente.")
