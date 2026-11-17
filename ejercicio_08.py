VALOR_DIFICULTAD = {"baja": 1, "media": 2, "alta": 3}

def _es_mejor(r1, r2, campo, descendente):
    if campo == "tiempo":
        v1, v2 = r1.tiempo_min, r2.tiempo_min
    else:  # dificultad
        v1, v2 = VALOR_DIFICULTAD[r1.dificultad], VALOR_DIFICULTAD[r2.dificultad]
    
    if descendente:
        return v1 > v2
    return v1 < v2

def ordenar_seleccion(recetas, campo, descendente):
    n = len(recetas)
    for i in range(n - 1):
        idx_extremo = i
        for j in range(i + 1, n):
            if _es_mejor(recetas[j], recetas[idx_extremo], campo, descendente):
                idx_extremo = j
        recetas[i], recetas[idx_extremo] = recetas[idx_extremo], recetas[i]
    return recetas

def ordenar_insercion(recetas, campo, descendente):
    for i in range(1, len(recetas)):
        actual = recetas[i]
        j = i - 1
        while j >= 0 and _es_mejor(actual, recetas[j], campo, descendente):
            recetas[j + 1] = recetas[j]
            j -= 1
        recetas[j + 1] = actual
    return recetas

# TEORIA: Ordenar por Inserción es estable. Un algoritmo estable es aquel que preserva el orden relativo inicial de los elementos que son iguales según la clave de ordenamiento.