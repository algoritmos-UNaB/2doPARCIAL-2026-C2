## Ejercicio 2 — Biblioteca (8 pts)

#Definir la clase `Biblioteca`, el catálogo de todas las canciones.

#- `agregar(cancion)` incorpora una canción.
#- `cantidad()` devuelve cuántas hay.
#- `obtener(id)` devuelve la canción con ese `id`. Si no está, lanza `CancionNoEncontradaError`.
#- `listar()` devuelve una lista de strings, uno por canción, usando `__str__`.
#- `__iter__` permite recorrer las canciones con un `for`.

#La playlist no vive en esta clase.

#**Teoría.** En una o dos oraciones: qué guarda la biblioteca y qué guarda una playlist.

#---

class CancionNoEncontradaError(Exception):
    pass
class Biblioteca():
    def __init__(self):
        self.canciones = []
    def agregar(self, cancion):
        self.canciones.append(cancion)
    def cantidad(self):
        return len(self.canciones)
    def obtener(self, id):
        for cancion in self.canciones:
            if cancion.id == id:
                return cancion
        raise CancionNoEncontradaError(f'No se encontro la cancion con la ID{id}')
    
    def listar (self):
        L=[]

        for cancion in self.canciones:
            L.append(str(cancion))
        return L
    def __iter__(self):
        return iter(self.canciones)

#RESPUESTA: La biblioteca es una lista de todas las canciones mientras que una playlist solo mantiene las canciones a ser ejecutadas