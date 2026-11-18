## Ejercicio 4 — Playlist sobre lista enlazada (14 pts)

from ejercicio2 import Cancion, CancionNoEncontradaError

class Nodo:
    def __init__(self, dato, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente

class ListaEnlazada:
    def __init__(self):
        self._primero = None
        self._tamanio = 0

    def esta_vacia(self):
        return self._primero is None

    def tamanio(self):
        return self._tamanio

    def insertar_al_inicio(self, dato):
        self._primero = Nodo(dato, self._primero)
        self._tamanio += 1

    def insertar_al_final(self, dato):
        nuevo = Nodo(dato)
        if self._primero is None:
            self._primero = nuevo
        else:
            actual = self._primero
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self._tamanio += 1

    def quitar_primero(self):
        if self._primero is None:
            raise IndexError("La lista está vacía.")
        dato = self._primero.dato
        self._primero = self._primero.siguiente
        self._tamanio -= 1
        return dato

    def __iter__(self):
        actual = self._primero
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente

class Playlist:
    def __init__(self):
        self._canciones = ListaEnlazada()

    def agregar(self, cancion):
        self._canciones.insertar_al_final(cancion)

    def quitar(self, id):
        anterior = None
        actual = self._canciones._primero
        while actual is not None:
            if actual.dato.id == id:
                if anterior is None:
                    self._canciones.quitar_primero()
                else:
                    anterior.siguiente = actual.siguiente
                    self._canciones._tamanio -= 1
                return
            anterior = actual
            actual = actual.siguiente
        raise CancionNoEncontradaError(id)

    def listar(self):
        return [str(cancion) for cancion in self._canciones]

    def duracion_total(self):
        total = 0
        for cancion in self._canciones:
            total += cancion.duracion_seg
        return total

# **Teoría.**
# Para insertar al final cuando ya hay n elementos se recorren n nodos:
# se visita el primero y se avanza por `siguiente` hasta llegar al último
# (el que tiene siguiente == None), y se engancha el nuevo nodo ahí.
# Es O(n) porque la lista solo guarda referencia al primero, no al último.
