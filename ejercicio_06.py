from ejercicio_04 import ListaEnlazada

class ColaVaciaError(Exception):
    pass

class Cola:
    def _init_(self):
        self.items = ListaEnlazada()

    def encolar(self, dato):
        self.items.insertar_al_final(dato)

    def desencolar(self):
        if self.esta_vacia():
            raise ColaVaciaError("La cola está vacía.")
        return self.items.quitar_primero()

    def ver_frente(self):
        if self.esta_vacia():
            raise ColaVaciaError("La cola está vacía.")
        return self.items.primero.dato

    def esta_vacia(self):
        return self.items.esta_vacia()

class ColaTurnos:
    def _init_(self):
        self.turnos = Cola()

    def encolar(self, pokemon):
        self.turnos.encolar(pokemon)

    def siguiente(self):
        return self.turnos.desencolar()

    def proximo(self):
        return self.turnos.ver_frente()

# TEORIA
#No devuelve C porque la cola sigue la disciplina FIFO (First In, First Out), donde el primer elemento en entrar (A) es el primero en salir.