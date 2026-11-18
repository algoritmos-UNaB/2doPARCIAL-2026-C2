from ejercicio_04 import ListaEnlazada

class PilaVaciaError(Exception):
    pass

class Pila:
    def __init__(self):
        self.lista = ListaEnlazada()
    
    def apilar(self, dato):
        self.lista.insertar_al_inicio(dato)

    def esta_vacia(self):
        return self.lista.esta_vacia()

    def desapilar(self):
        if self.esta_vacia():
            raise PilaVaciaError("La pila esta vacia")
       
        return self.lista.quitar_primero()

    def ver_tope(self):
        if self.esta_vacia():
            raise PilaVaciaError("La pila esta vacia")
        return self.lista.cabeza.dato

class HistorialAcciones:
    def __init__(self):
            self.pila = Pila()

    def registrar(self, accion):
        self.pila.apilar(accion)
    
    def deshacer(self):
        return self.pila.desapilar()

    def ultima(self):
        return self.pila.ver_tope()


# TEORIA 
# Queda B porque el que entra sale ultimo, por ende el ultimo que entro se desapilo. La disciplina se llama LIFO