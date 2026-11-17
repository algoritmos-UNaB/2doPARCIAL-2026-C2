from ejercicio_04 import ListaEnlazada


class PilaVaciaError(Exception):
    def __init__(self, mensaje="La pila está vacía."):
        super().__init__(mensaje)


class Pila:
    def __init__(self):
        self._items = ListaEnlazada()

    def apilar(self, dato):
        # pongo el elemento al inicio de la lista
        self._items.insertar_al_inicio(dato)

    def desapilar(self):
        if self.esta_vacia():
            raise PilaVaciaError("No se puede desapilar: la pila está vacía.")

        return self._items.quitar_primero()

    def ver_tope(self):
        if self.esta_vacia():
            raise PilaVaciaError("No se puede ver el tope: la pila está vacía.")

        # obtengo el 1er elemento sin eliminarlo
        return next(iter(self._items))

    def esta_vacia(self):
        return self._items.esta_vacia()


class HistorialReproduccion:
    def __init__(self):
        self._pila = Pila()

    def registrar(self, cancion):
        self._pila.apilar(cancion)

    def anterior(self):
        return self._pila.desapilar()

    def ultima(self):
        return self._pila.ver_tope()



# El primer anterior() devuelve "De Música Ligera"
# Porque la pila sigue una estructura LIFO, o sea último en entrar, primero en salir. Como fue la última canción registrada, quedó en el tope y es la primera en salir