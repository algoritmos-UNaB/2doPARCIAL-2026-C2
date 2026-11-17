
from ejercicio_04 import ListaEnlazada


class ColaVaciaError(Exception):
    pass


class Cola:
    def __init__(self):
        self.datos = ListaEnlazada()

    def encolar(self, dato):
        self.datos.insertar_al_final(dato)

    def desencolar(self):
        if self.esta_vacia():
            raise ColaVaciaError("La cola esta vacia")

        return self.datos.quitar_primero()

    def ver_frente(self):
        if self.esta_vacia():
            raise ColaVaciaError("La cola esta vacia")

        return self.datos.primero.dato

    def esta_vacia(self):
        return self.datos.esta_vacia()


class ColaPreparacion:
    def __init__(self):
        self.cola = Cola()

    def encolar(self, receta):
        self.cola.encolar(receta)

    def siguiente(self):
        return self.cola.desencolar()

    def proxima(self):
        return self.cola.ver_frente()


# TEORIA
# No devuelve C porque una cola funciona con la disciplina FIFO: el primero en entrar es el primero en salir.
