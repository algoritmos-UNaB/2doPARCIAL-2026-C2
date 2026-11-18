from ejercicio_02 import PokemonNoEncontrado

class EquipoLlenoError(Exception):
    pass


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        

    def esta_vacia(self):
        return self.cabeza == None
    
    def tamanio(self):
        actual = self.cabeza
        contador = 0
        while actual is not None:
            contador += 1
            actual = actual.siguiente
        return contador

    def insertar_al_inicio(self,dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def insertar_al_final(self,dato):
        nuevo = Nodo(dato)

        if self.esta_vacia():
            self.cabeza = nuevo 
            return

        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente

        actual.siguiente = nuevo 

    def quitar_primero(self):
        actual = self.cabeza
        self.cabeza = self.cabeza.siguiente
        return actual.dato

    def buscar(self, id):
        actual = self.cabeza

        while actual is not None:
            if id == actual.dato.id:
                return actual.dato
            else:
                actual = actual.siguiente
        
        return None
    
    def __iter__(self):
        actual = self.cabeza
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente

    def eliminar(self, id):
        actual = self.cabeza
        anterior = None

        while actual is not None:
            if actual.dato.id == id:

                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                return True

            anterior = actual
            actual = actual.siguiente

        return False

class Equipo:

    def __iter__(self):
        return iter(self.lista)

    def __init__(self):
        self.lista = ListaEnlazada()
    def cantidad(self):
        return self.lista.tamanio()
    def agregar(self, pokemon):
        if self.cantidad() == 6:
            raise EquipoLlenoError("Equipo lleno")
        
        self.lista.insertar_al_final(pokemon)
    
    def quitar(self, id):
        resultado = self.lista.eliminar(id)
        if resultado is False:
            raise PokemonNoEncontrado("Pokemon no encontrado")
#  TEORIA
#  La referencia al penultimo esta en el siguiente del nodo anterior a el. los nodos no tienen referencia hacia atras por eso empezamos desde cabeza y sus siguientes