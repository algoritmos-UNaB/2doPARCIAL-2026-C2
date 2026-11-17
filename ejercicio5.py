## Ejercicio 5 — Historial de reproducción (10 pts)

class PilaVaciaError(Exception):
    def __init__(self):
        super().__init__("La pila está vacía.")


class Pila:
    def __init__(self):
        self._lista = ListaEnlazada()

    def apilar(self, dato):
        self._lista.insertar_al_inicio(dato)

    def desapilar(self):
        if self._lista.esta_vacia():
            raise PilaVaciaError()
        return self._lista.quitar_primero()

    def ver_tope(self):
        if self._lista.esta_vacia():
            raise PilaVaciaError()
        return self._lista._primero.dato

    def esta_vacia(self):
        return self._lista.esta_vacia()


class HistorialReproduccion:
    def __init__(self):
        self._pila = Pila()

    def registrar(self, cancion):
        self._pila.apilar(cancion)

    def anterior(self):
        return self._pila.desapilar()

    def ultima(self):
        return self._pila.ver_tope()

# **Teoría.**
# Devuelve "De musica ligera", fue el ultimo elemento cargado, por ende el primero de la pila en salir al desapilar
