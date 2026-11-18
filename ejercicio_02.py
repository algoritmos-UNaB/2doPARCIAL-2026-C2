class CancionNoEncontradaError(Exception):
    pass

class Biblioteca:
    def __init__(self):
        self.canciones = []

    def agregar(self, cancion):
        self.canciones.append(cancion)
        return cancion

    def cantidad(self):
        return len(self.canciones)

    def obtener(self, id):
        for cancion in self.canciones:
            if cancion.id == id:
                return cancion
        raise CancionNoEncontradaError(
            "No se encontró la canción con ID " + str(id)
        )

    def listar(self):
        resultado = []
        for cancion in self.canciones:
            resultado.append(str(cancion))
        return resultado

    def __iter__(self):
        return iter(self.canciones)

## La biblioteca guarda el catálogo de todas las canciones que se encuentran disponibles y una playlist son canciones seleccionadas para reproducir en un orden.