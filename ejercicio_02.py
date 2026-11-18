from ejercicio_01 import Cancion

class CancionNoEncontradaError(Exception):
    def __init__(self, mensaje="La cancion no fue encontrada"):
        super().__init__(mensaje)


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
        raise CancionNoEncontradaError(
            f"No existe una canción con id {id} en la biblioteca")

    def listar(self):
        return [str(cancion) for cancion in self._canciones]

    def __iter__(self):
        return iter(self._canciones)


# Teoria:
# La biblioteca guarda el catálogo completo, es decir, todas las canciones que existen, cada una con sus datos. 
# Una playlist guarda solo una selección ordenada de canciones que armó el ususario (un subconjunto del catálogo).