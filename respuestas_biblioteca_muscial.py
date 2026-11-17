## Ejercicio 1 — Canción (8 pts)

class Cancion:
    def __init__(self, id, titulo, artista, album, genero, anio, duracion_seg):
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.genero = genero
        self.anio = anio
        self.duracion_seg = duracion_seg

    def duracion_mmss(self):
        minutos = self.duracion_seg // 60
        segundos = self.duracion_seg % 60
        return f"{minutos}:{segundos:02d}"

    def __str__(self):
        return (
            f"#{self.id} {self.titulo} | {self.artista} | "
            f"{self.anio} | {self.duracion_mmss()}"
        )

    def __eq__(self, other):
        if not isinstance(other, Cancion):
            return NotImplemented
        return self.id == other.id

# **Teoría.**
# Guardar la duración como segundos enteros permite operarla como con `duracion_mmss, lo que no
# sería posible en formato de cadena de texto


## Ejercicio 2 — Biblioteca (8 pts)

class CancionNoEncontradaError(Exception):
    def __init__(self, id):
        super().__init__(f"No se encontró la canción con id {id}.")
        self.id = id

class Biblioteca:
    def __init__(self):
        self._canciones = []

    def agregar(self, cancion):
        self._canciones.append(cancion)

    def cantidad(self):
        return len(self._canciones)

    def obtener(self, id):
        for cancion in self._canciones:
            if cancion.id == id:
                return cancion
        raise CancionNoEncontradaError(id)

    def listar(self):
        return [str(cancion) for cancion in self._canciones]

    def __iter__(self):
        return iter(self._canciones)

# **Teoría.**
# La biblioteca guarda el catalogo completo y la playlist, una seleccion de ese catalogo

## Ejercicio 3 — Versiones (12 pts)

def versiones_de(biblioteca, versiones, cancion_id):
    """Lista de (titulo, tipo) de todo lo derivado, sin incluir la original."""
    biblioteca.obtener(cancion_id)  # valida que exista; lanza si no

    directas = [
        (cid, tipo) for (cid, padre, tipo) in versiones if padre == cancion_id
    ]
    directas.sort(key=lambda par: par[0])

    resultado = []
    for cid, tipo in directas:
        titulo = biblioteca.obtener(cid).titulo
        resultado.append((titulo, tipo))
        resultado.extend(versiones_de(biblioteca, versiones, cid))
    return resultado

## Ejercicio 4 — Playlist sobre lista enlazada (14 pts)

class Nodo:
    def __init__(self, dato, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente

class ListaEnlazada:
    def __init__(self):
        self._primero = None
        self._tamanio = 0

    def esta_vacia(self):
        return self._primero is None

    def tamanio(self):
        return self._tamanio

    def insertar_al_inicio(self, dato):
        self._primero = Nodo(dato, self._primero)
        self._tamanio += 1

    def insertar_al_final(self, dato):
        nuevo = Nodo(dato)
        if self._primero is None:
            self._primero = nuevo
        else:
            actual = self._primero
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self._tamanio += 1

    def quitar_primero(self):
        if self._primero is None:
            raise IndexError("La lista está vacía.")
        dato = self._primero.dato
        self._primero = self._primero.siguiente
        self._tamanio -= 1
        return dato

    def __iter__(self):
        actual = self._primero
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente

class Playlist:
    def __init__(self):
        self._canciones = ListaEnlazada()

    def agregar(self, cancion):
        self._canciones.insertar_al_final(cancion)

    def quitar(self, id):
        anterior = None
        actual = self._canciones._primero
        while actual is not None:
            if actual.dato.id == id:
                if anterior is None:
                    self._canciones.quitar_primero()
                else:
                    anterior.siguiente = actual.siguiente
                    self._canciones._tamanio -= 1
                return
            anterior = actual
            actual = actual.siguiente
        raise CancionNoEncontradaError(id)

    def listar(self):
        return [str(cancion) for cancion in self._canciones]

    def duracion_total(self):
        total = 0
        for cancion in self._canciones:
            total += cancion.duracion_seg
        return total

# **Teoría.**
# Para insertar al final cuando ya hay n elementos se recorren n nodos:
# se visita el primero y se avanza por `siguiente` hasta llegar al último
# (el que tiene siguiente == None), y se engancha el nuevo nodo ahí.
# Es O(n) porque la lista solo guarda referencia al primero, no al último.

## Ejercicio 5 — Historial de reproducción (10 pts)

class PilaVaciaError(Exception):
    def __init__(self):
        super().__init__("La pila está vacía.")


class Pila:
    def __init__(self):
        self._lista = ListaEnlazada()

    def apilar(self, dato):
        self._lista.insertar_al_inicio(dato)

    def desapilar(self):
        if self._lista.esta_vacia():
            raise PilaVaciaError()
        return self._lista.quitar_primero()

    def ver_tope(self):
        if self._lista.esta_vacia():
            raise PilaVaciaError()
        return self._lista._primero.dato

    def esta_vacia(self):
        return self._lista.esta_vacia()


class HistorialReproduccion:
    def __init__(self):
        self._pila = Pila()

    def registrar(self, cancion):
        self._pila.apilar(cancion)

    def anterior(self):
        return self._pila.desapilar()

    def ultima(self):
        return self._pila.ver_tope()

# **Teoría.**
# Devuelve "De musica ligera", fue el ultimo elemento cargado, por ende el primero de la pila en salir al desapilar
