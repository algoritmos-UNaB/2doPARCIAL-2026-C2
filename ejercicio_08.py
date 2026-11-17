"""Ejercicio 8. Ordenamientos in-place por seleccion e insercion."""


def ordenar_por_anio_seleccion(canciones) -> list:
    """Ordena por año de mayor a menor mediante seleccion."""
    for i in range(len(canciones) - 1):
        posicion_mayor = i
        for j in range(i + 1, len(canciones)):
            if canciones[j].anio > canciones[posicion_mayor].anio:
                posicion_mayor = j
        canciones[i], canciones[posicion_mayor] = (
            canciones[posicion_mayor], canciones[i]
        )
    return canciones


def ordenar_por_duracion_insercion(canciones) -> list:
    """Ordena por duracion de menor a mayor mediante insercion estable."""
    for i in range(1, len(canciones)):
        actual = canciones[i]
        j = i - 1
        while j >= 0 and canciones[j].duracion_seg > actual.duracion_seg:
            canciones[j + 1] = canciones[j]
            j -= 1
        canciones[j + 1] = actual
    return canciones

# Seleccion e insercion tienen complejidad O(n2) en el peor caso.
# insercion conserva el orden relativo de canciones con la misma duracion por que desplaza solamente las de duracion mayor.
#sleccion puede alterar el orden relatico de canciones con el mismo año, al intercambiar elementos alejados.
