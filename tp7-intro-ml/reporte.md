# Introducción ML

## Ejercicio 1
- **(a)** En este caso, el método flexible sería el más adecuado debido a la gran cantidad de datos, esto permitirá que modele con mejor precisión las relaciones complejas debido a la gran cantidad de información.

- **(b)** En este caso, el método flexible seria peor ya que teniendo pocos datos y muchos predictores, nos puede llevar a un sobreajuste sobre estos datos y teniendo un peor rendimiento sobre nuevos datos. En su lugar, el inflexible tiene menor capacidad de ajustarse a detalles específicos pero tendrá mejor rendimiento sobre nuevos datos.

- **(c)** En este caso un método flexible será más adecuado ya que puede capturar estas relaciones no lineales (que son más complejas) con mayor eficiencia.

- **(d)** Si la varianza del error es alta, el modelo flexible tendrá peor rendimiento ya que podría sobreajustar el modelo, esto debido a que los métodos más flexibles tienden a tener una mayor varianza. Entonces podemos decir que el método inflexible será mejor en este caso ya que su varianza es mas baja.

## Ejercicio 2

- **(a)** En este caso tenemos un problema de **regresión** ya que nos estamos refiriendo a una variable cuantitativa , el salario del CEO. Además es un problema de **inferencia** ya que queremos saber la relación entre los predictores (Ganancias, Número de empleados, Industria) y el salario del CEO. n = 300 y p = 3.

- **(b)** En este caso tenemos un problema de **clasificación** ya que el resultado solo puede ser éxito o fracaso. Además es un problema de **predicción** ya que lo único que nos interesa es saber si el nuevo producto va a ser un éxito o fracaso. n = 20 y p = 13 (precio, presupuesto de marketing, precio de la competencia y otras 10 variables).

- **(c)** En este caso tenemos un problema de **regresión** ya que el cambio porcentual es una variable cuantitativa. Además es un problema de **predicción** ya que nos interesa predecir el cambio porcentual en la tasa de cambio USD/Euro basándonos en los cambios en los mercados de valores. n = 52 (semanas del año 2012) y p = 3 (Cambio en el mercado estadounidense,británico y alemán).

## Ejercicio 3

**Enfoque muy flexible:**

- **Ventajas**:

    - Un enfoque flexible se puede adaptar mejor cuando tenemos relaciones no lineas (relaciones más complejas) entre los predictores y las variables de respuesta.

    - Tenemos un menor sesgo ya que el modelo se ajusta mejor a los datos observados.

- **Desventajas**:

    - Mayor riesgo de sobreajuste (overfitting), ya que el modelo se puede ajustar muy bien en los datos de **entrenamiento** pero esto puede implicar un peor rendimiento en los datos de **prueba**.

    - Tenemos una mayor varianza ya que el modelo está sobreajustado con los datos de **entrenamiento**, lo cual hace que sea sensible a cambios en los datos de entrenamiento.

**¿Cuándo preferir uno sobre otro?**

- Más flexible: Se prefiere cuando los datos son abundantes y la relación entre predictores y la variable respuesta es muy no lineal o compleja, y cuando el objetivo es maximizar la precisión en los datos de **entrenamiento**.

- Menos flexible: Se prefiere cuando los datos son escasos o cuando se quiere un modelo más **interpretable** y general, incluso si esto implica una menor precisión. Es adecuado cuando se sabe que la relación entre los predictores y la respuesta es lineal.

## Ejercicio 4

El enfoque paramétrico asumen una forma específica para la función **f** que relaciona los predictores con la respuesta, por ejemplo, una relación lineal, en este caso nos enfocamos en estimar los parámetros, lo cual es sencillo pero tiene una desventaja, esta desventaja se puede dar en el caso de que hayamos asumido incorrectamente la forma de la función **f** que relaciona los predictores con la respuesta, lo cual nos llevaria a una predicción mucho menos precisa.

En el caso de los métodos con un enfoque no paramétrico NO asumimos la forma de la función **f**, en su lugar lo que hacemos es permitir que los datos nos conduzcan a un modelo que sea parecido a la función **f**, la ventaja de esto es que es bastante flexible ya que el modelo puede ajustarse a relaciones no lineales entre los predictores y las respuestas. La desventaja de este enfoque no paramétrico es que necesitamos una gran cantidad de datos para poder modelar correctamente la función **f** lo cual nos puede llevar también a un overfitting.

## Ejercicio 5

**A.** Distancia euclideana de X1=X2=X3=0 a las demás observaciones:

| Obs | Distancia euclideana |
| --- | ---------------------|
|  1  |         3            |
|  2  |         2            |
|  3  |        √10           |
|  4  |        √5            |
|  5  |        √2            |
|  6  |        √3            |

**B. Cuál es la predicción con K=1, ¿Por qué?**

Con K = 1 el vecino más cercano es la observación 5, por lo tanto la predicción será Green.

**C. Cuál es la predicción con K=3, ¿Por qué?**

Con K = 3 los vecinos más cercanos son la Obs 2 (Red), 5 (Green) y 6 (Red), entonces tenemos 2/3 que son Red y por lo tanto la predicción es Red.

**D. Si la frontera de decisión de Bayes en este problema es altamente no lineal, ¿esperaríamos que el mejor valor de K fuera grande o pequeño? ¿Por qué?**

Esperariamos un valor más chico para K ya que para valores de K muy grandes la frontera se comportaría de forma casi lineal. En cambio para valores más chicos se capturarían mejor las variaciones y tendería a ser no lineal.