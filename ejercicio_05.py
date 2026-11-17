"""Ejercicio 5. Historial de reproduccion mediante una pila."""

if __package__:
    from .ejercicio_04 import ListaEnlazada
else:
    from ejercicio_04 import ListaEnlazada


class PilaVaciaError(Exception):
    """Se intento consultar o desapilar una pila vacia."""


class Pila:
    def __init__(self):
        self._items = ListaEnlazada()

    def apilar(self, dato):
        return self._items.insertar_al_inicio(dato)

    def desapilar(self):
        if self.esta_vacia():
            raise PilaVaciaError("No se puede desapilar porque la pila esta vacia.")
        return self._items.quitar_primero()

    def ver_tope(self):
        if self.esta_vacia():
            raise PilaVaciaError("No se puede ver el tope de una pila vacia.")
        return self._items._cabeza.dato

    def esta_vacia(self):
        return self._items.esta_vacia()


class HistorialReproduccion:
    def __init__(self):
        self._pila = Pila()

    def registrar(self, cancion):
        return self._pila.apilar(cancion)

    def anterior(self):
        return self._pila.desapilar()

    def ultima(self):
        return self._pila.ver_tope()


# el primer anterior() devuelve , la ultima cancion crada
# la pila aplica LIFO , asi que el ultimo elemento apilado es el primero que devuelve desapilar()
