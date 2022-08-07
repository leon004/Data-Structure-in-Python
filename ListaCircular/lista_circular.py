from nodo import Nodo


class ListaCircular():
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def Vacia(self): 
        return self.primero == None
    
    def AgregarInicio(self,dato):
        if self.Vacia():
            self.primero = self.ultimo = Nodo(dato)
            self.ultimo.siguiente = self.primero
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero = aux
            self.ultimo.siguiente = self.primero
    
    def AgregarFinal(self,dato):
        if self.Vacia():
            self.primero = self.ultimo = Nodo(dato)
            self.ultimo.siguiente = self.primero
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.siguiente = self.primero

    def Recorrer(self):
        aux = self.primero
        while aux.siguiente != self.primero:
            print(aux.dato)
            aux = aux.siguiente
        print(aux.dato)