# TEORÍA: Traza de descendientes(4) con aristas [(4, 5), (5, 6)]: 1) entra descendientes(4), 2) entra descendientes(5), 3) entra descendientes(6) que alcanza el caso base al no tener destinos y retorna [].

from ejercicio_02 import Pokedex, PokemonNoEncontrado


def descendientes(origen_id: int, pokedex: Pokedex, aristas: list) -> list:
    # Valida que el origen exista en la Pokédex (si no, lanza PokemonNoEncontrado)
    pokedex.obtener(origen_id)

    resultado = []
    for origen, destino in aristas:
        if origen == origen_id:
            # Valida que el destino también exista en la Pokédex
            pokedex.obtener(destino)
            resultado.append(destino)
            resultado.extend(descendientes(destino, pokedex, aristas))

    return resultado