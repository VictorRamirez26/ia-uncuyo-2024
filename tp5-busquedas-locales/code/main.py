import time
import math
import tablero
import pandas as pd
import hill_climbing as hc
import lib_analisis as la

# Lista de tamaños de tableros para probar
tamaños = [4, 8, 10, 12, 15]

# Ejecutar la prueba con 30 iteraciones para cada tamaño y guardar en Excel
resultados = la.testHillClimbingForDifferentSizes(tamaños, 30)

# Crear un DataFrame con los resultados
df = pd.DataFrame(resultados)

# Guardar los resultados en un archivo Excel
df.to_excel("hill_climbing_results.xlsx", index=False)
print(f"\nResultados guardados en hill_climbing_results.xlsx")
la.boxplot_tiempos(df)
la.boxplot_movimientos(df)