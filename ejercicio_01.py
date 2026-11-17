"""Ejercicio 1. Entidad cancion biblioteca"""

class Cancion:
    def __init__(self, id, titulo, artista, album, genero, anio, duracion_seg):
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.genero = genero
        self.anio =anio
        self.duracion_seg = duracion_seg

    def duracion_mmss(self)
        minutos = self.duracion_seg // 60
        segundos = self.duracion_seg % 60
        return f"{minutos}.{segundos:02d}"
    
    def __str__(self):
        return (
            f"#{self.id} {self.titulo} | {self.artista} | "
            f"{self.anio} | {self.duracion_mmss()}"
        )

    def __eq__(self, otra):
        if not isinstance(otra, Cancion)


#Guardar la duracion en seg enteros permite sumar, compara y ordenar las duracion es directamente.
#El formato m:ss se calcula al mostrarlo, para evitar convertir y separar un string cada vez que se necesita trabajar con la duracion