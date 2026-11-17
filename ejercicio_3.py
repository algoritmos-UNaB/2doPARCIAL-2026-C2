from ejercicio_2 import RecetaNoEncontrada


class SubrecetaFaltanteError(Exception):
    pass


class IngredienteFaltanteError(Exception):
    pass


def ingredientes_totales(receta_id, libro, subrecetas, ingredientes):

    # Verificar que exista la receta
    libro.obtener(receta_id)

    resultado = []

    # Buscar ingredientes propios
    for id_receta, nombre, cantidad, unidad in ingredientes:

        if id_receta == receta_id:

            if not nombre or not nombre.strip():
                raise IngredienteFaltanteError(
                    "El ingrediente no tiene nombre"
                )

            resultado.append((nombre, cantidad, unidad))

    # Buscar sub-recetas recursivamente
    for id_padre, id_subreceta in subrecetas:

        if id_padre == receta_id:

            try:
                libro.obtener(id_subreceta)

            except RecetaNoEncontrada:
                raise SubrecetaFaltanteError(
                    f"No existe la sub-receta {id_subreceta}"
                )

            resultado.extend(
                ingredientes_totales(
                    id_subreceta,
                    libro,
                    subrecetas,
                    ingredientes
                )
            )

    return resultado


# TEORIA:
# La traza es:
# ingredientes_totales(9)
# ingredientes_totales(1) -> caso base
# ingredientes_totales(2) -> caso base