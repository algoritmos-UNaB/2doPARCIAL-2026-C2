# TEORÍA: No devuelve C porque la cola funciona bajo la disciplina FIFO (First In, First Out,
# "primero en entrar, primero en salir"). Como A fue el primer elemento en encolarse, es el que
# lleva más tiempo esperando y sale primero, mientras que C queda al final esperando su turno.

from ejercicio_04 import ListaEnlazada


class ColaVaciaError(Exception):
    pass


class Cola:
    def _init_(self):
        self._datos = ListaEnlazada()

    def esta_vacia(self):
        return self._datos.esta_vacia()

    def encolar(self, dato):
        self._datos.insertar_al_final(dato)

    def desencolar(self):
        if self.esta_vacia():
            raise ColaVaciaError("No se puede desencolar de una cola vacía.")
        return self._datos.quitar_primero()

    def ver_frente(self):
        if self.esta_vacia():
            raise ColaVaciaError("No se puede ver el frente de una cola vacía.")
        return self._datos.cabeza.dato


class ColaTurnos:
    def _init_(self):
        self._cola = Cola()

    def encolar(self, pokemon):
        self._cola.encolar(pokemon)

    def siguiente(self):
        return self._cola.desencolar()

    def proximo(self):
        return self._cola.ver_frente()