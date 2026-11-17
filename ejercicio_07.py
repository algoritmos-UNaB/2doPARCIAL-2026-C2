def busqueda_lineal(recetas, ingredientes, campo, valor):
    resultados = []
    for receta in recetas:
        if campo == "nombre" and receta.nombre == valor:
            resultados.append(receta)
        elif campo == "categoria" and receta.categoria == valor:
            resultados.append(receta)
        elif campo == "ingrediente":
            for req_id, nombre, cant, unid in ingredientes:
                if req_id == receta.id and nombre == valor:
                    resultados.append(receta)
                    break
    return resultados


def busqueda_binaria(recetas, campo, valor):
    if campo != "nombre":
        return None
    
    izq, der = 0, len(recetas) - 1
    
    while izq <= der:
        medio = (izq + der) // 2
        actual = recetas[medio]
        
        if actual.nombre == valor:
            return actual
        elif actual.nombre < valor:
            izq = medio + 1
        else:
            der = medio - 1
            
    return None

# TEORIA: No, porque el algoritmo requiere cortar el espacio de búsqueda a la mitad evaluando mayor/menor respecto al campo buscado (nombre), por lo que un ordenamiento por tiempo invalida el supuesto lógico.