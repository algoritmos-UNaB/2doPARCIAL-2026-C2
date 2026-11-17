def busqueda_lineal(pokemones, campo, valor):
    coincidencias = []
    for pokemon in pokemones:
        if campo == "nombre":
            if pokemon.nombre == valor:
                coincidencias.append(pokemon)
        elif campo == "tipo":
            if pokemon.tipo1 == valor or pokemon.tipo2 == valor:
                coincidencias.append(pokemon)
        elif campo == "nro":
            if pokemon.id == valor:
                coincidencias.append(pokemon)
    return coincidencias

def busqueda_binaria(pokemones, campo, valor):
    izquierda = 0
    derecha = len(pokemones) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if campo == "nombre":
            actual = pokemones[medio].nombre
        else:
            actual = pokemones[medio].id
        if actual == valor:
            return pokemones[medio]
        if actual < valor:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return None

# TEORIA -> No sería confiable ordenarla por otro campo, porque en una busqueda binaria descartamos la mitad
# de la lista, si descartamos por un criterio equivocado podriamos perder los datos que nos importan por estar en esa mitad