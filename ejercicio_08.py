
def obtener_valor(receta, campo):
    if campo == "tiempo":
        return receta.tiempo_min

    elif campo == "dificultad":
        orden = {
            "baja": 1,
            "media": 2,
            "alta": 3
        }
        return orden[receta.dificultad]


def ordenar_seleccion(recetas, campo, descendente=False):
    n = len(recetas)

    for i in range(n):
        mejor = i

        for j in range(i + 1, n):
            valor_j = obtener_valor(recetas[j], campo)
            valor_mejor = obtener_valor(recetas[mejor], campo)

            if descendente:
                if valor_j > valor_mejor:
                    mejor = j
            else:
                if valor_j < valor_mejor:
                    mejor = j

        recetas[i], recetas[mejor] = recetas[mejor], recetas[i]

    return recetas


def ordenar_insercion(recetas, campo, descendente=False):
    for i in range(1, len(recetas)):
        actual = recetas[i]
        valor_actual = obtener_valor(actual, campo)
        j = i - 1

        while j >= 0:
            valor_anterior = obtener_valor(recetas[j], campo)

            if descendente:
                if valor_anterior < valor_actual:
                    recetas[j + 1] = recetas[j]
                    j -= 1
                else:
                    break
            else:
                if valor_anterior > valor_actual:
                    recetas[j + 1] = recetas[j]
                    j -= 1
                else:
                    break

        recetas[j + 1] = actual

    return recetas


# TEORIA
# Insercion es estable porque mantiene el orden original de los elementos que tienen el mismo valor.
