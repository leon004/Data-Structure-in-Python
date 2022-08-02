""" 
Busqueda Binaria 
Funcionamiento: 
Buscar datos en una coleccion de datos 
Ventajas: Realiza menos comparaciones que el metodo de Busqueda Lineal

Requisitos antes de analizar el Algoritmo:
Tener la lista ordenada de manera ascendente (Menor a mayor)

Algoritmo: 
1.- Calcular el punto medio, (izquierda + derecha)/2
2.- Comparar el punto medio con el dato a buscar
3.- Si es igual al dato al punto medio, retornar indice
4.- Si el dato a buscar es mayor que el punto medio, izquierda es igual al valor medio + 1
5.- Si el dato a buscar es menor que el punto medio, derecha es igual al valor medio - 1 
6.- Se sigue ejecutando siempre y cuando izquierda sea menor o igual a derecha
"""