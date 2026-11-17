## Ejercicio 1 — Canción (8 pts)

#Definir la clase `Cancion`.

#Atributos: `id` (int), `titulo` (str), `artista` (str), `album` (str), `genero` (str), `anio` (int), `duracion_seg` (int).

#Métodos:

#- `duracion_mmss()` devuelve la duración como `m:ss`. `316` → `"5:16"`, `65` → `"1:05"`, `59` → `"0:59"`.
#- `__str__` devuelve `#12 Jijiji | Patricio Rey y sus Redonditos de Ricota | 1988 | 5:16`.
#- `__eq__` compara por `id`.

#**Teoría.** La duración se guarda en segundos enteros y `duracion_mmss` la calcula. Explicar en dos oraciones por qué conviene guardarla así y no en un string `"5:16"`.

#---


class Cancion:
    def __init__(self, id, titulo, artista, album, genero, anio, duracion_seg):
        self.id= id
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.genero = genero
        self.anio = int(anio)
        self.duracion_seg = int(duracion_seg)
    def duracion_mmss(self):
        minutos = self.duracion_seg // 60
        segundos = self.duracion_seg % 60
        return f'{minutos}:{segundos}'
    def __str__(self):
        return f'#{self.id} {self.titulo} | {self.artista} | {self.anio} | {self.duracion_mmss}'
    def __eq__(self, otro):
        return self.id == otro.id

# RESPUESTA: Es mas facil para operar funciones matemáticas o comparar. Asi tambien convertirla en m:ss con una funcion como la implementada