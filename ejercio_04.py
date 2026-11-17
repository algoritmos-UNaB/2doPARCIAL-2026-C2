 # TEORÍA: En una lista enlazada simple, la referencia al penúltimo nodo no está guardada directamente
# en un atributo propio, sino en el atributo siguiente del nodo anterior (es decir, el antepenúltimo).
# Por eso, para encontrarlo hay que recorrer la lista desde la cabeza avanzando nodo por nodo hasta
# llegar al que cumple actual.siguiente.siguiente is None.


class PokemonNoEncontrado(Exception):
    pass


class EquipoLlenoError(Exception):
    pass


class Nodo:
    def _init_(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    def _init_(self):
        self.cabeza = None
        self._tamanio = 0

    def esta_vacia(self):
        return self.cabeza is None

    def tamanio(self):
        return self._tamanio

    def insertar_al_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        self._tamanio += 1

    def insertar_al_final(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self._tamanio += 1

    def quitar_primero(self):
        if self.esta_vacia():
            return None
        dato = self.cabeza.dato
        self.cabeza = self.cabeza.siguiente
        self._tamanio -= 1
        return dato

    def eliminar(self, id):
        anterior = None
        actual = self.cabeza
        while actual is not None:
            if actual.dato.id == id:
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                self._tamanio -= 1
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def buscar(self, id):
        actual = self.cabeza
        while actual is not None:
            if actual.dato.id == id:
                return actual.dato
            actual = actual.siguiente
        return None

    def _iter_(self):
        actual = self.cabeza
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente


class Equipo:
    MAX_POKEMONS = 6

    def _init_(self):
        self._pokemons = ListaEnlazada()

    def agregar(self, pokemon):
        if self._pokemons.tamanio() >= self.MAX_POKEMONS:
            raise EquipoLlenoError("El equipo ya tiene el máximo de 6 Pokémon.")
        self._pokemons.insertar_al_final(pokemon)

    def quitar(self, id):
        if not self._pokemons.eliminar(id):
            raise PokemonNoEncontrado(f"No se encontró el Pokémon con id {id} en el equipo.")

    def cantidad(self):
        return self._pokemons.tamanio()

    def _iter_(self):
        return iter(self._pokemons)