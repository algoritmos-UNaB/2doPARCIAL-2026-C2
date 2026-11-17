
from ejercicio_01 import Cancion
from ejercicio_02 import CancionNoEncontradaError


def busqueda_lineal(canciones, campo, valor) -> list:
    resultado = []

    for cancion in canciones:
        if getattr(cancion, campo) == valor:
            resultado.append(cancion)

    return resultado


def busqueda_binaria_por_titulo(canciones_ordenadas, titulo) -> Cancion:
    izq = 0
    der = len(canciones_ordenadas) - 1

    while izq <= der:
        medio = (izq + der) // 2
        titulo_medio = canciones_ordenadas[medio].titulo

        if titulo_medio == titulo:
            return canciones_ordenadas[medio]
        elif titulo_medio < titulo:
            izq = medio + 1
        else:
            der = medio - 1

    raise CancionNoEncontradaError(titulo)


# La búsqueda binaria necesita que la lista esté ordenada por título para poder descartar la mitad izquierda o derecha en cada comparación.
# Su complejidad para n canciones es O(log n), mientras que en la búsqueda lineal por artista tiene complejidad O(n) porque recorre la lista
