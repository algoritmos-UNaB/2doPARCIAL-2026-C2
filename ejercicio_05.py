class PilaVaciaError(Exception):
    pass

class Pila:
    def __init__(self):
        self.lista = ListaEnlazada()

    def apilar(self, dato):
        return self.lista.insertar_al_inicio(dato)

    def desapilar(self):
        if self.esta_vacia():
            raise PilaVaciaError("Error: la pila está vacía")
        return self.lista.quitar_primero()

    def ver_tope(self):
        if self.esta_vacia():
            raise PilaVaciaError("Error: la pila está vacía")
        return self.lista.primero.dato

    def esta_vacia(self):
        return self.lista.esta_vacia()

class HistorialReproduccion:
    def __init__(self):
        self.pila = Pila()

    def registrar(self, cancion):
        return self.pila.apilar(cancion)

    def anterior(self):
        return self.pila.desapilar()

    def ultima(self):
        return self.pila.ver_tope()

# El primer anterior() devuelve "De Musica Ligera" porque fue la última canción apilada. 