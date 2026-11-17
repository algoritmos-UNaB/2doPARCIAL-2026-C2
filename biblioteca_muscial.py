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
