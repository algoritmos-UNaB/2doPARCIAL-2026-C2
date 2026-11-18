from ejercicio_02 import CancionNoEncontradaError


class ListaVaciaError(Exception):
    def __init__(self, mensaje="La lista está vacía"):
        super().__init__(mensaje)


class Nodo:
    def __init__(self, dato, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente


class ListaEnlazada:
    def __init__(self):
        self.primero = None

    def esta_vacia(self) -> bool:
        return self.primero is None

    def tamanio(self) -> int:
        cantidad = 0
        actual = self.primero
        while actual is not None:
            cantidad += 1
            actual = actual.siguiente
        return cantidad

    def insertar_al_inicio(self, dato):
        self.primero = Nodo(dato, self.primero)

    def insertar_al_final(self, dato):
        nuevo = Nodo(dato)
        if self.primero is None:
            self.primero = nuevo
            return
        actual = self.primero
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevo

    def quitar_primero(self):
        if self.primero is None:
            raise ListaVaciaError("No se puede quitar el primero de una lista vacía")
        dato = self.primero.dato
        self.primero = self.primero.siguiente
        return dato

    def quitar_si(self, condicion) -> bool:
        """Quita el primer nodo cuyo dato cumple la condición. Devuelve si quitó algo."""
        anterior = None
        actual = self.primero
        while actual is not None:
            if condicion(actual.dato):
                if anterior is None:
                    self.primero = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def __iter__(self):
        actual = self.primero
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente


class Playlist:
    def __init__(self):
        self._canciones = ListaEnlazada()

    def agregar(self, cancion):
        self._canciones.insertar_al_final(cancion)

    def quitar(self, id):
        if not self._canciones.quitar_si(lambda c: c.id == id):
            raise CancionNoEncontradaError(
                f"No existe una canción con id {id} en la playlist")

    def listar(self):
        return [str(cancion) for cancion in self._canciones]

    def duracion_total(self):
        total = 0
        for cancion in self._canciones:
            total += cancion.duracion_seg
        return total


# Teoria:
# Como la lista solo conoce el primer nodo, para insertar al final hay que
# recorrer los n nodos existentes hasta llegar al último: n nodos (O(n)).