from ejercicio_04 import ListaEnlazada


class PilaVaciaError(Exception):
    pass


class Pila:

    def __init__(self):
        self._lista = ListaEnlazada()

    def apilar(self, dato):
        self._lista.insertar_al_inicio(dato)

    def desapilar(self):
        if self.esta_vacia():
            raise PilaVaciaError("Pila vacía")
        return self._lista.quitar_primero()

    def ver_tope(self):
        if self.esta_vacia():
            raise PilaVaciaError("Pila vacía")
        return next(iter(self._lista))

    def esta_vacia(self):
        return self._lista.esta_vacia()


class HistorialAcciones:

    def __init__(self):
        self._pila = Pila()

    def registrar(self, accion):
        self._pila.apilar(accion)

    def deshacer(self):
        return self._pila.desapilar()

    def ultima(self):
        return self._pila.ver_tope()


# TEORIA
# Queda B en el tope. Porque se saca C que fue el último que entró. 
# Se llama LIFO. El último que entra es el primero que sale.