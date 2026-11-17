# TEORÍA: No, el resultado no es confiable porque la búsqueda binaria descarta mitades asumiendo un orden estricto por nombre, por lo que al estar ordenada por ataque puede descartar la mitad donde realmente se encuentra el Pokémon buscado.


def busqueda_lineal(pokemones, campo, valor):
    coincidencias = []
    for pokemon in pokemones:
        if campo == "nombre" and pokemon.nombre == valor:
            coincidencias.append(pokemon)
        elif campo == "tipo" and (pokemon.tipo1 == valor or pokemon.tipo2 == valor):
            coincidencias.append(pokemon)
        elif campo == "nro" and pokemon.id == valor:
            coincidencias.append(pokemon)
    return coincidencias


def busqueda_binaria(pokemones, campo, valor):
    izquierda = 0
    derecha = len(pokemones) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        pokemon_actual = pokemones[medio]
        valor_actual = pokemon_actual.nombre if campo == "nombre" else pokemon_actual.id

        if valor_actual == valor:
            return pokemon_actual
        elif valor_actual < valor:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return None