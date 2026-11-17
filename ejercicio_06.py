from ejercicio_04 import ListaEnlazada


class ColaVaciaError(Exception):
    def __init__(self, mensaje="La cola está vacía."):
        super().__init__(mensaje)


class Cola:
    def __init__(self):
        self._items = ListaEnlazada()

    def encolar(self, dato):
        # pongo el elemento al final de la lista
        self._items.insertar_al_final(dato)

    def desencolar(self):
        if self.esta_vacia():
            raise ColaVaciaError("No se puede desencolar: la cola está vacía.")

        return self._items.quitar_primero()

    def ver_frente(self):
        if self.esta_vacia():
            raise ColaVaciaError("No se puede ver el frente: la cola está vacía.")

        # obtengo el 1er elemento sin eliminarlo
        return next(iter(self._items))

    def esta_vacia(self):
        return self._items.esta_vacia()


class ColaReproduccion:
    def __init__(self):
        self._cola = Cola()

    def encolar_cancion(self, cancion):
        self._cola.encolar(cancion)

    def siguiente(self):
        return self._cola.desencolar()

    def que_sigue(self):
        return self._cola.ver_frente()


# Teoría:
# El primer siguiente() devuelve "Jijiji".
# Porque la cola trabaja con el principio FIFO (primero en entrar, primero en salir), por lo cual las canciones salen en el mismo orden en que fueron agregadas, a diferencia de la pila del ejercicio 5 que utiliza LIFO, donde sale primero la última canción que fue registrada.