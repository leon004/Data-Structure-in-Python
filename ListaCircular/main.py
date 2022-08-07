"""
Lista Circular Simple

Es una lsita en la que cada nodo tiene un enlace, similar al de las listas enlazadas simples, excepto que el siguiente nodo del ultimo
apunta al primero 
Como en una lista enlazada simple los nuevos nodos pueden ser solo eficientemente insertados despues de uno ya que tengamos referenciado
Caracteristicas:
1.- Permite accesos al primer nodo desde el puntero del ultimo nodo.
"""

from lista_circular import ListaCircular

lista = ListaCircular()

lista.AgregarFinal(10)
lista.AgregarFinal(56)
lista.AgregarFinal(78)
lista.AgregarFinal(90)

lista.Recorrer()