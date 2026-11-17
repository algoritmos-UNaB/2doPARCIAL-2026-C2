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
