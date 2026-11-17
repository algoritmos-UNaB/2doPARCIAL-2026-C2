from ejercicio_01 import Cancion


class CancionNoEncontradaError(Exception):
    def __init__(self, id_cancion):
        super().__init__(f"Canción con id {id_cancion} no encontrada.")


class Biblioteca:
    def __init__(self):
        self._canciones = []

    def agregar(self, cancion):
        self._canciones.append(cancion)

    def cantidad(self):
        return len(self._canciones)

    def obtener(self, id_cancion):
        for cancion in self._canciones:
            if cancion.id == id_cancion:
                return cancion
        raise CancionNoEncontradaError(id_cancion)

    def listar(self):
        return [str(cancion) for cancion in self._canciones]

    def __iter__(self):
        return iter(self._canciones)


#La biblioteca va guardar el catálogo completo de canciones disponibles para poder consultarlas cuando sea necesario. En cambio la playlist guarda una selección de canciones que elegimos para reproducirlas en un orden determinado