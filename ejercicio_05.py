# TEORÍA: En el tope queda "B", ya que al apilar "A", luego "B" y por último "C", el último elemento
# en entrar es "C" y al desapilar una vez se extrae ese elemento dejando a "B" arriba. Esta disciplina
# se llama LIFO (Last In, First Out, o "último en entrar, primero en salir").

from ejercicio_04 import ListaEnlazada


class PilaVaciaError(Exception):
    pass


class Pila:
    def _init_(self):
        self._datos = ListaEnlazada()

    def esta_vacia(self):
        return self._datos.esta_vacia()

    def apilar(self, dato):
        self._datos.insertar_al_inicio(dato)

    def desapilar(self):
        if self.esta_vacia():
            raise PilaVaciaError("No se puede desapilar de una pila vacía.")
        return self._datos.quitar_primero()

    def ver_tope(self):
        if self.esta_vacia():
            raise PilaVaciaError("No se puede ver el tope de una pila vacía.")
        return self._datos.cabeza.dato


class HistorialAcciones:
    def _init_(self):
        self._pila = Pila()

    def registrar(self, accion):
        self._pila.apilar(accion)

    def deshacer(self):
        return self._pila.desapilar()

    def ultima(self):
        return self._pila.ver_tope()