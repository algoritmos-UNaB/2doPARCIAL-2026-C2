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
