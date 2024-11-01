import pandas as pd
import algorithms as algo
import plot_utils as utils
import random


# Lista de tamaños de tableros para probar
sizes = [4, 8, 10, 12, 15]
iterations = 30
# Descomentar esta linea para generar nuevos resultados
"""
# Ejecutar la prueba con 30 iteraciones para cada tamaño y guardar en Excel
seed = 1436123
tableros = utils.PlotUtils.generarTableros(sizes , iterations)

results1 = utils.PlotUtils.generateResults(tableros,algo.hillClimbing)
results2 = utils.PlotUtils.generateResults(tableros,algo.simulatedAnnealing)
results3 = utils.PlotUtils.generateResults(tableros,algo.geneticAlgorithm)
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

"""
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

size = 10
num_muestra = random.randrange(0,30)
utils.PlotUtils.h_function(df1 , size , "Hill Climbing" , 2)
utils.PlotUtils.h_function(df2 , size , "Simulated Annealing" , 2)
utils.PlotUtils.h_function(df3 , size , "Genetic Algorithm", 2)


# Calculo el porcentaje de veces que el algoritmo encontró una solución con 0 reinas atacandose
percentages_list_df1 = utils.PlotUtils.calculate_solution_percentage_by_size(df1, sizes , iterations)
percentages_list_df2 = utils.PlotUtils.calculate_solution_percentage_by_size(df2, sizes , iterations)
percentages_list_df3 = utils.PlotUtils.calculate_solution_percentage_by_size(df3, sizes , iterations)

# Gráfico de barras que nos muestra el porcentaje de veces que se encontró la solución de acuerdo al tamaño
utils.PlotUtils.plot_percentage_by_sizes(sizes, percentages_list_df1, "Hill Climbing")
utils.PlotUtils.plot_percentage_by_sizes(sizes, percentages_list_df2, "Simulated Annealing")
utils.PlotUtils.plot_percentage_by_sizes(sizes, percentages_list_df3, "Genetic Algorithm")
