class Cancion:
    def __init__(self, id, titulo, artista, album, genero, anio, duracion_seg):
        self.id = int(id)
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.genero = genero
        self.anio = int(anio)
        self.duracion_seg = int(duracion_seg)
    def duracion_mmss(self):
        minutos, segundos = divmod(self.duracion_seg, 60)
        return f"{minutos}:{segundos:02d}"

    def __str__(self):
        return f"#{self.id} {self.titulo} | {self.artista} | {self.anio} | {self.duracion_mmss()}"

    def __eq__(self, other):
        return isinstance(other, Cancion) and self.id == other.id


# Al almacenar los segundos como números enteros, resultan más fáciles las operaciones matemáticas, como calcular cuánto dura en total una playlist o comparar la duración entre canciones. Además, evitamos tener que convertir un texto como "5:16" cada vez que necesitamos hacer algún cálculo y podemos mostrar la duración en formato minutos y segundos cuando sea necesario