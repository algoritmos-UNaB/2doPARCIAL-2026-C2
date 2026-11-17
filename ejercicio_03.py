def descendientes(origen_id, pokedex, aristas):
    pokedex.obtener(origen_id)
    resultado = []
    for origen, destino in aristas:
        if origen == origen_id:
            pokedex.obtener(destino)
            resultado.append(destino)
            resultado.extend(descendientes(destino, pokedex, aristas))
    return resultado
# La excepcion se lanza en otro lado, no se ve acá explicitamente

# TEORIA -> 
# descendientes(4) -> 4, 5 -> Entra primero al for.
# descendientes(5) -> 5, 6 -> Entra segundo al for.
# descendientes(6) -> 6    -> Aca finaliza, caso base devuelve vacío -> Entro tercero al for.