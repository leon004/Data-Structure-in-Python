"""
Lista circula doblemente enlazada
En una lista enlazada doblemente circular, cada nodo tiene dos enlaces,
similares a los de la lista doblemnente en;azda excepto que el enlace anterior del
primer nodo apunta al ultimo y el enlacee siguiente del ultimo nodo, apunta al primero

"""
from lista_circular_doble_enlazada import ListaCircularDobleEnlazada

lista = ListaCircularDobleEnlazada()

lista.agregar_final(12)
lista.agregar_final(45)
lista.agregar_final(18)
lista.agregar_final(36)
lista.agregar_final(10)
lista.eliminar_ultimo()
lista.recorrer_inicio_a_fin()
print("*" * 25)
lista.recorrer_fin_a_inicio()

