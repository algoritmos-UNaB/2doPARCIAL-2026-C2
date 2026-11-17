"""Ejercicio 7. Busquedas  lineal y binaria a mano."""

if __package__:
    from .ejercicio_01 import Cancion
    from .ejercicio_02 import CancionNoEncontradaError
else:
    from ejercicio_01 import Cancion
    from ejercicio_02 import CancionNoEncontradaError


class CampoInvalidoError(Exception):
    """El campo solicitado no es uno de los campos de busqueda admitidos."""


def busqueda_lineal(canciones, campo, valor) -> list:
    """Devuelve todas las coincidencias exactas, en el orden original."""
    if campo not in ("titulo", "artista", "genero"):
        raise CampoInvalidoError(
            "El campo de uúsqueda debe ser titulo, artista o genero."
        )

    resultado = []
    for cancion in canciones:
        if getattr(cancion, campo) == valor:
            resultado.append(cancion)
    return resultado


def busqueda_binaria_por_titulo(canciones_ordenadas, titulo) -> Cancion:
    """Busca en una lista que ya esta ordenada ascendentemente por titulo."""
    izquierda = 0
    derecha = len(canciones_ordenadas) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        cancion = canciones_ordenadas[medio]
        if cancion.titulo == titulo:
            return cancion
        if cancion.titulo < titulo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    raise CancionNoEncontradaError(
        f"No se encontro una cancon con el titulo '{titulo}'."
    )


# la lista esta ordenada por titulopara poder descartar una mitad segun la comparacion entre el tutulo buscado yu el titulo
# de la posicion central.
# la busqueda binaria usa 0(log n) y la bsuqueda lienal por artista tiene 0(n), por que recorre todas las canciones
