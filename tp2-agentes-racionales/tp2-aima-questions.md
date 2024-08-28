## 2.10 Considera una versión modificada del entorno de la aspiradora en el Ejercicio 2.8, en la cual al agente se le penaliza con un punto por cada movimiento.

### A. ¿Puede un agente reflexivo simple ser perfectamente racional en este entorno?

No, no puede ser racional ya que no maximizaria su medida de desempeño debido a la penalización, el agente solo puede detectar si su casillero actual esta limpio o no, pero no su alrededor, por lo tanto seguiria moviendose innecesariamente haciendo que se aplique la penalización.

### B. ¿Qué pasa con un agente reflexivo con estado?

En el caso que guardemos el estado, por ejemplo de las casillas visitadas o del movimiento anterior, el agente no seria racional, pero si tendría un mejor desempeño. Ejemplo: [S,L] supongamos que empezamos en el casillero que está sucio (S), el agente luego de limpiar el casillero se moveria a la derecha, el cual está limpio (L), es decir que el agente hizo un movimiento innecesario y por lo tanto aplicaría la penalización, haciendo que no maximice su medida de desempeño pero haciendo que se detenga ya que no tiene más casilleros por visitar, esto lo hace más eficiente que el agente 2.10.A pero no lo convierte en un agente racional.

### C. ¿Cómo cambian tus respuestas a las partes a y b si las percepciones del agente le dan el estado limpio/sucio de cada casilla en el entorno?

En este caso, el agente si sería racional ya que evitaría movimientos innecesarios. Ejemplo [S,L] supongamos que el agente comienza en el casillero sucio (S), luego de limpiar este casillero el agente se quedaría quieto ya que sabe que el casillero de la derecha esta limpio y si se mueve no ganaría ningún punto por limpiar pero si le aplicaría la penalización.

## 2.11 Considera una versión modificada del entorno de la aspiradora en el Ejercicio 2.8, en la cual la geografía del entorno—su extensión, límites y obstáculos—es desconocida, al igual que la configuración inicial de suciedad. (El agente puede moverse hacia arriba y hacia abajo, así como a la izquierda y a la derecha.)

### A. ¿Puede un agente reflexivo simple ser perfectamente racional en este entorno? Explica.

No, al no saber su entorno el agente no puede optimizar sus movimientos para minimizar las penalizaciones.

### B. ¿Puede un agente reflexivo simple con una función de agente aleatorizada superar a un agente reflexivo simple? Diseña tal agente y mide su rendimiento en varios entornos.

Como observamos en puntos anteriores de este tp, el agente con función aleatoria puede llegar a tener el mismo rendimiento que el agente reflexivo simple, pero en entornos con mayor tamaño el agente aleatorio tiene un peor rendimiento que el agente reflexivo simple.

### C. ¿Puedes diseñar un entorno en el que tu agente aleatorizado tenga un mal rendimiento? Muestra tus resultados.

Cualquier entorno mas grande que 8x8 nos muestra que el agente aleatorizado tiene un mal rendimiento frente al agente reflexivo simple.

### D. ¿Puede un agente reflexivo con estado superar a un agente reflexivo simple? Diseña tal agente y mide su rendimiento en varios entornos. ¿Puedes diseñar un agente racional de este tipo?

Si, un agente reflexivo con estado puede superarlo ya que puede recordar los casilleros que ya ha visitado. Sin embargo no se podria diseñar un agente racional ya que sigue desconociendo su entorno.
