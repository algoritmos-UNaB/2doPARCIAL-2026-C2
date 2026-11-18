"""Ejercicio 3 — Relación recursiva: ingredientes_totales."""

from ejercicio_02 import RecetaNoEncontrada, libro_examen


class SubrecetaFaltanteError(Exception):
    """Una receta usa una sub-receta que no está en el libro."""


class IngredienteFaltanteError(Exception):
    """Una fila de ingredientes tiene el nombre vacío."""



SUBRECETAS_EXAMEN = [
    (9, 1),
    (9, 2),
    (10, 3),
    (10, 5),
    (12, 3),
]

INGREDIENTES_EXAMEN = [  
    (1, "perejil", 50, "g"),
    (1, "ajo", 4, "dientes"),
    (2, "tomate", 3, "u"),
    (2, "cebolla", 1, "u"),
    (3, "cebolla", 2, "u"),
    (3, "ajo", 2, "dientes"),
    (5, "harina", 500, "g"),
    (5, "agua", 150, "ml"),
    (9, "vacio", 1200, "g"),
    (9, "chorizo", 4, "u"),
    (10, "carne picada", 500, "g"),
    (12, "maiz blanco", 300, "g"),
]


def _ingredientes_propios(receta_id, ingredientes):
    """Las filas de esa receta, en el orden de la tabla, como (nombre, cantidad, unidad)."""
    propios = []
    for rid, nombre, cantidad, unidad in ingredientes:
        if rid == receta_id:
            if nombre is None or str(nombre).strip() == "":
                raise IngredienteFaltanteError(f"La receta {receta_id} tiene un ingrediente sin nombre.")
            propios.append((nombre, cantidad, unidad))
    return propios


def _subrecetas_de(receta_id, subrecetas):
    """Los ids de las sub-recetas de esa receta, en el orden de la tabla."""
    hijas = []
    for rid, subreceta_id in subrecetas:
        if rid == receta_id:
            hijas.append(subreceta_id)
    return hijas


def ingredientes_totales(receta_id, libro, subrecetas, ingredientes):
    """Ingredientes propios + los de cada sub-receta (en profundidad), como lista de tuplas.

    Orden: primero los propios; después cada sub-receta completa (con sus propias
    sub-recetas) antes de pasar a la sub-receta hermana.
    """
    libro.obtener(receta_id)  

    resultado = _ingredientes_propios(receta_id, ingredientes)
    hijas = _subrecetas_de(receta_id, subrecetas)

    if len(hijas) == 0:
        return resultado 

    for subreceta_id in hijas:
        try:
            libro.obtener(subreceta_id)
        except RecetaNoEncontrada:
            raise SubrecetaFaltanteError(
                f"La receta {receta_id} usa la sub-receta {subreceta_id}, que no está en el libro."
            ) from None
        for fila in ingredientes_totales(subreceta_id, libro, subrecetas, ingredientes):
            resultado.append(fila)
    return resultado


# TEORIA
# Traza de ingredientes_totales(9) con los datos del enunciado:
#
#   1) ingredientes_totales(9)    propios: vacio, chorizo; sub-recetas: 1, 2
#   2)   ingredientes_totales(1)  CASO BASE (sin sub-recetas): perejil, ajo   -> vuelve a 9
#   3)   ingredientes_totales(2)  CASO BASE (sin sub-recetas): tomate, cebolla -> vuelve a 9
#   9 devuelve: vacio, chorizo, perejil, ajo, tomate, cebolla
#
# Orden en que entran los llamados: 9, 1, 2. La llamada a 1 termina antes de
# que empiece la de 2 (la sub-receta hermana).


if __name__ == "__main__":
    libro = libro_examen()
    for numero, fila in enumerate(ingredientes_totales(9, libro, SUBRECETAS_EXAMEN, INGREDIENTES_EXAMEN), start=1):
        print(f"{numero}. {fila}")
    print("Empanadas de carne (10):", ingredientes_totales(10, libro, SUBRECETAS_EXAMEN, INGREDIENTES_EXAMEN))
    try:
        ingredientes_totales(9, libro, SUBRECETAS_EXAMEN + [(9, 77)], INGREDIENTES_EXAMEN)
    except SubrecetaFaltanteError as error:
        print("SubrecetaFaltanteError:", error)
