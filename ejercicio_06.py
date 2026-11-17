from ejercicio_04 import ListaEnlazada


class ColaVaciaError(Exception):
    pass


class Cola:

    def __init__(self):
        self._lista = ListaEnlazada()

    def encolar(self, dato):
        self._lista.insertar_al_final(dato)

    def desencolar(self):
        if self.esta_vacia():
            raise ColaVaciaError("Cola vacía")
        return self._lista.quitar_primero()

    def ver_frente(self):
        if self.esta_vacia():
            raise ColaVaciaError("Cola vacía")
        return next(iter(self._lista))

    def esta_vacia(self):
        return self._lista.esta_vacia()


class ColaTurnos:

    def __init__(self):
        self._cola = Cola()

    def encolar(self, pokemon):
        self._cola.encolar(pokemon)

    def siguiente(self):
        return self._cola.desencolar()

    def proximo(self):
        return self._cola.ver_frente()


# TEORIA
# Porque la cola es FIFO, el primero que entra es el primero que sale.