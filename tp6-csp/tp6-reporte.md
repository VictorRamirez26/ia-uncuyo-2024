## Ejercicio 1

### Variables:
- Conjunto de variables: X<sub>i,j</sub> tal que i,j indican la fila y columna respectivamente y sus valores varian entre 1 y 9. En total hay 81 variables.

### Dominio:
- Conjunto: Las variables X<sub>i,j</sub> pueden tomar los valores {1,2,3,4,5,6,7,8,9} para cada celda, o en el caso de un sudoku parcialmente completado, la variable de la celda tomará el valor completado.

### Restricciones:

- Filas: Cada fila debe contener los números del 1 al 9 sin repetirse.

- Columnas: Cada columna debe contener los números del 1 al 9 sin repetirse.

- Subcuadrícula: Cada subcuadrícula de 3x3 debe tener los valores del 1 al 9 sin repetirse.

## Ejercicio 2

Utilizaremos el algoritmo AC-3 para detectar la inconsistencia con la asignación parcial WA = Red , V = Blue. Es decir que cuando lleguemos a un punto en el que tengamos una variable X<sub>i</sub> con dominio vacío, no tendremos solución para esta asignación parcial.

*Nota*: Se asignará R = Red , G = Green y B = Blue.

Dominio inicial del problema:
- D(WA) = {R}
- D(NT) = {R,B,G}
- D(SA) = {R,B,G}
- D(Q) = {R,B,G}
- D(NSW) = {R,B,G}
- D(V) = {B}
Una posible ordenación de los arcos para este ejemplo es:
Q = {(SA->WA), (SA->V), (NT->SA), (NSW->V), (NSW->SA), (Q->NSW), (Q->SA), (NT->Q), (NT->WA)}

Algoritmo:
1. SA->WA : Elimino R del dominio SA, D(SA) = {B,G}
2. SA->V : Elimino B del dominio SA, D(SA) = {G}
3. NT->SA : Elimino G de NT, D(NT) = {R,B}
4. NSW->V : Elimino B de NSW, D(NSW) = {R,G}
5. NSW->SA : Elimino G de NSW, D(NSW) = {R}
6. Q->NSW : Elimino R de Q, D(Q) = {B,G}
7. Q->SA : Elimino G de Q, D(Q) = {B}
8. NT->Q : Elimino B de NT, D(NT) = {R}
9. NT->WA : Elimino R de NT, D(NT) = { }

Como NT no tiene mas valores en su dominio, podemos concluir que para esta asignación parcial no tenemos solución.

## Ejercicio 3
La complejidad en el peor de los casos en un grafo con estructura de árbol es O(E*D), donde E es el número de aristas y D tamaño de dominio más grande. Esto se debe a que ningún arco será considerado más de una vez.

## Ejercicio 4

Vamos a poder lograrlo en **O(n² ⋅ d²)** si tenemos en cuenta lo siguiente:

1. Para cada valor en el dominio de X<sub>k</sub> llevamos una cuenta de cuántos valores en el dominio de X<sub>i</sub> 
son consistentes con ese valor de X<sub>k</sub>.

2. Cada vez que se elimina un valor de X<sub>i</sub> se reduce el contador correspondiente en X<sub>k</sub>. Si en algún momento el contador para un valor de X<sub>k</sub> llega a cero, ese valor debe ser eliminado, ya que no tiene ningun valor consistente en X<sub>i</sub>.

3. Para cada arco (X<sub>k</sub>,X<sub>i</sub>), en el peor de los casos, vamos a necesitar verificar todos los valores en el dominio de X<sub>k</sub> y de X<sub>i</sub>. Esto toma **O(d²)** por arco, y hay **O(n²)** arcos en el peor de los casos (grafo completo), lo que resulta en un coste total de **O(n² ⋅ d²)** para el pre-cálculo.

## Ejercicio 5

### Demostrar la correctitud del algoritmo CSP para ´arboles estructurados

La 2-consistencia nos dice que para cada par de variables X<sub>i</sub> , X<sub>j</sub> conectadas por una restricción, entonces para cada valor del dominio de X<sub>i</sub> existe al menos un valor en el dominio X<sub>j</sub> que satisface la restricción entre estos.

En un árbol, la propiedad que nos interesa es que no tiene ciclos. Esto significa que una vez que asignamos valores a las variables no vamos a tener caminos "cíclicos" que nos provoquen una inconsistencia. Entonces, una vez que una variable sea consistente con su vecino (nodo hijo), esa consistencia no se verá afectada por la asignaciones posteriores. 

Entonces, para demostrar la n-consistencia en un árbol vamos a elegir un nodo "raíz" y vamos a realizar un recorrido hacia abajo, aplicando la 2-consistencia en cada nodo, lo que garantiza que para cualquier valor asignado a una variable, existe al menos un valor compatible en sus nodos hijos. Como el grafo no tiene ciclos, no necesitamos preocuparnos de que las asignaciones en otros subárboles interfieran con las consistencias previamente establecidas. Esto implica que la 2-consistencia es **suficiente** para garantizar la n-consistencia en un CSP basado en árboles.
