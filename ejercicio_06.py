class ColaVaciaError(Exception):
    pass

class Cola:
    def _init_(self):
        self.datos = ListaEnlazada()

    def encolar(self, dato):
        self.datos.insertar_al_final(dato)

    def desencolar(self):
        if self.esta_vacia():
            raise ColaVaciaError("La cola está vacía.")
        return self.datos.quitar_primero()

    def ver_frente(self):
        if self.esta_vacia():
            raise ColaVaciaError("La cola está vacía.")
        return self.datos.primero.dato

    def esta_vacia(self):
        return self.datos.esta_vacia()


class ColaPreparacion:
    def _init_(self):
        self.pedidos = Cola()

    def encolar(self, receta):
        self.pedidos.encolar(receta)

    def siguiente(self):
        return self.pedidos.desencolar()

    def proxima(self):
        return self.pedidos.ver_frente()

# TEORIA: No devuelve C porque la cola implementa la disciplina FIFO (First In, First Out), garantizando que los elementos salgan en el mismo orden de llegada.