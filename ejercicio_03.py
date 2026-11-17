def descendientes(origen_id, pokedex, aristas):
    pokedex.obtener(origen_id)

    destinos = []
    for origen, destino in aristas:
        if origen == origen_id:
            destinos.append(destino)

    # caso base
    if destinos == []:
        return []

    # caso recursivo
    resultado = []
    for destino in destinos:
        resultado.append(destino)
        resultado.extend(descendientes(destino, pokedex, aristas))
    return resultado


# TEORIA
# descendientes(4): tiene destino 5, lo agrega y llama a descendientes(5)
# descendientes(5): tiene destino 6, lo agrega y llama a descendientes(6)
# descendientes(6): no tiene destinos, es el caso base y devuelve []
# Al volver, descendientes(5) da [6] y descendientes(4) da [5, 6].