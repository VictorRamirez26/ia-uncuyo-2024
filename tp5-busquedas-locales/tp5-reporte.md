# Introducción
Se implementaron tres algoritmos de búsqueda local para abordar el problema de las N-reinas y comparar los resultados de cada algoritmo. Los algoritmos implementados fueron:
- **Hill Climbing**
- **Simulated Annealing**
- **Genetic Algorithm**

Para el problema de las N-reinas se tomaron tableros de tamaños 4, 8, 10, 12, 15.

# Marco Teórico 
Para el desarrollo de los algoritmos, se utilizó una representación del tablero mediante una lista, donde cada elemento corresponde a la posición de una reina en su respectiva columna. Por ejemplo, la lista [1, 2, 1, 0] indica que la reina de la columna 0 se encuentra en la fila 1, la reina de la columna 1 está en la fila 2, la reina de la columna 2 también está en la fila 1, y la reina de la columna 3 está en la fila 0.

Al inicio de cada algoritmo, se generó aleatoriamente un tablero, el cual se utilizó como punto de partida en el caso de los algoritmos Hill Climbing y Simulated Annealing.

En el caso del primer algoritmo, Hill Climbing, se parte de una solución generada aleatoriamente y se generan soluciones vecinas al mover una reina dentro de su columna. A continuación, el algoritmo examina estas soluciones vecinas y selecciona aquella que presenta la mejor función objetivo, que en este contexto corresponde al número mínimo de pares de reinas que se amenazan mutuamente.

El segundo algoritmo, Simulated Annealing, es similar al Hill Climbing, pero introduce la posibilidad de aceptar soluciones peores que la actual con una cierta probabilidad, lo que permite explorar el espacio de soluciones de manera más amplia.

Con respecto al algoritmo genético, se generó una cantidad determinada de tableros, que constituyeron la población inicial. A partir de esta población, se seleccionaron los mejores individuos mediante un método de torneo. Posteriormente, se llevó a cabo la reproducción de estos padres a través de un proceso de cruza, que incluye una probabilidad de mutación para introducir variaciones en la nueva generación.

# Diseño Experimental

### Información sobre el Algoritmo Hill Climbing

- **Generación de Vecinos**: El algoritmo genera vecinos para una tabla de reinas al cambiar la posición de una reina en cada columna. Para cada columna, se crean nuevos estados (tablas) al mover la reina a todas las filas posibles, excepto a su posición actual.

- **Evaluación de Vecinos**: Se evalúan todos los vecinos generados y se calcula el número de conflictos (reinas atacándose entre sí) para cada uno. Esto se hace mediante la función `checkConflicts`, que cuenta los pares de reinas en conflicto.

- **Selección del Mejor Vecino**: El algoritmo identifica el vecino con el menor número de conflictos. Si hay varios vecinos que comparten el mismo número mínimo de conflictos, uno de ellos se selecciona aleatoriamente como el mejor vecino.

### Información sobre el Algoritmo Simulated Annealing

- **Tabla Inicial**: El algoritmo comienza con una tabla inicial (tablero) que representa la disposición de las reinas.

- **Temperatura Inicial**: La temperatura inicial se establece en 1000, lo que permite explorar una amplia gama de soluciones al principio del proceso.

- **Tasa de Enfriamiento**: Se utiliza una tasa de enfriamiento del 90% (0.90), lo que significa que la temperatura se reduce en un 10% después de cada iteración. Esto afecta la probabilidad de aceptar movimientos que incrementan los conflictos.

- **Máximo de Iteraciones**: Se permite un máximo de 1000 iteraciones para la búsqueda de soluciones, proporcionando un límite al tiempo de ejecución del algoritmo.

- **Selección de Vecinos**: En cada iteración, se generan todos los vecinos posibles de la tabla actual. Se selecciona uno aleatoriamente para considerar como el próximo estado.

- **Criterio de Aceptación**: El algoritmo acepta el siguiente estado bajo dos condiciones:
  - Si el estado vecino tiene menos conflictos que el estado actual, se acepta.
  - Si el estado vecino tiene más conflictos, se acepta con una probabilidad determinada por la función de Boltzmann, que depende de la diferencia de conflictos y de la temperatura actual.

- **Historial de Conflictos**: Se mantiene un registro del número de conflictos de reinas a lo largo de las iteraciones para evaluar el progreso del algoritmo hacia una solución óptima.

### Información sobre el Algoritmo Genético

- **Población Inicial**: Dependiendo del tamaño del tablero (n), se establece un número variable de individuos en la población inicial:
  - Para \( n = 4 \): 20 individuos
  - Para \( n = 8 \): 100 individuos
  - Para \( n = 10 \): 150 individuos
  - Para \( n = 12 \): 200 individuos
  - Para \( n = 15 \): 250 individuos

- **Método de Selección por Torneo**: Se seleccionan padres utilizando un torneo con una cantidad de participantes definida por la partición, la cual se determina en función del tamaño del tablero. Por ejemplo, para \( n = 4 \) se utiliza una partición de 4, mientras que para \( n = 15 \) se usa 25.

- **Cruzamiento**: Se implementa un cruzamiento de un punto entre los padres seleccionados para generar nuevos hijos. La elección del punto de cruzamiento se realiza de manera aleatoria, asegurando que al menos un elemento de cada padre esté presente en los hijos.

- **Mutación**: La probabilidad de mutación está fijada en un 5% (0.05). Durante la mutación, se selecciona aleatoriamente una columna y se cambia la fila de la reina en esa columna.

- **Generaciones**: El algoritmo tiene un límite de 1000 generaciones para encontrar una solución óptima. En cada generación, se evalúa el fitness de los hijos generados, que se calcula como el número total de pares de reinas que no se atacan. Si se alcanza el máximo fitness posible (que es \((n \ (n - 1)) / 2\)), se considera que se ha encontrado una solución.

### Criterios de Finalización y Resultados

- **Condición de Parada**: Los algoritmos se detienen si se encuentra un estado sin conflictos (es decir, un estado óptimo donde ninguna reina ataca a otra) o si se alcanza el máximo de iteraciones/generaciones permitidas.

- **Resultados**: El algoritmo devuelve la mejor tabla encontrada, el número de conflictos en esa tabla, el número de movimientos realizados y el historial de conflictos a lo largo de la ejecución.

# Análisis y Discusión de Resultados

### Tiempos de Ejecución

Se generaron gráficos de caja que ilustran el tiempo de ejecución de cada algoritmo para diferentes tamaños de tablero. Además, se elaboró un boxplot que presenta los resultados de las 30 iteraciones realizadas para cada tamaño.

![Imagen 1](/images/Tiempos/hill_climbing_tiempos.png)
![Imagen 2](/images/Tiempos/simulated_annealing_tiempos.png)
![Imagen 3](/images/Tiempos/genetico_tiempos.png)

Al comparar el rendimiento del algoritmo Hill Climbing con el Simulated Annealing en términos de tiempo de ejecución, se observa que Hill Climbing tiene un desempeño ligeramente superior, especialmente en tableros de menor tamaño. 

Por otro lado, el Genetic Algorithm se destaca como el que requiere más tiempo para encontrar una solución, independientemente del tamaño del tablero analizado.


### Cantidad de Estados Explorados

Se generaron gráficos de caja que reflejan la cantidad de estados explorados por cada algoritmo, considerando todos los tamaños de tablero. Estos gráficos muestran el número de estados recorridos hasta encontrar una solución o alcanzar el límite de iteraciones.

![Imagen 4](/images/Movimientos/hill_climbing_movimientos.png)
![Imagen 5](/images/Movimientos/simulated_annealing_movimientos.png)
![Imagen 6](/images/Movimientos/genetico_movimientos.png)

Al comparar Hill Climbing con Simulated Annealing en términos de estados explorados, se observa que Hill Climbing recorre una menor cantidad de estados independientemente del tamaño del tablero. Esto se debe, en gran parte, a que Simulated Annealing incluye una probabilidad de moverse a un estado peor, lo cual ayuda a evitar caer en máximos locales.

Por otro lado, el Genetic Algorithm es el que requiere más movimientos para encontrar una solución, debido a las operaciones de cruce entre padres y la probabilidad de mutación en cada generación.

### Evolución de Reinas Atacadas

A continuación, analizaremos cómo se comporta cada algoritmo en la búsqueda de una solución. Para ello, tomaremos una muestra de ejecuciones con un tamaño de tablero de 10 y observaremos la evolución de los pares de reinas en conflicto en cada iteración.

![Imagen 7](/images/Funcion%20H/h_hill_climbing.png)
![Imagen 8](/images/Funcion%20H/h_simulated_annealing.png)
![Imagen 9](/images/Funcion%20H/h_genetic_algorithm.png)

Como se observa en el gráfico, Hill Climbing presenta una disminución continua en el número de reinas en conflicto, ya que el algoritmo siempre se mueve hacia estados con menos conflictos. Sin embargo, en este caso, se quedó atrapado en un máximo local y no logró alcanzar la solución.

Por su parte, Simulated Annealing muestra una gran variación al inicio debido a su mayor probabilidad de moverse a estados con más conflictos al principio. Esta probabilidad disminuye a medida que el algoritmo avanza, permitiendo que se explore más ampliamente al inicio y se refine en las últimas iteraciones. En esta muestra, Simulated Annealing sí encontró la solución.

En el caso de Genetic Algorithm, la cantidad de reinas en conflicto se mantiene casi constante a lo largo de las generaciones debido a la estrategia de selección por torneos que se implementó. Sin embargo, este algoritmo no alcanzó la solución en el límite de 1000 generaciones. Sin esta restricción y la probabilidad de mutación, podría eventualmente encontrarla. Esto contrasta con Hill Climbing, que podría quedarse atascado en un máximo local sin importar la cantidad de iteraciones.

### Porcentaje de Soluciones Encontradas

A continuación, se analiza el porcentaje de éxito de cada algoritmo en encontrar la solución óptima, es decir, un estado donde no haya ningún par de reinas atacándose entre sí.

![Imagen 10](/images/Porcentajes/porcentajes_hill_climbing.png)
![Imagen 11](/images/Porcentajes/porcentajes_simulated_annealing.png)
![Imagen 12](/images/Porcentajes/porcentajes_genetic_algorithm.png)

Como se observa, Hill Climbing tiene una baja probabilidad de encontrar la solución óptima, y esta probabilidad disminuye a medida que aumenta el tamaño del tablero. Por el contrario, Simulated Annealing y Genetic Algorithm presentan una alta probabilidad de éxito en tableros pequeños; sin embargo, esta probabilidad también disminuye en tableros de mayor tamaño. Aun así, ambos algoritmos tienen una probabilidad significativamente mayor de alcanzar la solución óptima en comparación con Hill Climbing. Esto se debe a la capacidad de exploración que ofrece la probabilidad de mutación en el caso de Genetic Algorithm y la posibilidad de aceptar estados peores al inicio en Simulated Annealing, lo que ayuda a evitar quedar atrapados en óptimos locales.

# Conclusión

Al comparar los tres algoritmos Hill Climbing, Simulated Annealing y Genetic Algorithm en términos de rendimiento, se observan diferencias significativas en sus tiempos de ejecución, probabilidad de encontrar la solución óptima y la cantidad de estados explorados.

Hill Climbing muestra una ventaja en la cantidad de estados explorados, recorriendo menos estados que Simulated Annealing y Genetic Algorithm. Esto lo convierte en una opción rápida y eficiente en términos de tiempo para tableros pequeños, pero sufre de una alta probabilidad de quedarse atrapado en máximos locales, lo cual reduce su probabilidad de alcanzar la solución óptima en tableros grandes. Este comportamiento se refleja en su baja probabilidad de éxito en encontrar una configuración sin conflictos cuando el tamaño del tablero aumenta.

Por otro lado, Simulated Annealing presenta una mayor probabilidad de encontrar soluciones óptimas en tableros grandes en comparación con Hill Climbing, gracias a su capacidad de aceptar temporalmente estados peores. Este enfoque le permite escapar de máximos locales, aunque a costa de un mayor número de estados explorados y una variabilidad mayor en sus tiempos de ejecución, particularmente en tableros de mayor tamaño.

Genetic Algorithm, aunque tiene el tiempo de ejecución más largo y recorre la mayor cantidad de estados debido a la recombinación y mutación, ofrece una alta probabilidad de éxito en tableros pequeños y medianos. Sin embargo, su eficiencia disminuye considerablemente en tableros más grandes debido a la complejidad de su proceso de búsqueda en múltiples generaciones.

En conclusión, si el objetivo es minimizar el tiempo y la cantidad de estados explorados en tableros pequeños, Hill Climbing es la mejor opción. Para tableros más grandes o en aplicaciones donde es fundamental maximizar la probabilidad de encontrar la solución óptima, Simulated Annealing y Genetic Algorithm son opciones más sólidas, con una ventaja particular para Simulated Annealing debido a su capacidad de manejar estados subóptimos temporalmente.
