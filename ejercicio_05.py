
from ejercicio_04 import ListaEnlazada


class PilaVaciaError(Exception):
    pass


class Pila:
    def __init__(self):
        self.datos = ListaEnlazada()

    def apilar(self, dato):
        self.datos.insertar_al_inicio(dato)

    def desapilar(self):
        if self.esta_vacia():
            raise PilaVaciaError("La pila esta vacia")

        return self.datos.quitar_primero()

    def ver_tope(self):
        if self.esta_vacia():
            raise PilaVaciaError("La pila esta vacia")

        return self.datos.primero.dato

    def esta_vacia(self):
        return self.datos.esta_vacia()


class HistorialCocinado:
    def __init__(self):
        self.pila = Pila()

    def cocinar(self, receta):
        self.pila.apilar(receta)

    def deshacer(self):
        return self.pila.desapilar()

    def ultima(self):
        return self.pila.ver_tope()


# TEORIA
# Queda B en el tope. La disciplina se llama LIFO

