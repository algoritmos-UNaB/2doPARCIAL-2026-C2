class SubrecetaFaltanteError(Exception):
    pass

class IngredienteFaltanteError(Exception):
    pass

def ingredientes_totales(receta_id, libro, subrecetas, ingredientes):
    # Validamos que la receta principal exista
    libro.obtener(receta_id)

    resultado = []
    
    # 1. Ingredientes propios de la receta
    for req_id, nombre, cantidad, unidad in ingredientes:
        if req_id == receta_id:
            if not nombre:
                raise IngredienteFaltanteError("Falta el nombre de un ingrediente.")
            resultado.append((nombre, cantidad, unidad))

    # 2. Ingredientes de cada subreceta
    for req_id, sub_id in subrecetas:
        if req_id == receta_id:
            try:
                libro.obtener(sub_id)
            except RecetaNoEncontrada:
                raise SubrecetaFaltanteError(f"Falta la subreceta {sub_id} en el libro.")
            
            sub_ingredientes = ingredientes_totales(sub_id, libro, subrecetas, ingredientes)
            resultado.extend(sub_ingredientes)

    return resultado

# TEORIA: Traza de ingredientes_totales(9): 
# - Entra llamada para receta_id=9 (procesa ingredientes, luego itera subrecetas).
# - Entra llamada para receta_id=1 (procesa ingredientes, caso base).
# - Entra llamada para receta_id=2 (procesa ingredientes, caso base).