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

def busqueda_binaria(dato):
    izquierda = 0
    derecha = len(lista)-1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if dato == lista[medio]:
            return medio
        elif dato < lista[medio]:
            derecha = medio - 1
        else:
            izquierda = medio + 1
    return None

def buscar(dato):
    if busqueda_binaria == None:
        return "El dato % no se encuentra"%(dato)
    else:
        return "El dato %d se encuentra en el indice: %d"%(dato, busqueda_binaria(dato))

lista = [5, 12, 15, 30, 50, 65, 70, 87, 88, 96]

print(buscar(12))