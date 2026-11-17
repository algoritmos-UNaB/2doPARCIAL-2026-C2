def obtener_valor(pokemon, campo):
    if campo == "ataque":
        return pokemon.ataque
    if campo == "velocidad":
        return pokemon.velocidad
    return pokemon.id

def ordenar_seleccion(pokemones, campo, descendente):
    for i in range(len(pokemones) - 1):
        elegido = i
        for j in range(i + 1, len(pokemones)):
            valor_j = obtener_valor(pokemones[j], campo)
            valor_elegido = obtener_valor(pokemones[elegido], campo)
            if descendente:
                if valor_j > valor_elegido:
                    elegido = j
            else:
                if valor_j < valor_elegido:
                    elegido = j
        if elegido != i:
            auxiliar = pokemones[i]
            pokemones[i] = pokemones[elegido]
            pokemones[elegido] = auxiliar
    return pokemones

def ordenar_insercion(pokemones, campo, descendente):
    for i in range(1, len(pokemones)):
        actual = pokemones[i]
        valor_actual = obtener_valor(actual, campo)
        j = i - 1
        while j >= 0:
            valor_j = obtener_valor(pokemones[j], campo)
            if descendente:
                debe_mover = valor_j < valor_actual
            else:
                debe_mover = valor_j > valor_actual
            if not debe_mover:
                break
            pokemones[j + 1] = pokemones[j]
            j -= 1
        pokemones[j + 1] = actual
    return pokemones

# TEORIA -> El algoritmo de insercion es estable, estable es aquel que ante elementos de igual valor en X campo, mantiene le orden