from ejercicio_02 import CancionNoEncontradaError


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
        # el nuevo nodo pasa a ser el primero en lista
        nuevo = Nodo(dato, self._cabeza)
        self._cabeza = nuevo
        self._tamanio += 1

    def insertar_al_final(self, dato):
        nuevo = Nodo(dato)

        if self.esta_vacia():
            self._cabeza = nuevo
        else:
            # recorro la lista hasta llegar al último nodo
            actual = self._cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente

            actual.siguiente = nuevo

        self._tamanio += 1

    def quitar_primero(self):
        if self.esta_vacia():
            raise IndexError("La lista está vacía.")

        dato = self._cabeza.dato
        self._cabeza = self._cabeza.siguiente
        self._tamanio -= 1

        return dato

    def eliminar(self, dato) -> bool:
        if self.esta_vacia():
            return False

        # si el dato está en el primer nodo
        if self._cabeza.dato == dato:
            self.quitar_primero()
            return True

        # busco el dato recorriendo el resto de la lista
        anterior = self._cabeza
        actual = anterior.siguiente

        while actual is not None:
            if actual.dato == dato:
                anterior.siguiente = actual.siguiente
                self._tamanio -= 1
                return True

            anterior = actual
            actual = actual.siguiente

        return False

    def __iter__(self):
        # recorro los nodos desde el 1ro hasta el último
        actual = self._cabeza

        while actual is not None:
            yield actual.dato
            actual = actual.siguiente


class Playlist:
    def __init__(self):
        self._canciones = ListaEnlazada()

    def agregar(self, cancion):
        self._canciones.insertar_al_final(cancion)

    def quitar(self, id_cancion):
        # busco la canción por id
        for cancion in self._canciones:
            if cancion.id == id_cancion:
                self._canciones.eliminar(cancion)
                return

        raise CancionNoEncontradaError(id_cancion)

    def listar(self):
        resultado = []

        for cancion in self._canciones:
            resultado.append(str(cancion))

        return resultado

    def duracion_total(self):
        total = 0

        for cancion in self._canciones:
            total += cancion.duracion_seg

        return total


# Se recorren los n nodos que ya están en la lista
# Como solo se guarda una referencia al primer nodo, hay que avanzar hasta llegar al último para poder agregar otro nuevo