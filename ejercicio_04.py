from ejercicio_02 import PokemonNoEncontrado

class EquipoLlenoError(Exception):
    pass

class Nodo:
    def _init_(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def _init_(self):
        self.primero = None
        self._tamanio = 0

    def esta_vacia(self):
        return self.primero is None

    def tamanio(self):
        return self._tamanio

    def insertar_al_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.primero
        self.primero = nuevo
        self._tamanio += 1

    def insertar_al_final(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self.primero = nuevo
        else:
            actual = self.primero
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self._tamanio += 1

    def quitar_primero(self):
        if self.esta_vacia():
            raise Exception("La lista está vacía.")
        dato = self.primero.dato
        self.primero = self.primero.siguiente
        self._tamanio -= 1
        return dato

    def eliminar(self, id):
        actual = self.primero
        anterior = None
        while actual is not None:
            if actual.dato.id == id:
                if anterior is None:
                    self.primero = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                self._tamanio -= 1
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def buscar(self, id):
        actual = self.primero
        while actual is not None:
            if actual.dato.id == id:
                return actual.dato
            actual = actual.siguiente
        return None

    def _iter_(self):
        actual = self.primero
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente

class Equipo:
    def _init_(self):
        self.pokemones = ListaEnlazada()

    def agregar(self, pokemon):
        if self.cantidad() >= 6:
            raise EquipoLlenoError("El equipo ya cuenta con 6 Pokémon.")
        self.pokemones.insertar_al_final(pokemon)

    def quitar(self, id):
        if not self.pokemones.eliminar(id):
            raise PokemonNoEncontrado(f"El id {id} no está en el equipo.")

    def cantidad(self):
        return self.pokemones.tamanio()

    def _iter_(self):
        return iter(self.pokemones)

# TEORIA
# En una lista enlazada simple, la referencia al penúltimo no está guardada de forma explícita; se la encuentra iterando nodo por nodo desde el principio hasta hallar que el 'siguiente.siguiente' sea None.