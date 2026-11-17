def descendientes(origen_id, pokedex, aristas):
    pokedex.obtener(origen_id)

    for origen, destino in aristas:
        pokedex.obtener(destino)

    def recorrer(actual):
        resultado = []

        for origen, destino in aristas:
            if origen == actual:
                resultado.append(destino)
                resultado.extend(recorrer(destino))

        return resultado

    return recorrer(origen_id)


# El recorrido entra primero con 4, despues con 5 y por ultimo con 6 que es el caso base por que no tiene destinos y devuelve una lista vacia.