from ejercicio_01 import Cancion

class CancionNoEncontradaError(Exception):
    """Se busca una cancion por id (o titulo) y no existe."""

    def init(self, mensaje="La cancion no fue encontrada"):
        super().init(mensaje)

 class Biblioteca:
    def init(self):
        self._canciones = []

    def agregar(self, cancion):
        self._canciones.append(cancion)

    def cantidad(self):
        return len(self._canciones)

    def obtener(self, id):
        for cancion in self._canciones:
            if cancion.id == id:
                return cancion
        raise CancionNoEncontradaError(f"No existe una cancion con id {id} en la biblioteca")

    def listar(self):
        return [str(cancion) for cancion in self._canciones]

    def iter(self):
        return iter(self._canciones)

 # TEORIA
 # La biblioteca guarda el catalogo completo de canciones (todas las que existen en
 # el sistema). Una playlist guarda solo una seleccion ordenada de esas canciones,
 # elegida por el usuario, y puede cambiar sin afectar al catalogo.
