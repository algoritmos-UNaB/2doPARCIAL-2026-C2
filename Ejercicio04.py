class Nodo:
    def __init__(self, dato, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self._tamanio = 0

    def esta_vacia(self) -> bool:
        return self.cabeza is None

    def tamanio(self) -> int:
        return self._tamanio

    def insertar_al_inicio(self, dato):
        nuevo = Nodo(dato, self.cabeza)
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
            raise IndexError("La lista está vacía")
        dato = self.cabeza.dato
        self.cabeza = self.cabeza.siguiente
        self._tamanio -= 1
        return dato

    def __iter__(self):
        actual = self.cabeza
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente

class Playlist:
    def __init__(self):
        self.elementos = ListaEnlazada()

    def agregar(self, cancion):
        self.elementos.insertar_al_final(cancion)

    def quitar(self, id):
        if self.elementos.esta_vacia():
            raise CancionNoEncontradaError(f"No se encontró la canción con id {id}")

        if self.elementos.cabeza.dato.id == id:
            self.elementos.quitar_primero()
            return

        actual = self.elementos.cabeza
        while actual.siguiente is not None:
            if actual.siguiente.dato.id == id:
                actual.siguiente = actual.siguiente.siguiente
                self.elementos._tamanio -= 1
                return
            actual = actual.siguiente

        raise CancionNoEncontradaError(f"No se encontró la canción con id {id}")

    def listar(self) -> list:
        return [str(cancion) for cancion in self.elementos]

    def duracion_total(self) -> int:
        total = 0
        for cancion in self.elementos:
            total += cancion.duracion_seg
        return total            

#Teoría. La lista solo guarda una referencia al primer nodo.
# ¿Cuántos nodos se recorren para insertar al final cuando ya hay n elementos?
#Rta:  Se recorren n nodos.