from ejercicio_01 import Cancion


def ordenar_por_anio_seleccion(canciones) -> list:
    """Selección. Año de mayor a menor."""
    n = len(canciones)

    for i in range(n - 1):
        pos_mayor = i

        for j in range(i + 1, n):
            if canciones[j].anio > canciones[pos_mayor].anio:
                pos_mayor = j

        canciones[i], canciones[pos_mayor] = canciones[pos_mayor], canciones[i]

    return canciones


def ordenar_por_duracion_insercion(canciones) -> list:
    """Inserción. duracion_seg de menor a mayor."""
    for i in range(1, len(canciones)):
        actual = canciones[i]
        j = i - 1

        while j >= 0 and canciones[j].duracion_seg > actual.duracion_seg:
            canciones[j + 1] = canciones[j]
            j -= 1

        canciones[j + 1] = actual

    return canciones



# Los 2 algoritmos tienen una complejidad de peor caso  O(n^2)
# El ordenamiento por inserción es el que conserva el orden relativo de las dos canciones con la misma calve, porque es estable. Selección no te va garantizar esa estabilidad