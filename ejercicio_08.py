def _clave(pokemon, campo):
    if campo == "ataque":
        return pokemon.ataque
    if campo == "velocidad":
        return pokemon.velocidad
    if campo == "nro":
        return pokemon.id
    raise ValueError("Campo inválido")


def _va_antes(a, b, descendente):
    if descendente:
        return a > b
    return a < b


def ordenar_seleccion(pokemones, campo, descendente=False):
    n = len(pokemones)
    for i in range(n - 1):
        elegido = i
        for j in range(i + 1, n):
            if _va_antes(_clave(pokemones[j], campo), _clave(pokemones[elegido], campo), descendente):
                elegido = j
        if elegido != i:
            pokemones[i], pokemones[elegido] = pokemones[elegido], pokemones[i]
    return pokemones


def ordenar_insercion(pokemones, campo, descendente=False):
    for i in range(1, len(pokemones)):
        actual = pokemones[i]
        j = i - 1
        while j >= 0 and _va_antes(_clave(actual, campo), _clave(pokemones[j], campo), descendente):
            pokemones[j + 1] = pokemones[j]
            j -= 1
        pokemones[j + 1] = actual
    return pokemones


# TEORIA
# El estable es inserción, estable quiere decir que si dos elementos tienen el mismo valor quedan en el mismo orden que tenían antes de ordenar.