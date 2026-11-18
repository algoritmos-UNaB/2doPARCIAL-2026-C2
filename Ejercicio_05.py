from Ejercicio_04 import ListaEnlazada

## Ejercicio 5 — Historial de reproducción (10 pts)

#Implementar `Pila` sobre `ListaEnlazada` (apilar y desapilar en el extremo del primer nodo):

#- `apilar(dato)`
#- `desapilar()` devuelve el tope. Si está vacía, lanza `PilaVaciaError`.
#- `ver_tope()` devuelve el tope y lo deja en la pila. Si está vacía, lanza `PilaVaciaError`.
#- `esta_vacia()`

#Definir `HistorialReproduccion`, que usa una `Pila` de canciones:

#- `registrar(cancion)` apila lo que acaba de sonar.
#- `anterior()` desapila y devuelve la canción a la que se vuelve.
#- `ultima()` devuelve la última canción reproducida, sin sacarla.

#**Teoría.** Se registran, en este orden, Jijiji, Alfonsina y el mar, y De Música Ligera. ¿Qué devuelve el primer `anterior()`? ¿Por qué?

class PilaVaciaError (Exception):
    pass

class Pila:
    def __init__ (self):
        self.lista = ListaEnlazada()

    def esta_vacia (self):
        return self.lista.esta_vacia()
    
    def apilar (self, dato):
        self.lista.insertar_al_inicio(dato)

    def desapilar (self):
        if self.esta_vacia() == True:
            raise PilaVaciaError ("La pila esta vacia!")
        dato = self.lista.quitar_primero()
        return dato

    def ver_tope(self):
        if self.esta_vacia() == True:
            raise PilaVaciaError ("La pila esta Vacia!")
        dato = self.lista.primero.dato
        return dato

class HistorialReproduccion:
    def __init__(self):
        self.pila = Pila()

    def registrar (self, cancion):
        self.pila.apilar(cancion)

    def anterior (self):
        cancion =  self.pila.desapilar()
        return cancion
    
    def ultima (self):
        cancion = self.pila.ver_tope()
        return cancion

#RTA Teoria: Devuelve De Musica Ligera porque la pila funciona ultimo en entrar primero en salir, al haber sido la ultima cancion agregada quedo arriba y es la primera que sale