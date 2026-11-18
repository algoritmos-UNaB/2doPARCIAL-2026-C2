def ordenar_por_anio_seleccion(canciones) -> list:
    """Selección. Año de mayor a menor."""
    n = len(canciones)
    for i in range(n - 1):
        indice_mayor = i
        for j in range(i + 1, n):
            if canciones[j].anio > canciones[indice_mayor].anio:
                indice_mayor = j
        if indice_mayor != i:
            canciones[i], canciones[indice_mayor] = canciones[indice_mayor], canciones[i]
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


# Teoria:
# Peor caso: selección O(n^2) e inserción O(n^2).
# El que conserva el orden relativo de claves iguales (estable) es INSERCIÓN:
# solo desplaza mientras el anterior sea estrictamente mayor, así que los iguales
# no se cruzan. SELECCIÓN intercambia elementos lejanos y puede alterar ese orden.