from ejercicio_04 import ListaEnlazada

class ColaVaciaError(Exception):
    pass

class Cola:
    def __init__(self):
        self.elementos = ListaEnlazada()

    def encolar(self, dato):
        self.elementos.insertar_al_final(dato)

    def desencolar(self):
        if self.elementos.esta_vacia():
            raise ColaVaciaError("La cola esta vacia")
        return self.elementos.quitar_primero()

    def ver_frente(self):
        if self.elementos.esta_vacia():
            raise ColaVaciaError("La cola esta vacia")
        return self.elementos.primero.dato

    def esta_vacia(self):
        return self.elementos.esta_vacia()

class ColaTurnos:
    def __init__(self):
        self.turnos = Cola()

    def encolar(self, pokemon):
        self.turnos.encolar(pokemon)

    def siguiente(self):
        return self.turnos.desencolar()

    def proximo(self):
        return self.turnos.ver_frente()

# TEORIA: En este caso la cola es FIFO, sale primero el que entro primero. 
# Por ende en este caso sale A ya que fue el primero en entrar