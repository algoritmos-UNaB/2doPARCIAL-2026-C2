from ejercicio_02 import PokemonNoEncontrado

def descendientes(origen_id, pokedex, aristas):

    pokedex.obtener(origen_id)

    resultado = []

    for origen, destino in aristas:

        if origen == origen_id:

            pokedex.obtener(destino)

            resultado.append(destino)

            siguientes = descendientes(destino, pokedex, aristas)

            for id in siguientes:
                resultado.append(id)

    return resultado

# TEORIA
# Traza de descendientes(4):
# 1. descendientes(4): encuentra el destino 5.
# 2. descendientes(5): encuentra el destino 6.
# 3. descendientes(6): no tiene destinos, devuelve [].
# 4. descendientes(5) devuelve [6].
# 5. descendientes(4) devuelve [5, 6].