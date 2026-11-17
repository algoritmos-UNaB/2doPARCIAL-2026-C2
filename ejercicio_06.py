from ejercicio_04 import ListaEnlazada
from ejercicio_01 import Pokemon


class ColaVaciaError(Exception):
    pass


class Cola:
    def __init__(self):
        self.elementos = ListaEnlazada()

    def encolar(self, elemento):
        self.elementos.insertar_al_final(elemento)

    def desencolar(self):
        if self.esta_vacia():
            raise ColaVaciaError("La cola está vacía")

        return self.elementos.quitar_primero()

    def ver_frente(self):
        if self.esta_vacia():
            raise ColaVaciaError("La cola está vacía")

        return self.elementos.buscar_primero()

    def esta_vacia(self):
        return self.elementos.esta_vacia()


class ColaTurnos:
    def __init__(self):
        self.cola = Cola()

    def encolar(self, pokemon):
        self.cola.encolar(pokemon)

    def siguiente(self):
        return self.cola.desencolar()

    def proximo(self):
        return self.cola.ver_frente()


#Teoria
#Una "Cola" usa el principio "FIFO" (First in, First Out)
# Ej: si ingresean "A","B","C" al desencolar se obtiene "a", luego "b" y x
# ultimo "c"