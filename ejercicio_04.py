
from ejercicio_02 import RecetaNoEncontrada


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.primero = None

    def esta_vacia(self):
        return self.primero is None

    def tamanio(self):
        contador = 0
        actual = self.primero

        while actual is not None:
            contador += 1
            actual = actual.siguiente

        return contador

    def insertar_al_final(self, dato):
        nuevo = Nodo(dato)

        if self.esta_vacia():
            self.primero = nuevo
            return

        actual = self.primero

        while actual.siguiente is not None:
            actual = actual.siguiente

        actual.siguiente = nuevo

    def insertar_al_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.primero
        self.primero = nuevo

    def quitar_primero(self):
        if self.esta_vacia():
            return None

        dato = self.primero.dato
        self.primero = self.primero.siguiente

        return dato

    def eliminar_donde(self, condicion):
        actual = self.primero
        anterior = None

        while actual is not None:
            if condicion(actual.dato):
                if anterior is None:
                    self.primero = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente

                return True

            anterior = actual
            actual = actual.siguiente

        return False

    def __iter__(self):
        actual = self.primero

        while actual is not None:
            yield actual.dato
            actual = actual.siguiente


class MenuSemanal:
    DIAS = [
        "lunes", "martes", "miercoles", "jueves",
        "viernes", "sabado", "domingo"
    ]

    def __init__(self):
        self.menu = ListaEnlazada()

    def agregar(self, dia, receta):
        if dia not in self.DIAS:
            raise ValueError("Dia invalido")

        actual = self.menu.primero

        while actual is not None:
            if actual.dato[0] == dia:
                actual.dato = (dia, receta)
                return

            actual = actual.siguiente

        self.menu.insertar_al_final((dia, receta))

    def quitar(self, dia):
        eliminado = self.menu.eliminar_donde(
            lambda par: par[0] == dia
        )

        if not eliminado:
            raise RecetaNoEncontrada("No hay receta para ese dia")

    def receta_de(self, dia):
        for dia_menu, receta in self.menu:
            if dia_menu == dia:
                return receta

        raise RecetaNoEncontrada("No hay receta para ese dia")

    def __iter__(self):
        return iter(self.menu)


# TEORIA
# En una lista enlazada simple no se guarda directamente la referencia al penultimo nodo. Hay que recorrer la lista desde el primero para encontrarlo.
