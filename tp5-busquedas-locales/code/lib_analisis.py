import time
import math
import tablero
import hill_climbing as hc
import matplotlib.pyplot as plt
import seaborn as sns

def calcular_desviacion_estandar(valores, promedio):
    """Calcula la desviación estándar de una lista de valores."""
    suma_diferencias = sum((x - promedio) ** 2 for x in valores)
    varianza = suma_diferencias / len(valores)
    return math.sqrt(varianza)

def testHillClimbingForDifferentSizes(sizes, iterations):
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
            
            # Aplicar Hill Climbing
            solucion, conflictos, moves = hc.hillClimbing(tablero_inicial)
            
            # Medir tiempo final de ejecución
            end_time = time.time()
            tiempo_ejecucion = end_time - start_time
            
            # Almacenar resultados en la lista
            resultados.append({
                "Tamaño del tablero": size,
                "Movimientos": moves,
                "Tiempo (segundos)": tiempo_ejecucion
            })
    
    return resultados


def boxplot_tiempos(df):
    """
    Genera un gráfico de cajas y extensiones (boxplot) de los tiempos de ejecución
    para cada tamaño de tablero.
    """
    plt.figure(figsize=(10, 6))
    sns.boxplot(x="Tamaño del tablero", y="Tiempo (segundos)", data=df)
    plt.title("Gráfico de Cajas y Extensiones de Tiempos de Ejecución")
    plt.xlabel("Tamaño del Tablero")
    plt.ylabel("Tiempo de Ejecución (segundos)")
    plt.show()

def boxplot_movimientos(df):
    """
    Genera un gráfico de cajas y extensiones (boxplot) de la cantidad de movimientos
    para encontrar el óptimo en cada tamaño de tablero.
    """
    plt.figure(figsize=(10, 6))
    sns.boxplot(x="Tamaño del tablero", y="Movimientos", data=df)
    plt.title("Gráfico de Cajas y Extensiones de Movimientos")
    plt.xlabel("Tamaño del Tablero")
    plt.ylabel("Cantidad de Movimientos")
    plt.show()
