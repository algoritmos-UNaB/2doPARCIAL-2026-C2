def _obtener_campo(pokemon, campo):
    if campo == "ataque": return pokemon.ataque
    if campo == "velocidad": return pokemon.velocidad
    if campo == "nro": return pokemon.id
    return None

def ordenar_seleccion(pokemones, campo, descendente):
    n = len(pokemones)
    for i in range(n - 1):
        idx_extremo = i
        for j in range(i + 1, n):
            val_j = _obtener_campo(pokemones[j], campo)
            val_ext = _obtener_campo(pokemones[idx_extremo], campo)
            
            if descendente:
                if val_j > val_ext:
                    idx_extremo = j
            else:
                if val_j < val_ext:
                    idx_extremo = j
                    
        pokemones[i], pokemones[idx_extremo] = pokemones[idx_extremo], pokemones[i]
    return pokemones

def ordenar_insercion(pokemones, campo, descendente):
    for i in range(1, len(pokemones)):
        actual = pokemones[i]
        val_actual = _obtener_campo(actual, campo)
        j = i - 1
        
        while j >= 0:
            val_j = _obtener_campo(pokemones[j], campo)
            debe_desplazar = (val_j < val_actual) if descendente else (val_j > val_actual)
            
            if debe_desplazar:
                pokemones[j + 1] = pokemones[j]
                j -= 1
            else:
                break
                
        pokemones[j + 1] = actual
    return pokemones

# TEORIA
# De los dos algoritmos mencionados el estable es Inserción. Estable: que mantiene el orden relativo original de aquellos elementos cuyas claves de ordenamiento son idénticas.