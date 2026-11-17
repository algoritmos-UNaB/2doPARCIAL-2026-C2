from ejercicio_04 import ListaEnlazada


class PilaVaciaError(Exception):
    pass


class Pila:

    def __init__(self):
        self.elementos = ListaEnlazada()

    def apilar(self, dato):
        self.elementos.insertar_al_inicio(dato)

    def desapilar(self):
        if self.esta_vacia():
            raise PilaVaciaError("La pila esta vacia")

        return self.elementos.quitar_primero()

    def ver_tope(self):
        if self.esta_vacia():
            raise PilaVaciaError("La pila esta vacia")

        return self.elementos.buscar_primero()

    def esta_vacia(self):
        return self.elementos.esta_vacia()


class HistorialAcciones:

    def __init__(self):
        self.pila = Pila()

    def registrar(self, accion):
        self.pila.apilar(accion)

    def deshacer(self):
        return self.pila.desapilar()

    def ultima(self):
        return self.pila.ver_tope()


#Teoria
#Despues de apilar tanto "A","B","C" al desapilar una vez queda "B" a la
# cabeza, esto se llama "LIFO" (Last In, First Out)