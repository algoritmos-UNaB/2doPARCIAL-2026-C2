from ejercicio_04 import ListaEnlazada

class PilaVaciaError(Exception):
    pass

class Pila:
    def _init_(self):
        self.items = ListaEnlazada()

    def apilar(self, dato):
        self.items.insertar_al_inicio(dato)

    def desapilar(self):
        if self.esta_vacia():
            raise PilaVaciaError("La pila está vacía.")
        return self.items.quitar_primero()

    def ver_tope(self):
        if self.esta_vacia():
            raise PilaVaciaError("La pila está vacía.")
        return self.items.primero.dato

    def esta_vacia(self):
        return self.items.esta_vacia()

class HistorialAcciones:
    def _init_(self):
        self.acciones = Pila()

    def registrar(self, accion):
        self.acciones.apilar(accion)

    def deshacer(self):
        return self.acciones.desapilar()

    def ultima(self):
        return self.acciones.ver_tope()

# TEORIA
#  En el tope queda "B", ya que al desapilar salió "C". Esta disciplina se llama LIFO (Last In, First Out).