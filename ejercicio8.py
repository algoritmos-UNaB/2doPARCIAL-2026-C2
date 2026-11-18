from ejercicio2 import Cancion


def ordenar_por_anio_seleccion(canciones):
    n = len(canciones)
    for i in range(n - 1):
        indice_mayor = i
        for j in range(i + 1, n):
            if canciones[j].anio > canciones[indice_mayor].anio:
                indice_mayor = j
        if indice_mayor != i:
            canciones[i], canciones[indice_mayor] = canciones[indice_mayor], canciones[i]
    return canciones


def ordenar_por_duracion_insercion(canciones):
    for i in range(1, len(canciones)):
        actual = canciones[i]
        j = i - 1
        while j >= 0 and canciones[j].duracion_seg > actual.duracion_seg:
            canciones[j + 1] = canciones[j]
            j -= 1
        canciones[j + 1] = actual
    return canciones


# **Teoría.**
#selección es O(n²) siempre; inserción es O(n²) en el peor caso (y O(n) si ya está casi ordenada). 
#El de inserción conserva el orden relativo de dos canciones con la misma clave (es estable); selección no, porque el intercambio puede cruzar elementos iguales.
