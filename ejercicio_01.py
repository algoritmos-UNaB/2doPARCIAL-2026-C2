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
        minutos, segundos = divmod(self.duracion_seg, 60)
        return f"{minutos}:{segundos:02d}"

    def __str__(self):
        return (f"#{self.id} {self.titulo} | {self.artista} | "
                f "{self.anio} | {self.duracion_mmss()}")

    def __eq__(self, otra):
        if not isinstance(otra, Cancion):
            return self.id == otra.id

    def __hash__(self):
        return hash(self.id)


# Teoria:
# La duración se guarda en segundos enteros porque así se puede sumar, comparar y ordenar directamente (duracion_total, ordenar por duración).
# El formato "m:ss" es sólo la presentación, ya que se deriva del número, mientras que un string obligaría a desarmar el texto para volver a obtener el número y podría quedar inconsistente.
