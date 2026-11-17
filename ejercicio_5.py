from ejercicio_4 import ListaEnlazada


class PilaVaciaError(Exception):
    pass


class Pila:

    def __init__(self):
        self.datos = ListaEnlazada()

    def apilar(self, dato):
        self.datos.insertar_al_inicio(dato)

    def desapilar(self):

        if self.esta_vacia():
            raise PilaVaciaError("La pila está vacía")

        return self.datos.quitar_primero()

    def ver_tope(self):

        if self.esta_vacia():
            raise PilaVaciaError("La pila está vacía")

        return self.datos.cabeza.dato

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


# TEORIA:
# Quedan A y B, con B en el tope.
# La disciplina se llama LIFO:
# Last In, First Out (último en entrar, primero en salir).