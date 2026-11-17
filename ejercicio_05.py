from ejercicio_04 import ListaEnlazada

class PilaVaciaError(exception):
    pass

class Pila:
    def __init__(self):
        self.lista = ListaEnlazada()

    def esta_vacia(self):
        return self.lista.esta_vacia()

    def apilar(self, dato):
        self.lista.insertar_al_inicio(dato)

    def desapilar(self):
        if self.esta_vacia():
            raise PilaVaciaError("La pila está vacía")

        return self.lista.quitar_primero()

    def ver_tope(self):
        if self.esta_vacia():
            raise PilaVaciaError("La pila está vacía")

        return self.lista.cabeza.dato

class HistorialAcciones:
    def __init__(self):
        self.pila = Pila()

    def registrar(self, accion):
        self.pila.apilar(accion)

    def deshacer(self):
        return self.pila.desapilar()

    def ultima(self):
        return self.pila.ver_tope()


# Al desapilar se retira "C" y queda "B" en el tope, la disciplina se llama LIFO (Last In, First Out) el primero en entrar es el primero en salir.