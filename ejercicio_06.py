"""Ejercicio 6. Cola de las proximas canciones a reproducir."""

if __package__:
    from .ejercicio_04 import ListaEnlazada
else:
    from ejercicio_04 import ListaEnlazada


class ColaVaciaError(Exception):
    """Se intento consultar o desencolar una cola vacia."""


class Cola:
    def __init__(self):
        self._items = ListaEnlazada()

    def encolar(self, dato):
        return self._items.insertar_al_final(dato)

    def desencolar(self):
        if self.esta_vacia():
            raise ColaVaciaError("No se puede desencolar porque la cola esta vacia.")
        return self._items.quitar_primero()

    def ver_frente(self):
        if self.esta_vacia():
            raise ColaVaciaError("No se puede ver el frente de una cola vacia.")
        return self._items._cabeza.dato

    def esta_vacia(self):
        return self._items.esta_vacia()


class ColaReproduccion:
    def __init__(self):
        self._cola = Cola()

    def encolar_cancion(self, cancion):
        return self._cola.encolar(cancion)

    def siguiente(self):
        return self._cola.desencolar()

    def que_sigue(self):
        return self._cola.ver_frente()

# el primer siguiente() devuelve jijiji la primer cancion ecolada
# la cola aplica FIFO y mantiene el orden de llegada. La pila aplica LIFO y devuelve
# primero la ultima cancion agregada.
