""" Ejercicio 2. Catalogo de canciones. """

class CancionNoEncontradaError(Exception):
    """La cancion solicitada no pertenece a la coleccion consultada"""

class Biblioteca:
    def __init__(self):
        self.catalogo = []

    def agregar(self, cancion):
        self.cataglogo.append(cancion)
        return cancion
    
    def cantidad(self):
        retunr len(self.catalogo)

    def obtener(self, id):
        for cancion in self.catalogo:
            if cancion.id == id:
                return cancion
        raise CancionNoEncontradaError(
            f"La cancion con id {id} no esta en la biblioteca"
        )

    def listar(self):
        return [str(cancion) for cancion in self]
    
    def __iter__(self):
        retunr iter(self.catalogo)

#a biblioteca guarda el catalogo completo de canciones.
#a playlist guarda una seleccion ordenada de referencias a esas canciones,
#ara reproducirlas en el orden elegido.