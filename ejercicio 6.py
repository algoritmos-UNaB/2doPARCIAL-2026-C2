# ejercicio_06.py

from ejercicio_04 import ListaEnlazada, Cancion, CancionNoEncontradaError


class ColaVaciaError(Exception):
    def __init__(self):
        super().__init__("La cola está vacía.")


class Cola:
    def __init__(self):
        self._lista = ListaEnlazada()

    def encolar(self, dato):
        self._lista.insertar_al_final(dato)

    def desencolar(self):
        if self._lista.esta_vacia():
            raise ColaVaciaError()
        return self._lista.quitar_primero()

    def ver_frente(self):
        if self._lista.esta_vacia():
            raise ColaVaciaError()
        return self._lista._primero.dato

    def esta_vacia(self):
        return self._lista.esta_vacia()


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
# El primer siguiente() devuelve "Jijiji", porque la cola es FIFO: el
# primero encolado es el primero en salir. En la pila (ej. 5) el orden
# es LIFO: el último registrado es el primero en devolverse (De Música Ligera).
