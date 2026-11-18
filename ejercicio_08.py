"""Ejercicio 8 — Ordenamiento por selección e inserción (sin sorted ni list.sort).

Las dos funciones ordenan la MISMA lista que reciben (en el lugar) y la devuelven.
"""

ORDEN_DIFICULTAD = {"baja": 0, "media": 1, "alta": 2}


def _clave(receta, campo):
    if campo == "tiempo":
        return receta.tiempo_min
    if campo == "dificultad":
        return ORDEN_DIFICULTAD[receta.dificultad]   
    raise ValueError(f"Campo {campo!r} no válido: tiene que ser 'tiempo' o 'dificultad'.")


def _va_antes(a, b, campo, descendente):
    """True si `a` tiene que ir estrictamente antes que `b`. Con claves iguales, False."""
    if descendente:
        return _clave(a, campo) > _clave(b, campo)
    return _clave(a, campo) < _clave(b, campo)


def ordenar_seleccion(recetas, campo, descendente=False):
    """Para cada posición i busca la receta que va primero entre las que faltan y la intercambia con i."""
    _clave_valida(campo)
    n = len(recetas)
    for i in range(n - 1):
        elegida = i
        for j in range(i + 1, n):
            if _va_antes(recetas[j], recetas[elegida], campo, descendente):
                elegida = j
        if elegida != i:
            recetas[i], recetas[elegida] = recetas[elegida], recetas[i]
    return recetas


def ordenar_insercion(recetas, campo, descendente=False):
    """Toma cada receta y la corre a la izquierda mientras la anterior vaya después que ella."""
    _clave_valida(campo)
    for i in range(1, len(recetas)):
        actual = recetas[i]
        j = i - 1
    
        while j >= 0 and _va_antes(actual, recetas[j], campo, descendente):
            recetas[j + 1] = recetas[j]
            j -= 1
        recetas[j + 1] = actual
    return recetas


def _clave_valida(campo):
    if campo not in ("tiempo", "dificultad"):
        raise ValueError(f"Campo {campo!r} no válido: tiene que ser 'tiempo' o 'dificultad'.")


# TEORIA
# El estable es inserción (selección no lo es). Un ordenamiento es estable si
# los elementos con la misma clave quedan, entre sí, en el mismo orden relativo
# que tenían antes de ordenar. Ejemplo de por qué selección no lo es: con
# claves [2a, 2b, 1], el primer intercambio pone el 1 en la posición 0 y manda
# 2a al final: [1, 2b, 2a], y 2a quedó después de 2b.


if __name__ == "__main__":
    from ejercicio_02 import libro_examen
    from ejercicio_04 import LibroRecetas

    libro = libro_examen(LibroRecetas())

    recetas = libro.listar()
    print("selección por tiempo, ascendente:")
    for receta in ordenar_seleccion(recetas, "tiempo", descendente=False):
        print("  ", receta)

    recetas = libro.listar()
    print("inserción por dificultad, ascendente:")
    for receta in ordenar_insercion(recetas, "dificultad", descendente=False):
        print("  ", receta)

    recetas = libro.listar()
    print("inserción por tiempo, descendente:")
    for receta in ordenar_insercion(recetas, "tiempo", descendente=True):
        print("  ", receta)
