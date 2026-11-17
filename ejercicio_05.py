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

#---

class HistorialReproducion:
    def __init__(self):
        self._pila = Pila()
    def registrar(self, cancion):
        self._pila.apilar(cancion)
    def anterior(self):
        return self._pila.desapilar()
    def ultima(self):
        return self._pila.ver_tope()

#RESPUESTA= Devolveria Musica Ligera ya que funciona ajo la regla de LIFO(first in first out)