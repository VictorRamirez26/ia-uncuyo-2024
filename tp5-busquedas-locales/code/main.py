import pandas as pd
import algorithms as algo
import plot_utils as utils
import random
# Lista de tamaños de tableros para probar
sizes = [4, 8, 10, 12, 15]

# Descomentar esta linea para generar nuevos resultados
"""
# Ejecutar la prueba con 30 iteraciones para cada tamaño y guardar en Excel
seed = random.randint(0,100000000)
random.seed(seed)
results1 = utils.PlotUtils.generateResults(sizes,30,algo.hillClimbing)
random.seed(seed)
results2 = utils.PlotUtils.generateResults(sizes,30,algo.simulatedAnnealing)
results3 = utils.PlotUtils.generateResults(sizes,30,algo.geneticAlgorithm)
# Crear un DataFrame con los resultados
df1 = pd.DataFrame(results1)
df2 = pd.DataFrame(results2)
df3 = pd.DataFrame(results3)

# Guardar los resultados en un archivo Excel
df1.to_excel("hill_climbing_results.xlsx", index=False)
print(f"\nResultados guardados en hill_climbing_results.xlsx")

df2.to_excel("simulated_annealing_results.xlsx", index=False)
print(f"\nResultados guardados en simulated_annealing_results.xlsx")

df3.to_excel("genetic_algorithm_results.xlsx", index=False)
print(f"\nResultados guardados en genetic_algorithm_results.xlsx")

"""
# Si ya tengo los resultados los leo, sino descomentar lo de arriba
df1 = pd.read_excel("hill_climbing_results.xlsx")
df2 = pd.read_excel("simulated_annealing_results.xlsx")
df3 = pd.read_excel("genetic_algorithm_results.xlsx")


# Gráficos Hill climbing
utils.PlotUtils.boxplot(df1,"Tamaño del tablero","Tiempo (segundos)", "Hill Climbing")
utils.PlotUtils.boxplot(df1,"Tamaño del tablero","Cantidad de Movimientos", 
                            "Hill Climbing")

# Gráficos Simulated Anneling
utils.PlotUtils.boxplot(df2,"Tamaño del tablero","Tiempo (segundos)", "Simulated Annealing")
utils.PlotUtils.boxplot(df2,"Tamaño del tablero","Cantidad de Movimientos", 
                            "Simulated Annealing")

                            
# Gráficos Algoritmo Genético
utils.PlotUtils.boxplot(df3,"Tamaño del tablero","Tiempo (segundos)", "Genetic Algorithm")
utils.PlotUtils.boxplot(df3,"Tamaño del tablero","Cantidad de Movimientos", 
                            "Genetic Algorithm")

"""

df3_filtrado = utils.PlotUtils.filtrarTableroSinConflictos(df3,10)
length_ejeX = df3_filtrado["Cantidad de Movimientos"]
ejeX = []
for i in range(length_ejeX):
    ejeX.append(i)

print(type(df3_filtrado))  # Debe ser <class 'pandas.core.frame.DataFrame'>


#utils.PlotUtils.lineChart(ejeX, df3_filtrado["Historial de reinas amenazadas"],
                        #  "Iteraciones", "Par de reinas atacadas", "", "Historial de reinas amenazadas")
"""