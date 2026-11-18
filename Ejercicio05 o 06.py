Ejercicio 6 — Cola de reproducción (10 pts)

class ColaVaciaError(Exception):
    pass

class Cola:
    def __init__(self):
        # Usamos nuestra ListaEnlazada por debajo
        self.elementos = ListaEnlazada()

    def esta_vacia(self) -> bool:
        return self.elementos.esta_vacia()

    def encolar(self, dato):
        # Agrega al final de la lista enlazada
        self.elementos.insertar_al_final(dato)

    def desencolar(self):
        # Saca y devuelve el primero. Si está vacía, lanza error.
        if self.esta_vacia():
            raise ColaVaciaError("La cola está vacía")
        return self.elementos.quitar_primero()

    def ver_frente(self):
        # Devuelve el primero sin sacarlo
        if self.esta_vacia():
            raise ColaVaciaError("La cola está vacía")
        return self.elementos.cabeza.dato

        class ColaReproduccion:
    def __init__(self):
        self.cola_canciones = Cola()

    def encolar_cancion(self, cancion):
        self.cola_canciones.encolar(cancion)

    def siguiente(self):
        # Devuelve la canción que toca ahora (la saca de la cola)
        return self.cola_canciones.desencolar()

    def que_sigue(self):
        # Devuelve la canción del frente, sin sacarla de la cola
        return self.cola_canciones.ver_frente()

#Teoría. Se encolan, en este orden, Jijiji, Alfonsina y el mar, y De Música Ligera. 
#¿Qué devuelve el primer siguiente()?
#Dado que en la fila, el primero que entra es el primero que sale, en este caso se reproduce jijiji (el primer tema)
# ¿En qué se diferencia este orden del de la pila del ejercicio 5?
#En el caso de pila, el ultimo en ingresar es el primero que sale, por lo que en este caso, se reproduce De musica Ligera.
