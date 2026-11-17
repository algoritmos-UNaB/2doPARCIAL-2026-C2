
class PilaVaciaError(Exception):
    pass

class Pila:
    def _init_(self):
        self.datos = ListaEnlazada()

    def apilar(self, dato):
        self.datos.insertar_al_inicio(dato)

    def desapilar(self):
        if self.esta_vacia():
            raise PilaVaciaError("La pila está vacía.")
        return self.datos.quitar_primero()

    def ver_tope(self):
        if self.esta_vacia():
            raise PilaVaciaError("La pila está vacía.")
        return self.datos.primero.dato

    def esta_vacia(self):
        return self.datos.esta_vacia()


class HistorialCocinado:
    def _init_(self):
        self.historial = Pila()

    def cocinar(self, receta):
        self.historial.apilar(receta)

    def deshacer(self):
        return self.historial.desapilar()

    def ultima(self):
        return self.historial.ver_tope()

# TEORIA: Queda "B" en el tope. Esta disciplina de estructura de datos se llama LIFO (Last In, First Out).