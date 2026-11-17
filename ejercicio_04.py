
class Nodo:
    def _init_(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def _init_(self):
        self.primero = None
        self._tamanio = 0

    def esta_vacia(self):
        return self.primero is None

    def tamanio(self):
        return self._tamanio

    def insertar_al_final(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self.primero = nuevo
        else:
            actual = self.primero
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self._tamanio += 1

    def insertar_al_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.primero
        self.primero = nuevo
        self._tamanio += 1

    def quitar_primero(self):
        if self.esta_vacia():
            raise Exception("La lista está vacía.")
        dato = self.primero.dato
        self.primero = self.primero.siguiente
        self._tamanio -= 1
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
                self._tamanio -= 1
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def _iter_(self):
        actual = self.primero
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente


DIAS_SEMANA = {"lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"}

class MenuSemanal:
    def _init_(self):
        self.dias = ListaEnlazada()

    def agregar(self, dia, receta):
        if dia not in DIAS_SEMANA:
            raise ValueError(f"Día inválido: {dia}")
        self.dias.eliminar_donde(lambda par: par[0] == dia)
        self.dias.insertar_al_final((dia, receta))

    def quitar(self, dia):
        if not self.dias.eliminar_donde(lambda par: par[0] == dia):
            raise RecetaNoEncontrada(f"El día {dia} no tiene receta.")

    def receta_de(self, dia):
        for d, r in self.dias:
            if d == dia:
                return r
        raise RecetaNoEncontrada(f"El día {dia} no tiene receta asignada.")

    def _iter_(self):
        return iter(self.dias)

# TEORIA: En una lista enlazada simple, la referencia al penúltimo nodo no está guardada directamente; se debe recorrer la lista desde el inicio llevando el rastro del nodo anterior para encontrarlo.