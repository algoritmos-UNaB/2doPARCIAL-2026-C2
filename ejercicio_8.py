# TEORÍA: El algoritmo estable es el de inserción; un algoritmo de ordenamiento es estable cuando
# conserva el orden relativo original entre aquellos elementos que tienen claves de comparación iguales.


def _obtener_valor(pokemon, campo):
    if campo == "ataque":
        return pokemon.ataque
    elif campo == "velocidad":
        return pokemon.velocidad
    return pokemon.id


def ordenar_seleccion(pokemones, campo, descendente=False):
    n = len(pokemones)
    for i in range(n):
        indice_objetivo = i
        for j in range(i + 1, n):
            val_j = _obtener_valor(pokemones[j], campo)
            val_obj = _obtener_valor(pokemones[indice_objetivo], campo)
            if (descendente and val_j > val_obj) or (not descendente and val_j < val_obj):
                indice_objetivo = j
        pokemones[i], pokemones[indice_objetivo] = pokemones[indice_objetivo], pokemones[i]
    return pokemones


def ordenar_insercion(pokemones, campo, descendente=False):
    for i in range(1, len(pokemones)):
        actual = pokemones[i]
        val_actual = _obtener_valor(actual, campo)
        j = i - 1
        while j >= 0:
            val_j = _obtener_valor(pokemones[j], campo)
            if (descendente and val_j < val_actual) or (not descendente and val_j > val_actual):
                pokemones[j + 1] = pokemones[j]
                j -= 1
            else:
                break
        pokemones[j + 1] = actual
    return pokemones