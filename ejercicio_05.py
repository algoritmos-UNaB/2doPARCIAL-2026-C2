"""Ejercicio 5 — Pila y HistorialCocinado."""

from ejercicio_04 import ListaEnlazada


class PilaVaciaError(Exception):
    """Se pidió desapilar o ver el tope de una pila vacía."""


class Pila:
    """Pila (LIFO) sobre ListaEnlazada: el tope es la cabeza de la lista.

    apilar = insertar_al_inicio y desapilar = quitar_primero, las dos O(1).
    """

    def __init__(self):
        self._datos = ListaEnlazada()

    def apilar(self, dato):
        self._datos.insertar_al_inicio(dato)

    def desapilar(self):
        if self.esta_vacia():
            raise PilaVaciaError("La pila está vacía.")
        return self._datos.quitar_primero()

    def ver_tope(self):
        if self.esta_vacia():
            raise PilaVaciaError("La pila está vacía.")
        return self._datos.ver_primero()

    def esta_vacia(self):
        return self._datos.esta_vacia()


class HistorialCocinado:
    """Recetas cocinadas, la última arriba: deshacer saca la más reciente."""

    def __init__(self):
        self._pila = Pila()

    def cocinar(self, receta):
        self._pila.apilar(receta)

    def deshacer(self):
        return self._pila.desapilar()      

    def ultima(self):
        return self._pila.ver_tope()       


# TEORIA
# Queda "B" en el tope: el desapilar saca "C", que fue el último en entrar.
# La disciplina se llama LIFO (Last In, First Out: último en entrar, primero en salir).


if __name__ == "__main__":
    pila = Pila()
    for letra in ("A", "B", "C"):
        pila.apilar(letra)
    print("desapilo:", pila.desapilar(), "| tope:", pila.ver_tope())

    from ejercicio_02 import libro_examen
    from ejercicio_04 import LibroRecetas
    libro = libro_examen(LibroRecetas())
    historial = HistorialCocinado()
    historial.cocinar(libro.obtener(1))
    historial.cocinar(libro.obtener(9))
    print("última:", historial.ultima())
    print("deshacer:", historial.deshacer())
    print("deshacer:", historial.deshacer())
    try:
        historial.deshacer()
    except PilaVaciaError as error:
        print("PilaVaciaError:", error)
