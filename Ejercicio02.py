class Biblioteca
    def __init__(self):
        self.canciones = {}
        self.canciones[cancion.id] = cancion
    def agregar(self, cancion):
        self.canciones[cancion.id] = cancion    
    def cantidad(self):
        return len(self.canciones)
    def obtener(self, id):
    try:
        return self.canciones[id]
    except KeyError:
        raise CancionNoEncontradaError(f"No se encontró la canción con id {id}")

    def listar(self):
        return [str(cancion) for cancion in self.canciones.values()]
    
    def __iter__(self):
        return iter(self.canciones.values())


#Teoría. En una o dos oraciones: qué guarda la biblioteca y qué guarda una playlist.
#Rta: La Biblioteca guarda toda la informacion disponible, en cambio la playlist solo lo que nosotros elijamos repoducir.
