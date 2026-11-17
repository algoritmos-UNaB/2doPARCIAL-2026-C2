def busqueda_lineal(recetas, ingredientes, campo, valor):

    coincidencias = []

    if campo == "ingrediente":

        ids = set()

        for receta_id, nombre, cantidad, unidad in ingredientes:

            if nombre == valor:
                ids.add(receta_id)

        for receta in recetas:

            if receta.id in ids:
                coincidencias.append(receta)

    elif campo == "nombre":

        for receta in recetas:

            if receta.nombre == valor:
                coincidencias.append(receta)

    elif campo == "categoria":

        for receta in recetas:

            if receta.categoria == valor:
                coincidencias.append(receta)

    else:
        raise ValueError("Campo inválido")

    return coincidencias


def busqueda_binaria(recetas, campo, valor):

    if campo != "nombre":
        raise ValueError("El campo debe ser nombre")

    izquierda = 0
    derecha = len(recetas) - 1

    while izquierda <= derecha:

        medio = (izquierda + derecha) // 2

        if recetas[medio].nombre == valor:
            return recetas[medio]

        elif recetas[medio].nombre < valor:
            izquierda = medio + 1

        else:
            derecha = medio - 1

    return None


# TEORIA:
# No, porque la búsqueda binaria necesita que la lista esté
# ordenada por el mismo campo utilizado para realizar la búsqueda.