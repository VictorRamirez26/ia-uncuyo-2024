import matplotlib.pyplot as plt
import seaborn as sns
import tablero 
import time
import algorithms as algo
import pandas as pd
class PlotUtils:

    @staticmethod
    def generateResults(sizes,iterations, algorithm):
        # Crear una lista para almacenar los resultados
        resultados = []

        for size in sizes:
            print(f"\nProbando con un tablero de {size} reinas: ")

            # Variables para estadísticas
            for i in range(iterations):
                # Generar el tablero inicial
                tablero_inicial = tablero.generarTablero(size)
                
                # Medir tiempo de ejecución
                start_time = time.time()
                
                # Aplicar Algoritmo
                if (algorithm is not algo.geneticAlgorithm):
                    solucion, conflictos, moves , h_e_list = algorithm(tablero_inicial)
                else:
                    solucion, conflictos, moves , h_e_list = algorithm(size)
                
                # Medir tiempo final de ejecución
                end_time = time.time()
                tiempo_ejecucion = end_time - start_time
                
                # Almacenar resultados en la lista
                resultados.append({
                    "Tamaño del tablero": size,
                    "Tablero solución": solucion,
                    "Número de conflicos": conflictos,
                    "Cantidad de Movimientos": moves,
                    "Tiempo (segundos)": tiempo_ejecucion,
                    "Historial de reinas amenazadas": h_e_list
                })
        
        return resultados

    @staticmethod 
    def lineChart(ejeX, ejeY, labelX:str, labelY:str, legend_str:str, title:str):

        # Eje x: Porcentaje de suciedad 0.1, 0.2 , 0.4 , etc
        # Eje y: Performance promedio de los 10 intentos
        # Se calcula para cada tipo de entorno
        
        plt.plot(ejeX, ejeY, label=legend_str, marker='o', linestyle='--')
        
        plt.title(title)
        plt.xlabel(labelX)
        plt.ylabel(labelY)
        plt.legend()
        plt.grid(True)
        
        # Muestra el gráfico para el tamaño actual
        plt.show()


    @staticmethod
    def boxplot(dataframe, ejeX:str, ejeY:str, title:str,):
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=ejeX, y=ejeY, data=dataframe)
        plt.title(title)
        plt.xlabel(ejeX)
        plt.ylabel(ejeY)
        plt.show()

    @staticmethod
    def filtrarTableroSinConflictos(dataframe, size):

        # Filtrar por tamaño del tablero y número de conflictos igual a 0
        filtro = (dataframe["Tamaño del tablero"] == size) & (dataframe["Número de conflicos"] == 0)
        tablero_sin_conflictos = dataframe[filtro]

        # Devolver solo el primer resultado, si hay más de uno
        if not tablero_sin_conflictos.empty:
            return tablero_sin_conflictos.iloc[0]  # Selecciona la primera fila
        else:
            return None