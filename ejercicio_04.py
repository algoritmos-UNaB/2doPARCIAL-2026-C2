from ejercicio_02 import PokemonNoEncontrado

class EquipoLlenoError(Exception):
    pass

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.cantidad = 0

    def esta_vacia(self):
        return self.primero is None

    def tamanio(self):
        return self.cantidad

    def insertar_al_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.primero
        self.primero = nuevo
        self.cantidad += 1

    def insertar_al_final(self, dato):
        nuevo = Nodo(dato)
        if self.primero is None:
            self.primero = nuevo
        else:
            actual = self.primero
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self.cantidad += 1

    def quitar_primero(self):
        if self.primero is None:
            return None
        nodo = self.primero
        self.primero = nodo.siguiente
        nodo.siguiente = None
        self.cantidad -= 1
        return nodo.dato

    def eliminar(self, id):
        anterior = None
        actual = self.primero
        while actual is not None:
            if actual.dato.id == id:
                if anterior is None:
                    self.primero = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                actual.siguiente = None
                self.cantidad -= 1
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def buscar(self, id):
        actual = self.primero
        while actual is not None:
            if actual.dato.id == id:
                return actual.dato
            actual = actual.siguiente
        return None

    def __iter__(self):
        actual = self.primero
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente


class Equipo:
    MAXIMO = 6

    def __init__(self):
        self.pokemones = ListaEnlazada()

    def agregar(self, pokemon):
        if self.pokemones.tamanio() >= Equipo.MAXIMO:
            raise EquipoLlenoError("El equipo ya tiene 6 pokemones")
        self.pokemones.insertar_al_final(pokemon)

    def quitar(self, id):
        if not self.pokemones.eliminar(id):
            raise PokemonNoEncontrado(f"No existe el pokemon con id {id} en el equipo")

    def cantidad(self):
        return self.pokemones.tamanio()

    def __iter__(self):
        return iter(self.pokemones)


# TEORIA
# La referencia no esta guardada y no se puede saber directamente
# hay que recorrer toda la lista hasta encontrar el "siguiente" que me interese y que sea el ultimo en este caso