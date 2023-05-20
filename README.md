# TDA-SOCIAL-NETWORK

El repositorio se divide en 4 directorios:

• databases
• matrix
• output
• src

El directorio databases contiene las bases de datos (en formato sql) utilizadas para la realización
de las pruebas y funcionalidad del código desarrollado. Este directorio no contiene la base de datos
original de la que se han extraído los datos debido al gran tamaño de la misma.

El directorio matrix contiene las matrices de adyacencia y distancia (en formato csv) creadas
tras el cálculo de las distancias entre usuarios. Estas matrices son utilizadas para el cálculo de la
persistencia y la similitud entre redes con el fin de ahorrar tiempo de cómputo.

El directorio output contiene los resultados y reports de las pruebas realizadas con el código
desarrollado. Aquí se encuentran los diagramas de barras y persistencia obtenidos tras el cálculo
de la persistencia y la similitud entre redes y otros resultados de interés.

Por último, el directorio src contiene el código fuente desarrollado. Este directorio se divide a su
vez en 4 subdirectorios:

• distance
• persistence
• similarity
• sql

Estos directorios funcionan como módulos de Python, por lo que se han de importar para hacer
uso de sus funciones.

El módulo distance es el encargado de calcular la distancia entre dos usuarios, así como el cálculo
de las matrices de adyacencia y distancia. También contiene la función que calcula los usuarios con
más actividad en la red.

El módulo persistence contiene las funciones encargadas del cálculo de la persistencia, así como
de imprimir los diagramas de barras y persistencia.

El módulo similarity contiene las funciones necesarias para el cálculo de similitud entre dos redes.

Por último, el módulo sql contiene las funciones encargadas de establecer una conexión con la base
de datos y obtener los resultados de las consultas.
