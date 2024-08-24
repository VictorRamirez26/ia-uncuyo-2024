# Comparación Agente Reflexivo Simple vs Agente Random
## Introducción 
En el presente informe se realizó una comparación del rendimiento del agente reflexivo simple vs agente random, esta comparación se realizo con las siguientes características:
- **Entornos**: 2x2, 4x4, 8x8, 16x16, 32x32, 64x64, 128x128
- **Porcentajes de suciedad**: 0.1, 0.2, 0.4, 0.8

Se realizaron un total de 10 pruebas para cada combinación de entorno-suciedad y ambos agentes trabajaron sobre el mismo entorno generado aleatoriamente en cada caso.

## Marco Teórico
Para la realización del ejercicio se utilizaron entornos con las siguientes características:
- Se generan las casillas con suciedad de forma aleatoria.
- La suciedad no se regenera una vez limpiada.
- Los agentes comienzan en un casillero aleatorio del entorno.

Los agentes se dividen en dos tipos:
- **Agente random o aleatorio**: Este tipo de agente realiza una acción de manera aleatoria, sin verificar si el casillero donde se encuentra esta sucio.
- **Agente reflexivo simple**: Similar al agente aleatorio, pero tiene un sensor que le indica si la casilla donde se encuentra esta sucia o no. En caso de estar sucia realiza la acción de limpiar, sino, se mueve de forma aleatoria.

Estos agentes pueden realizar las siguientes acciones:
- Moverse en 4 direcciones (Arriba,Abajo,Izquierda,Derecha).
- Quedarse quieto.
- Limpiar una casilla.
- Utilizar el sensor (Solo el Agente reflexivo simple).

Solo puede realizar un total de 1000 acciones.

## Diseño experimental

Se realizaron experimentos para evaluar el rendimiento de los dos agentes en entornos de distintos tamaños  y con diferentes porcentajes de suciedad. Se probaron todas las combinaciones posibles de tamaño y suciedad, y ambos agentes fueron evaluados 10 veces en cada combinación, asegurando que se realizaran las evaluaciones en los mismos entornos.

El rendimiento de cada agente se evaluó según la cantidad de celdas limpiadas y, en caso de completar la limpieza del entorno, se registró también la cantidad de acciones realizadas. Los experimentos se llevaron a cabo en **Python**, utilizando clases para representar los entornos y los agentes. Los resultados fueron almacenados en un archivo Excel y se generaron gráficos para su análisis empleando librerías como **matplotlib**, **seaborn** y **pandas**.


