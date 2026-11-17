"""Ejercicio 4. Nodos, lista enlazada y playlist sin tope."""

if __package__:
    from .ejercicio_02 import CancionNoEncontradaError
else:
    from ejercicio_02 import CancionNoEncontradaError


class ListaVaciaError(Exception):
    """Se intento quitar el primer dato de una lista vacia."""


class Nodo:
    def __init__(self, dato, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente


class ListaEnlazada:
    def __init__(self):
        self._cabeza = None
        self._tamanio = 0

    def esta_vacia(self) -> bool:
        return self._cabeza is None

    def tamanio(self) -> int:
        return self._tamanio

    def insertar_al_inicio(self, dato):
        self._cabeza = Nodo(dato, self._cabeza)
        self._tamanio += 1
        return dato

    def insertar_al_final(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self._cabeza = nuevo
        else:
            actual = self._cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self._tamanio += 1
        return dato

    def quitar_primero(self):
        if self.esta_vacia():
            raise ListaVaciaError("No se puede quitar un dato de una lista vacia.")
        dato = self._cabeza.dato
        self._cabeza = self._cabeza.siguiente
        self._tamanio -= 1
        return dato

    def __iter__(self):
        actual = self._cabeza
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente


class Playlist:
    def __init__(self):
        self._canciones = ListaEnlazada()

    def agregar(self, cancion):
        return self._canciones.insertar_al_final(cancion)

    def quitar(self, id):
        anterior = None
        actual = self._canciones._cabeza
        while actual is not None:
            if actual.dato.id == id:
                if anterior is None:
                    return self._canciones.quitar_primero()
                anterior.siguiente = actual.siguiente
                self._canciones._tamanio -= 1
                return actual.dato
            anterior = actual
            actual = actual.siguiente
        raise CancionNoEncontradaError(
            f"La cancion con id {id} no esta en la playlist."
        )

    def listar(self):
        return [str(cancion) for cancion in self._canciones]

    def duracion_total(self):
        total = 0
        for cancion in self._canciones:
            total += cancion.duracion_seg
        return total


# Con n > 0 se visitan los n nodoods, realizando n -| avance entre nodo hasta 
# llegar al ultimo para enlazar el nuevo.
# La operacion tiene complejidad 0(n).
# Con n = 0 se asigna el primer nodo directamente y se visitan 0 noodos previos.

