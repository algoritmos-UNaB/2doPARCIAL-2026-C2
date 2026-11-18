from ejercicio_04 import ListaEnlazada

class PilaVaciaError(Exception):
    def __init__(self, mensaje="La pila está vacía"):
        super().__init__(mensaje)

class Pila:
    def __init__(self):
        self._lista = ListaEnlazada()

    def apilar(self,dato):
        self._lista.insertar_al_inicio(dato)

    def desapilar(self):
        if self._lista.esta_vacia():
            raise PilaVaciaError("No se puede desapilar: la pila está vacía")
        return self._lista.quitar_primero()

    def ver_tope(self):
        if self._lista.esta_vacia():
            raise PilaVaciaError("No hay tope: la pila está vacía")
        return self._lista.primero.dato
    
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


# Teoria:
# El primer anterior() devuelve "De Música Ligera", porque la pila es LIFO
# (el último en entrar es el primero en salir, como una pila de platos). La 
# última canción registrada queda en el tope, y desapilar saca justamente el tope.