from ejercicio_02 import PokemonNoEncontrado


class Nodo:

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:

    def __init__(self):
        self.cabeza = None
        self.cantidad_elementos = 0

    def esta_vacia(self):
        return self.cabeza is None

    def tamanio(self):
        return self.cantidad_elementos

    def insertar_al_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        self.cantidad_elementos += 1

    def insertar_al_final(self, dato):
        nuevo = Nodo(dato)

        if self.esta_vacia():
            self.cabeza = nuevo
        else:
            actual = self.cabeza

            while actual.siguiente is not None:
                actual = actual.siguiente

            actual.siguiente = nuevo

        self.cantidad_elementos += 1

    def quitar_primero(self):
        if self.esta_vacia():
            return None

        dato = self.cabeza.dato
        self.cabeza = self.cabeza.siguiente
        self.cantidad_elementos -= 1

        return dato

    def eliminar(self, id):
        if self.esta_vacia():
            return False

        if self.cabeza.dato.id == id:
            self.quitar_primero()
            return True

        actual = self.cabeza

        while actual.siguiente is not None:

            if actual.siguiente.dato.id == id:
                actual.siguiente = actual.siguiente.siguiente
                self.cantidad_elementos -= 1
                return True

            actual = actual.siguiente

        return False

    def buscar(self, id):
        actual = self.cabeza

        while actual is not None:

            if actual.dato.id == id:
                return actual.dato

            actual = actual.siguiente

        return None

    def __iter__(self):
        actual = self.cabeza

        while actual is not None:
            yield actual.dato
            actual = actual.siguiente


class EquipoLlenoError(Exception):
    pass


class Equipo:

    def __init__(self):
        self.pokemones = ListaEnlazada()

    def agregar(self, pokemon):
        if self.cantidad() >= 6:
            raise EquipoLlenoError("El equipo esta lleno")

        self.pokemones.insertar_al_final(pokemon)

    def quitar(self, id):
        eliminado = self.pokemones.eliminar(id)

        if not eliminado:
            raise PokemonNoEncontrado("Pokemon no encontrado")

    def cantidad(self):
        return self.pokemones.tamanio()

    def __iter__(self):
        for pokemon in self.pokemones:
            yield pokemon


#Teoria
#En una lista enlazada simple la referencia al penultimo nodo esta guardada
# en el atributo siguiente del nodo anterior, para poder encontralo
# abria q recorrer toda la lista empezando desde la cabeza