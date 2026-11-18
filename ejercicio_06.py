from ejercicio_04 import ListaEnlazada

class ColaVaciaError(Exception):
    pass

class Cola:
    def __init__(self):
        self.lista = ListaEnlazada()
    
    def encolar(self, dato):
        self.lista.insertar_al_final(dato)

    def esta_vacia(self):
        return self.lista.esta_vacia()

    def desencolar(self):
        if self.esta_vacia():
            raise ColaVaciaError("La cola esta vacia")
       
        return self.lista.quitar_primero()

    def ver_frente(self):
        if self.esta_vacia():
            raise ColaVaciaError("La cola esta vacia")
        return self.lista.cabeza.dato

class ColaTurnos:
    def __init__(self):
            self.cola = Cola()

    def encolar(self, pokemon):
        self.cola.encolar(pokemon)
    
    def siguiente(self):
        return self.cola.desencolar()

    def proximo(self):
        return self.cola.ver_frente()


# TEORIA 
# Por que encolar inserta al final y el metodo quita el primero, en este caso el que entra primero sale primero FIFO
