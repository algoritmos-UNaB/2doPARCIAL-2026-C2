"""Ejercicio 7 — Búsqueda lineal y binaria sobre objetos Receta."""

CAMPOS_LINEAL = ("nombre", "categoria", "ingrediente")


def _usa_ingrediente(receta_id, ingredientes, nombre_ingrediente):
    for rid, nombre, _cantidad, _unidad in ingredientes:
        if rid == receta_id and nombre == nombre_ingrediente:
            return True
    return False


def busqueda_lineal(recetas, ingredientes, campo, valor):
    """Recorre todas las recetas y devuelve la lista de las que coinciden (en el orden de `recetas`)."""
    if campo not in CAMPOS_LINEAL:
        raise ValueError(f"Campo {campo!r} no válido. Opciones: {', '.join(CAMPOS_LINEAL)}.")
    coincidencias = []
    for receta in recetas:
        if campo == "nombre":
            coincide = receta.nombre == valor
        elif campo == "categoria":
            coincide = receta.categoria == valor
        else:  # "ingrediente"
            coincide = _usa_ingrediente(receta.id, ingredientes, valor)
        if coincide:
            coincidencias.append(receta)
    return coincidencias


def busqueda_binaria(recetas, campo, valor):
    """Busca por nombre en una lista YA ORDENADA por nombre. Devuelve la Receta o None.

    En cada vuelta mira el elemento del medio y descarta la mitad donde no puede
    estar: O(log n). Corta apenas lo encuentra o cuando el rango queda vacío.
    """
    if campo != "nombre":
        raise ValueError("La búsqueda binaria solo busca por 'nombre'.")
    izquierda = 0
    derecha = len(recetas) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        nombre_medio = recetas[medio].nombre
        if nombre_medio == valor:
            return recetas[medio]          
        if nombre_medio < valor:
            izquierda = medio + 1          
        else:
            derecha = medio - 1            
    return None                            


# TEORIA
# No: la binaria elige con qué mitad seguir comparando nombres, y si la lista
# está ordenada por tiempo esa comparación no indica de qué lado está el nombre,
# así que puede descartar la mitad donde estaba y devolver None aunque exista.


if __name__ == "__main__":
    from ejercicio_02 import libro_examen
    from ejercicio_03 import INGREDIENTES_EXAMEN
    from ejercicio_04 import LibroRecetas

    recetas = libro_examen(LibroRecetas()).listar()
    print("categoria salsa:", busqueda_lineal(recetas, INGREDIENTES_EXAMEN, "categoria", "salsa"))
    print("ingrediente ajo:", busqueda_lineal(recetas, INGREDIENTES_EXAMEN, "ingrediente", "ajo"))
    print("nombre Pizza:", busqueda_lineal(recetas, INGREDIENTES_EXAMEN, "nombre", "Pizza"))

    # Para la binaria, la lista tiene que estar ordenada por nombre (a mano, sin sorted):
    por_nombre = []
    for receta in recetas:
        i = len(por_nombre)
        por_nombre.append(receta)
        while i > 0 and por_nombre[i - 1].nombre > receta.nombre:
            por_nombre[i] = por_nombre[i - 1]
            i -= 1
        por_nombre[i] = receta
    print("binaria Locro:", busqueda_binaria(por_nombre, "nombre", "Locro"))
    print("binaria Pizza:", busqueda_binaria(por_nombre, "nombre", "Pizza"))
