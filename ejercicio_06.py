from ejercicio_04 import ListaEnlazada

class ColaVaciaError(Exception):
    pass

class Cola:
    def __init__(self):
        self._lista = ListaEnlazada()

    def encolar(self, dato):
        self._lista.insertar_al_final(dato)

    def desencolar(self):
        if self._lista.esta_vacia():
            raise ColaVaciaError("No se puede desencolar: la cola está vacía")
        return self._lista.quitar_primero()

    def ver_frente(self):
        if self._lista.esta_vacia():
            raise ColaVaciaError("No hay frente: la cola está vacía")
        return self._lista.primero.dato

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


    # Teoria:
    # El primr siguiente() devuelve "Jijiji": la cola es FIFO (primero en entrar,
    # primero en salir). La pila del ej. 5 es LIFO: devuelve primero la última canción
    # que entró; la cola respeta el orden de llegada.