from ejercicio2 import Cancion, CancionNoEncontradaError


def busqueda_lineal(canciones, campo, valor):
    campos_validos = ("titulo", "artista", "genero")
    if campo not in campos_validos:
        raise ValueError(f"Campo inválido: {campo}. Usar uno de {campos_validos}.")
    return [c for c in canciones if getattr(c, campo) == valor]


def busqueda_binaria_por_titulo(canciones_ordenadas, titulo):
    inicio = 0
    fin = len(canciones_ordenadas) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        actual = canciones_ordenadas[medio].titulo
        if actual == titulo:
            return canciones_ordenadas[medio]
        elif actual < titulo:
            inicio = medio + 1
        else:
            fin = medio - 1
    raise CancionNoEncontradaError(titulo)


# **Teoría.**
# busqueda_binaria_por_titulo pide la lista ordenada por título porque en
# cada paso descarta la mitad comparando el título del medio con el buscado;
# sin orden, esa comparación no dice en qué mitad seguir.
#
# Complejidad: la binaria es O(log n); la búsqueda lineal por artista es O(n).
