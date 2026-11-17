
from ejercicio_02 import RecetaNoEncontrada


class SubrecetaFaltanteError(Exception):
    pass


class IngredienteFaltanteError(Exception):
    pass


def ingredientes_totales(receta_id, libro, subrecetas, ingredientes):
    libro.obtener(receta_id)

    resultado = []

    # Agregar los ingredientes propios de la receta
    for fila in ingredientes:
        id_receta, nombre, cantidad, unidad = fila

        if id_receta == receta_id:
            if nombre.strip() == "":
                raise IngredienteFaltanteError("Ingrediente sin nombre")

            resultado.append((nombre, cantidad, unidad))

    # Buscar las sub-recetas y procesarlas
    for id_padre, id_subreceta in subrecetas:
        if id_padre == receta_id:
            try:
                libro.obtener(id_subreceta)
            except RecetaNoEncontrada:
                raise SubrecetaFaltanteError("Sub-receta no encontrada")

            resultado.extend(
                ingredientes_totales(
                    id_subreceta,
                    libro,
                    subrecetas,
                    ingredientes
                )
            )

    return resultado


# TEORIA
# La funcion empieza con la receta 9. Luego entra a la receta 1 y termina porque no tiene sub-recetas. Despues entra a la receta 2, que tambien es un caso base.
