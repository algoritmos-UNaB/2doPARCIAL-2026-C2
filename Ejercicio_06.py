from Ejercicio_04 import ListaEnlazada


## Ejercicio 6 — Cola de reproducción (10 pts)

#Implementar `Cola` sobre `ListaEnlazada`:

#- `encolar(dato)` agrega al final.
#- `desencolar()` saca y devuelve el primero. Si está vacía, lanza `ColaVaciaError`.
#- `ver_frente()` devuelve el primero y lo deja en la cola. Si está vacía, lanza `ColaVaciaError`.
#- `esta_vacia()`

#Definir `ColaReproduccion` (la cola “up next”), que usa una `Cola` de canciones:

#- `encolar_cancion(cancion)`
#- `siguiente()` devuelve la canción que toca ahora.
#- `que_sigue()` devuelve la canción del frente, sin sacarla.

#**Teoría.** Se encolan, en este orden, Jijiji, Alfonsina y el mar, y De Música Ligera. ¿Qué devuelve el primer `siguiente()`? ¿En qué se diferencia este orden del de la pila del ejercicio 5?

class ColaVaciaError (Exception):
    pass

class Cola:
    def __init__ (self):
        self.lista = ListaEnlazada()
    
    def esta_vacia (self):
        return self.lista.esta_vacia()

    def encolar (self, dato):
        self.lista.insertar_al_final (dato)

    def desencolar (self):
        if self.esta_vacia() == True
            raise ColaVaciaError ("La cola esta vacia!")
        dato = self.lista.quitar_primero()
        return dato

    def ver_frente (self):
        if self.esta_vacia() == True:
            raise ColaVaciaError ("La cola esta Vacia!")
        dato = self.lista.primero.dato
        return dato


class ColaReproduccion:
    def __init__ (self):
        self.cola = Cola()
    
    def encolar_cancion (self, cancion):
        self.cola.encolar (cancion)
    
    def siguiente (self):
        cancion = self.cola.desencolar()
        return cancion

    def que_sigue (self)
        cancion = self.cola.ver_frente()
        return cancion



#RTA Teoria: En este caso la primera que sale al contrario de la pila es Jijiji,  ya que el primero que entra es el primero que sale en la Cola
