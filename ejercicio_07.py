def busqueda_lineal(pokemones, campo, valor):
    resultados = []
    for p in pokemones:
        if campo == "nombre" and p.nombre == valor:
            resultados.append(p)
        elif campo == "tipo" and (p.tipo1 == valor or p.tipo2 == valor):
            resultados.append(p)
        elif campo == "nro" and p.id == valor:
            resultados.append(p)
    return resultados

def busqueda_binaria(pokemones, campo, valor):
    izq = 0
    der = len(pokemones) - 1
    
    while izq <= der:
        medio = (izq + der) // 2
        p_medio = pokemones[medio]
        
        if campo == "nombre":
            val_medio = p_medio.nombre
        elif campo == "nro":
            val_medio = p_medio.id
        else:
            return None
            
        if val_medio == valor:
            return p_medio
        elif val_medio < valor:
            izq = medio + 1
        else:
            der = medio - 1
            
    return None

# TEORIA
# No, el resultado no es confiable, porque la condición matemática para que la búsqueda binaria funcione descartando mitades es que el arreglo esté ordenado,en este caso, en base a el nombre .