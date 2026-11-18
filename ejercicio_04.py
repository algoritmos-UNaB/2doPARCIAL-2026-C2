"""Ejercicio 4 — Colección lineal principal: Nodo, ListaEnlazada y MenuSemanal.

Además, desde acá la colección principal del dominio es la lista enlazada
propia: LibroRecetas se redefine con la misma interfaz que en el ejercicio 2,
pero guardando las recetas en una ListaEnlazada en lugar de un list.
"""

import ejercicio_02
from ejercicio_02 import RecetaNoEncontrada


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    """Lista simplemente enlazada.

    _cabeza: primer nodo (None si está vacía).
    _ultimo: último nodo, para que insertar_al_final sea O(1) sin recorrer.
    _tamanio: cantidad de nodos, para que tamanio() sea O(1).
    """

    def __init__(self):
        self._cabeza = None
        self._ultimo = None
        self._tamanio = 0

    def esta_vacia(self):
        return self._cabeza is None

    def tamanio(self):
        return self._tamanio

    def __len__(self):
        return self._tamanio

    def insertar_al_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self._cabeza
        self._cabeza = nuevo
        if self._ultimo is None:      
            self._ultimo = nuevo
        self._tamanio += 1

    def insertar_al_final(self, dato):
        nuevo = Nodo(dato)
        if self._ultimo is None:      
            self._cabeza = nuevo
        else:
            self._ultimo.siguiente = nuevo
        self._ultimo = nuevo
        self._tamanio += 1

    def ver_primero(self):
        """El dato del primer nodo, sin sacarlo (lo usan ver_tope y ver_frente)."""
        if self.esta_vacia():
            raise IndexError("La lista está vacía.")
        return self._cabeza.dato

    def quitar_primero(self):
        """Saca el primer nodo y devuelve su dato. O(1)."""
        if self.esta_vacia():
            raise IndexError("La lista está vacía.")
        nodo = self._cabeza
        self._cabeza = nodo.siguiente
        if self._cabeza is None:      
            self._ultimo = None
        self._tamanio -= 1
        return nodo.dato

    def eliminar_donde(self, condicion):
        """Quita el primer nodo cuyo dato cumple `condicion`. True si quitó uno, False si no."""
        anterior = None
        actual = self._cabeza
        while actual is not None:
            if condicion(actual.dato):
                if anterior is None:                  
                    self._cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                if actual is self._ultimo:            
                    self._ultimo = anterior
                self._tamanio -= 1
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def reemplazar_donde(self, condicion, dato):
        """Cambia el dato del primer nodo que cumple `condicion`, sin moverlo de lugar."""
        actual = self._cabeza
        while actual is not None:
            if condicion(actual.dato):
                actual.dato = dato
                return True
            actual = actual.siguiente
        return False

    def __iter__(self):
        """Generador: un for recorre los datos desde la cabeza hasta el final."""
        actual = self._cabeza
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente


DIAS = ("lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo")


class MenuSemanal:
    """Pares (dia, receta) guardados en una ListaEnlazada, en el orden en que se agregaron."""

    def __init__(self):
        self._dias = ListaEnlazada()

    def agregar(self, dia, receta):
        if dia not in DIAS:
            raise ValueError(f"{dia!r} no es un día válido. Días: {', '.join(DIAS)}.")
        # Si el día ya tenía receta se reemplaza en su lugar; si no, va al final.
        if not self._dias.reemplazar_donde(lambda par: par[0] == dia, (dia, receta)):
            self._dias.insertar_al_final((dia, receta))

    def quitar(self, dia):
        if not self._dias.eliminar_donde(lambda par: par[0] == dia):
            raise RecetaNoEncontrada(f"El día {dia!r} no tiene receta.")

    def receta_de(self, dia):
        for d, receta in self._dias:
            if d == dia:
                return receta
        raise RecetaNoEncontrada(f"El día {dia!r} no tiene receta.")

    def __iter__(self):
        return iter(self._dias)  


class LibroRecetas(ejercicio_02.LibroRecetas):
    """Misma interfaz que el LibroRecetas del ejercicio 2, guardado en una ListaEnlazada."""

    def __init__(self):
        self._recetas = ListaEnlazada()

    def agregar(self, receta):
        if not self._recetas.reemplazar_donde(lambda r: r.id == receta.id, receta):
            self._recetas.insertar_al_final(receta)

    def obtener(self, id):
        for receta in self._recetas:
            if receta.id == id:
                return receta
        raise RecetaNoEncontrada(f"No hay ninguna receta con id {id}.")

    def listar(self):
        copia = []
        for receta in self._recetas:
            copia.append(receta)
        return copia

    def cantidad(self):
        return self._recetas.tamanio()


# TEORIA
# En una lista enlazada simple la referencia al último nodo está guardada en el
# atributo `siguiente` del penúltimo; como los nodos no apuntan hacia atrás (y
# _ultimo apunta al último, no al penúltimo), para llegar al penúltimo hay que
# recorrer desde la cabeza hasta el nodo cuyo siguiente es el último: O(n).


if __name__ == "__main__":
    lista = ListaEnlazada()
    for x in (2, 3):
        lista.insertar_al_final(x)
    lista.insertar_al_inicio(1)
    print(list(lista), "tamaño", lista.tamanio())
    print("eliminar_donde(par):", lista.eliminar_donde(lambda x: x % 2 == 0), list(lista))
    print("eliminar_donde(>10):", lista.eliminar_donde(lambda x: x > 10), list(lista))
    print("quitar_primero:", lista.quitar_primero(), list(lista))

    libro = ejercicio_02.libro_examen(LibroRecetas())
    menu = MenuSemanal()
    menu.agregar("lunes", libro.obtener(12))
    menu.agregar("miercoles", libro.obtener(10))
    menu.agregar("lunes", libro.obtener(9))       # reemplaza el lunes
    for dia, receta in menu:
        print(dia, "->", receta)
    menu.quitar("miercoles")
    try:
        menu.receta_de("miercoles")
    except RecetaNoEncontrada as error:
        print("RecetaNoEncontrada:", error)
    try:
        menu.agregar("Lunes", libro.obtener(1))
    except ValueError as error:
        print("ValueError:", error)
