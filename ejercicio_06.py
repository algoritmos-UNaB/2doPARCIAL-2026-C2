class ColaVaciaError(Exception):
    pass

class Cola:
    def __init__(self):
        self.lista = ListaEnlazada()

    def encolar(self, dato):
        return self.lista.insertar_al_final(dato)

    def desencolar(self):
        if self.esta_vacia():
            raise ColaVaciaError("Error: la cola está vacía")
        return self.lista.quitar_primero()

    def ver_frente(self):
        if self.esta_vacia():
            raise ColaVaciaError("Error: la cola está vacía")
        return self.lista.primero.dato

    def esta_vacia(self):
        return self.lista.esta_vacia()

class ColaReproduccion:
    def __init__(self): self.cola = Cola()

    def encolar_cancion(self, cancion):
        return self.cola.encolar(cancion)

    def siguiente(self):
        return self.cola.desencolar()

    def que_sigue(self):
        return self.cola.ver_frente()

# El primer siguiente() devuelve la cancion "Jijiji" porque es el primero en entrar. A diferencia de la pila que devolvía la última canción que se agregaba.