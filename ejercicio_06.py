"""Ejercicio 6 — Cola y ColaPreparacion."""

from ejercicio_04 import ListaEnlazada


class ColaVaciaError(Exception):
    """Se pidió desencolar o ver el frente de una cola vacía."""


class Cola:
    """Cola (FIFO) sobre ListaEnlazada: el frente es la cabeza y se encola al final.

    encolar = insertar_al_final (O(1) gracias a _ultimo) y
    desencolar = quitar_primero (O(1)).
    """

    def __init__(self):
        self._datos = ListaEnlazada()

    def encolar(self, dato):
        self._datos.insertar_al_final(dato)

    def desencolar(self):
        if self.esta_vacia():
            raise ColaVaciaError("La cola está vacía.")
        return self._datos.quitar_primero()

    def ver_frente(self):
        if self.esta_vacia():
            raise ColaVaciaError("La cola está vacía.")
        return self._datos.ver_primero()

    def esta_vacia(self):
        return self._datos.esta_vacia()


class ColaPreparacion:
    """Recetas esperando para prepararse, en orden de llegada."""

    def __init__(self):
        self._cola = Cola()

    def encolar(self, receta):
        self._cola.encolar(receta)

    def siguiente(self):
        return self._cola.desencolar()     

    def proxima(self):
        return self._cola.ver_frente()     


# TEORIA
# Porque la cola es FIFO (First In, First Out): se encola al final y se
# desencola del frente. A entró primero y quedó en el frente; C entró última,
# quedó al final y va a salir última.


if __name__ == "__main__":
    cola = Cola()
    for letra in ("A", "B", "C"):
        cola.encolar(letra)
    print("desencolo:", cola.desencolar(), "| frente:", cola.ver_frente())

    from ejercicio_02 import libro_examen
    from ejercicio_04 import LibroRecetas
    libro = libro_examen(LibroRecetas())
    preparacion = ColaPreparacion()
    preparacion.encolar(libro.obtener(5))
    preparacion.encolar(libro.obtener(10))
    print("próxima:", preparacion.proxima())
    print("siguiente:", preparacion.siguiente())
    print("siguiente:", preparacion.siguiente())
    try:
        preparacion.proxima()
    except ColaVaciaError as error:
        print("ColaVaciaError:", error)
