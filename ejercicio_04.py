## Ejercicio 4 — Playlist sobre lista enlazada (14 pts)

#Implementar, con nodos propios:

#```python
#class Nodo:
#    def __init__(self, dato, siguiente=None): ...

#class ListaEnlazada:
#    def esta_vacia(self) -> bool: ...
#    def tamanio(self) -> int: ...
#    def insertar_al_inicio(self, dato): ...
#    def insertar_al_final(self, dato): ...
#    def quitar_primero(self): ...
#    def __iter__(self): ...
#```

#`quitar_primero` devuelve el dato que estaba al frente y lo saca de la lista. El iterador recorre desde el primero hasta el último y termina con `StopIteration` (o con `yield`).

#Definir `Playlist`, que guarda canciones en una `ListaEnlazada`. No tiene tope de cantidad.

#- `agregar(cancion)` la inserta al final.
#- `quitar(id)` saca la canción con ese `id`. Si no está en la playlist, lanza `CancionNoEncontradaError`.
#- `listar()` devuelve los `__str__` recorriendo el iterador de la lista.
#- `duracion_total()` devuelve la suma de `duracion_seg` recorriendo el iterador. Playlist vacía: `0`.

#**Teoría.** La lista solo guarda una referencia al primer nodo. ¿Cuántos nodos se recorren para insertar al final cuando ya hay `n` elementos?

#---
class Nodo:
    def __init__(self, dato, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente

class ListaEnlazada:
    def __init__(self):
        self._cabeza = None
        self._tamanio = 0
    def esta_vacia(self):
        return self._cabeza is None
    def tamanio(self):
        return self._tamanio
    def insertar_al_inicio(self, dato):
        nuevo = Nodo(dato, self._cabeza)
        self._cabeza = nuevo
        self._tamanio += 1
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
    def quitar_primero(self):
        if self.esta_vacia():
            return None
        dato = self._cabeza.dato
        self._cabeza = self._cabeza.siguiente
        self._tamanio -= 1
        return dato
    def __iter__(self):
        actual = self._cabeza
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente
#RESPUESTA= Lo que le tome al equipo por la cantidad de nodos. O(n)