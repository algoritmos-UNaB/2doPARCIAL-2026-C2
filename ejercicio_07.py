def busqueda_lineal(pokemones, campo, valor):
    if campo != "nombre" and campo != "tipo" and campo != "nro":
        raise ValueError("Campo inválido")
    resultado = []
    for pokemon in pokemones:
        if campo == "nombre":
            coincide = pokemon.nombre == valor
        elif campo == "tipo":
            coincide = pokemon.tipo1 == valor or (pokemon.tipo2 != "" and pokemon.tipo2 == valor)
        else:
            coincide = pokemon.id == valor
        if coincide:
            resultado.append(pokemon)
    return resultado


def busqueda_binaria(pokemones, campo, valor):
    if campo != "nombre" and campo != "nro":
        raise ValueError("Campo inválido")
    izq = 0
    der = len(pokemones) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if campo == "nombre":
            actual = pokemones[medio].nombre
        else:
            actual = pokemones[medio].id
        if actual == valor:
            return pokemones[medio]
        elif actual < valor:
            izq = medio + 1
        else:
            der = medio - 1
    return None


# TEORIA
# No, porque la binaria descarta mitades según el nombre, y si la lista está ordenada por ataque puede descartar justo la mitad donde estaba y decir que no está.