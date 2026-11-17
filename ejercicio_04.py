from ejercicio_02 import PokemonNoEncontrado

class EquipoLLenoError(exception):
    pass

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def esta_vacia(self):
        return self.cabeza is None

    def tamanio(self):
        cantidad = 0
        actual = self.cabeza

        while actual is not None:
            cantidad += 1
            actual = actual.siguiente

        return cantidad

    def insertar_al_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def insertar_al_final(self, dato):
        nuevo = Nodo(dato)

        if self.esta_vacia():
            self.cabeza = nuevo
            return
        
        actual = self.cabeza

        while actual.siguiente is not None:
            acutal = actual.siguiente

        actual.siguiente = nuevo

    def quitar_primero(self):
        if self.esta_vacia():
            raise IndexError("La lista esta vacía")

        dato = self.cabeza.dato
        self.cabeza = self.cabeza.siguiente
        return dato

    def eliminar(self, id):
        actual = self.cabeza
        anterior = None

        while actual is not None:
            if actual.dato.id == id:
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente

                return True

            anterior = actual
            actual = actual.siguiente
        
        return False

    def buscar(self, id):
        actual = self.cabeza

        while actual is not None:
            if actual.dato.id == id:
                return actual.dato

            actual = actual.siguiente

        return None

    def __iter__(self):
        actual = self.cabeza

        while actual is not None:
            yield actual.dato
            actual = actual.siguiente
    
class Equipo:

    def __init__(self):
        self.pokemones = ListaEnlazada()

    def agregar(self, pokemon):
        if self.cantidad() >= 6:
            raise EquipoLlenoError("El equipo ya tiene 6 Pokémon")

        self.pokemones.insertar_al_final(pokemon)

    def quitar(self, id):
        if not self.pokemones.eliminar(id):
            raise PokemonNoEncontrado(
                f"No existe el Pokémon con id {id} en el equipo"
            )

    def cantidad(self):
        return self.pokemones.tamanio()

    def __iter__(self):
        return iter(self.pokemones)

# El ultimo nodo no guarda una referencia al penultimo por que cada nodo apunta al siguiente y para encontrar el penultimo hay que recorrer desde la cabeza conservando la referencia del nodo anterior.