from ejercicio_04 import ListaEnlazada

class PilaVaciaError(Exception):
    pass

class Pila:
    def __init__(self):
        self.elementos = ListaEnlazada()

    def apilar(self, dato):
        self.elementos.insertar_al_inicio(dato)

    def desapilar(self):
        if self.elementos.esta_vacia():
            raise PilaVaciaError("La pila esta vacia")
        return self.elementos.quitar_primero()

    def ver_tope(self):
        if self.elementos.esta_vacia():
            raise PilaVaciaError("La pila esta vacia")
        return self.elementos.primero.dato

    def esta_vacia(self):
        return self.elementos.esta_vacia()

class HistorialAcciones:
    def __init__(self):
        self.acciones = Pila()

    def registrar(self, accion):
        self.acciones.apilar(accion)

    def deshacer(self):
        return self.acciones.desapilar()

    def ultima(self):
        return self.acciones.ver_tope()

# TEORIA -> En este caso queda B, el ultimo que entra es el primero en salir (LIFO) en este caso sale C y queda el anterior