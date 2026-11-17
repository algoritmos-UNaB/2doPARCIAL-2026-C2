def obtener_clave(receta, campo):

    if campo == "tiempo":
        return receta.tiempo_min

    elif campo == "dificultad":

        orden = {
            "baja": 0,
            "media": 1,
            "alta": 2
        }

        return orden[receta.dificultad]

    else:
        raise ValueError("Campo inválido")


def ordenar_seleccion(recetas, campo, descendente=False):

    n = len(recetas)

    for i in range(n - 1):

        extremo = i

        for j in range(i + 1, n):

            clave_j = obtener_clave(recetas[j], campo)
            clave_extremo = obtener_clave(recetas[extremo], campo)

            if descendente:

                if clave_j > clave_extremo:
                    extremo = j

            else:

                if clave_j < clave_extremo:
                    extremo = j

        recetas[i], recetas[extremo] = recetas[extremo], recetas[i]

    return recetas


def ordenar_insercion(recetas, campo, descendente=False):

    for i in range(1, len(recetas)):

        actual = recetas[i]
        clave_actual = obtener_clave(actual, campo)

        j = i - 1

        while j >= 0:

            clave_anterior = obtener_clave(recetas[j], campo)

            if descendente:
                mover = clave_anterior < clave_actual
            else:
                mover = clave_anterior > clave_actual

            if not mover:
                break

            recetas[j + 1] = recetas[j]
            j -= 1

        recetas[j + 1] = actual

    return recetas


# TEORIA:
# El ordenamiento por inserción es estable.
# Esto significa que conserva el orden relativo de los elementos
# que tienen la misma clave de ordenamiento.