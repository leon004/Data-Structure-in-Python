"""
Nodo: 
En programacion, concretamene en estructuras de datos, un nodo es uno de los elementos
de una lista enlazada, de un arbol o de un grafo, Cada nodo es una estructura o registro que dispondra de varios campos
Y al menos uno de esos campos sera un puntero o referencia a otro nodo, de forma que, conocido un nodo, a partir de esa referencia
sera posible en teoria tener acceso a otros nodos de la estructura

"""

#Ejercicio: Crear una funcion para insertar un nodo en un arbol binario de busqueda

class Nodo:
    def __init__(self, dato):
        self.izquierda = None
        self.derecha = None
        self.dato = dato

    def insertar(raiz, nodo):
        if raiz  is None:
            raiz = nodo
        else:
            if raiz.dato < nodo.dato:
                if raiz.derecha is None:
                    raiz.derecha = nodo
                else: 
                    insertar(raiz.derecha, nodo)
            else: 
                if raiz.izquierda is None:
                    raiz.izquierda = nodo
                else:
                    insertar(raiz.izquierda, nodo)
        