from ejercicio_02 import PokemonNoEncontrado


class EquipoLlenoError(Exception):
    pass


class Nodo:

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:

    def __init__(self):
        self._primero = None
        self._ultimo = None
        self._tamanio = 0

    def esta_vacia(self):
        return self._primero is None

    def tamanio(self):
        return self._tamanio

    def insertar_al_final(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self._primero = nuevo
        else:
            self._ultimo.siguiente = nuevo
        self._ultimo = nuevo
        self._tamanio += 1

    def insertar_al_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self._primero
        self._primero = nuevo
        if self._ultimo is None:
            self._ultimo = nuevo
        self._tamanio += 1

    def quitar_primero(self):
        if self.esta_vacia():
            raise IndexError("Lista vacía")
        nodo = self._primero
        self._primero = nodo.siguiente
        if self._primero is None:
            self._ultimo = None
        self._tamanio -= 1
        return nodo.dato

    def eliminar(self, id):
        anterior = None
        actual = self._primero
        while actual is not None and actual.dato.id != id:
            anterior = actual
            actual = actual.siguiente
        if actual is None:
            return False
        if anterior is None:
            self._primero = actual.siguiente
        else:
            anterior.siguiente = actual.siguiente
        if actual is self._ultimo:
            self._ultimo = anterior
        self._tamanio -= 1
        return True

    def buscar(self, id):
        for dato in self:
            if dato.id == id:
                return dato
        return None

    def __iter__(self):
        actual = self._primero
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente


class Equipo:

    MAXIMO = 6

    def __init__(self):
        self._lista = ListaEnlazada()

    def agregar(self, pokemon):
        if self._lista.tamanio() == Equipo.MAXIMO:
            raise EquipoLlenoError("El equipo ya tiene 6")
        self._lista.insertar_al_final(pokemon)

    def quitar(self, id):
        if not self._lista.eliminar(id):
            raise PokemonNoEncontrado(f"El id {id} no está en el equipo")

    def cantidad(self):
        return self._lista.tamanio()

    def __iter__(self):
        return iter(self._lista)


# TEORIA
# La información está en el siguiente del antepenúltimo nodo.
# Para encontrarla, hay que recorrer la lista desde el primer nodo
# hasta llegar al penúltimo, ya que los nodos solo apuntan hacia adelante.