"""
Lista Doblemente Enlazada
Una lista doblemente enlazada es una lisata enlazada de nodos, donde cada nodo tien
un para de campos de enlace, uno al nodo siguiente, y al otro al anterior.

Caracteristicas:

1.- Recorrer la estructura en ambos sentidos, de inicio a fin y de fin a inicio
2.- Borrado mas simple de datos
3.- Estructura dinamica
"""
from lista_doblemente_enlazada import ListaDoblementeEnlazada

lista = ListaDoblementeEnlazada()

lista.agregar_final(12)
lista.agregar_final(56)
lista.agregar_final(21)
lista.agregar_final(10)
lista.agregar_final(11)
lista.recorrer_inicio()