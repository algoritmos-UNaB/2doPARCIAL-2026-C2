from ejercicio_02 import RecetaNoEncontrada


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self._tamanio = 0

    def esta_vacia(self):
        return self.cabeza is None

    def tamanio(self):
        return self._tamanio

    def insertar_al_inicio(self, dato):
        nuevo = Nodo(dato)

        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

        if self.cola is None:
            self.cola = nuevo

        self._tamanio += 1

    def insertar_al_final(self, dato):
        nuevo = Nodo(dato)

        if self.cola is None:
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            self.cola = nuevo

        self._tamanio += 1

    def quitar_primero(self):
        if self.esta_vacia():
            raise IndexError("La lista está vacía")

        dato = self.cabeza.dato
        self.cabeza = self.cabeza.siguiente

        self._tamanio -= 1

        if self.cabeza is None:
            self.cola = None

        return dato

    def eliminar_donde(self, condicion):
        anterior = None
        actual = self.cabeza

        while actual is not None:

            if condicion(actual.dato):

                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente

                if actual is self.cola:
                    self.cola = anterior

                self._tamanio -= 1
                return True

            anterior = actual
            actual = actual.siguiente

        return False

    def __iter__(self):
        actual = self.cabeza

        while actual is not None:
            yield actual.dato
            actual = actual.siguiente


class MenuSemanal:

    DIAS = [
        "lunes",
        "martes",
        "miercoles",
        "jueves",
        "viernes",
        "sabado",
        "domingo"
    ]

    def __init__(self):
        self.items = ListaEnlazada()

    def agregar(self, dia, receta):

        if dia not in self.DIAS:
            raise ValueError("Día inválido")

        actual = self.items.cabeza

        while actual is not None:

            dia_actual, receta_actual = actual.dato

            if dia_actual == dia:
                actual.dato = (dia, receta)
                return

            actual = actual.siguiente

        self.items.insertar_al_final((dia, receta))

    def quitar(self, dia):

        if dia not in self.DIAS:
            raise ValueError("Día inválido")

        eliminado = self.items.eliminar_donde(
            lambda par: par[0] == dia
        )

        if not eliminado:
            raise RecetaNoEncontrada(
                f"No hay receta para {dia}"
            )

    def receta_de(self, dia):

        if dia not in self.DIAS:
            raise ValueError("Día inválido")

        for dia_actual, receta in self.items:

            if dia_actual == dia:
                return receta

        raise RecetaNoEncontrada(
            f"No hay receta para {dia}"
        )

    def __iter__(self):
        return iter(self.items)


# TEORIA:
# La referencia al penúltimo nodo se encuentra recorriendo
# la lista desde la cabeza hasta encontrar el nodo anterior al último.