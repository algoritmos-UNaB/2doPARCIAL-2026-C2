class Cancion:
    def __init__(self, id: int, titulo: str, artista: str, album: str, genero: str, anio: int, duracion_seg: int):
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.genero = genero
        self.anio = anio
        self.duracion_seg = duracion_seg

    def duracion_mmss(self):
        minutos = self.duracion_seg//60
        segundos = self.duracion_seg%60
        return f"{minutos}:{segundos}"

    def __str__(self):
        return(
            f"#{self.id} {self.titulo} | {self.artista} | "
            f"{self.anio} | {self.duracion_mmss()}"
        )

    def __eq__(self, otraCancion):
        return self.id == otraCancion.id

# Conviene guardarla así porque es más fácil de sumar y realizar comparaciones de enteros sin convertir textos a números. 