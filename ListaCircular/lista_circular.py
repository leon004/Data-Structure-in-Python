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
        while aux:
            print(aux.dato)
            aux = aux.siguiente
            if aux == self.primero:
                break

    def RemoverInicio(self):
        if self.Vacia():
            print("Lista vacia")
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            self.primero = self.primero.siguiente
            self.ultimo.siguiente = self.primero

    def RemoverFinal(self):
        if self.Vacia():
            print("Lista Vacia")
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            aux = self.primero
            while aux.siguiente != self.ultimo:
                aux = aux.siguiente
            aux.siguiente = self.primero
            self.ultimo = aux