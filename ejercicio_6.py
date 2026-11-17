from ejercicio_4 import ListaEnlazada


class ColaVaciaError(Exception):
    pass


class Cola:

    def __init__(self):
        self.datos = ListaEnlazada()

    def encolar(self, dato):
        self.datos.insertar_al_final(dato)

    def desencolar(self):

        if self.esta_vacia():
            raise ColaVaciaError("La cola está vacía")

        return self.datos.quitar_primero()

    def ver_frente(self):

        if self.esta_vacia():
            raise ColaVaciaError("La cola está vacía")

        return self.datos.cabeza.dato

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


# TEORIA:
# Devuelve A porque una cola sigue la disciplina FIFO:
# First In, First Out (primero en entrar, primero en salir).