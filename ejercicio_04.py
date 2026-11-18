class Nodo:
    def __init__(self, dato, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente

class ListaEnlazada:
    def __init__(self):
        self.primero = None

    def esta_vacia(self) -> bool:
        return self.primero is None

    def tamanio(self) -> int:
        cantidad = 0
        actual = self.primero
        while actual is not None:
            cantidad = cantidad+1
            actual = actual.siguiente
        return cantidad

    def insertar_al_inicio(self, dato):
        self.primero = Nodo(dato, self.primero)
        return dato

    def insertar_al_final(self, dato):
        if self.esta_vacia():
            return self.insertar_al_inicio(dato)
        actual = self.primero

        while actual.siguiente is not None:
            actual = actual.siguiente

        actual.siguiente = Nodo(dato)
        return dato

    def quitar_primero(self):
        if self.esta_vacia():
            return None
        dato = self.primero.dato
        self.primero = self.primero.siguiente
        return dato

    def __iter__(self):
        actual. self.primero
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente

class Playlist:
    def __init__(self):
        self.canciones = ListaEnlazada()

    def agregar(self, cancion):
        return self.canciones.insertar_al_final(cancion)

    def quitar(self, id):
        anterior = None
        actual = self.canciones.primero
        while actual is not None:
            if actual.dato.id == id:
                if anterior is None:
                    return self.canciones.quitar_primero()
                
                anterior.siguiente = actual.siguiente
                return actual.dato
            
            anterior = actual
            actual = actual.siguiente
        
        raise CancionNoEncontradaError("No se encontró la canción con ID " + str(id) + " en la playlist")

    def listar(self):
        resultado = []

        for cancion in self.canciones:
            resultado.append(str(cancion))

        return resultado

    def duracion_total(self):
        total = 0

        for cancion in self.canciones:
            total = total+cancion.duracion_seg

        return total    

# Se recorren todos los nodos para llegar al último e insertar el nuevo elemento