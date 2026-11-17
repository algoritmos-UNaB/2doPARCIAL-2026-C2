
def busqueda_lineal(recetas, ingredientes, campo, valor):
    resultados = []

    for receta in recetas:
        if campo == "nombre":
            if receta.nombre == valor:
                resultados.append(receta)

        elif campo == "categoria":
            if receta.categoria == valor:
                resultados.append(receta)

        elif campo == "ingrediente":
            for ingrediente in ingredientes:
                id_receta, nombre, cantidad, unidad = ingrediente

                if id_receta == receta.id and nombre == valor:
                    resultados.append(receta)
                    break

    return resultados


def busqueda_binaria(recetas, campo, valor):
    if campo != "nombre":
        return None

    inicio = 0
    fin = len(recetas) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2

        if recetas[medio].nombre == valor:
            return recetas[medio]

        elif recetas[medio].nombre < valor:
            inicio = medio + 1

        else:
            fin = medio - 1

    return None


# TEORIA
# No, porque la busqueda binaria necesita que la lista este ordenada por el mismo campo que se utiliza para buscar.
