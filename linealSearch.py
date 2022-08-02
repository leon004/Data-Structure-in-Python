"""
Busqueda lineal: 
Funcionamiento: 
1.- Recorrer cada elemento de la lista
2.- Ir comparando el elemento que se desea buscar con cada elemento de la lista
3.- En caso de ser encontrado, retornar el indice en el que se encuentra en caso de retornar, false or None
"""

def busquedaLineal(dato): 
    for x in range(len(list)):
        if list[x] == dato:
            return x
    return None

def buscar(dato):
    if busquedaLineal(dato) == None:
        return "El dato %d no se encuentra"%(dato)
    else:
        return "El dato %d se encuentra en el indice: %d"%(dato, busquedaLineal(dato))





list = [12,45,78,9,6,5,4,3,]
 
for i in range(len(list)):
    print("[%d] => [%d]"%(i, list[i]))
print(buscar(78))