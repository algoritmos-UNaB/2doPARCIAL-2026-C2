from ejercicio_02 import PokemonNoEncontrado

def descendientes(origen_id, pokedex, aristas):
    pokedex.obtener(origen_id)
    resultado = []
    
    for origen, destino in aristas:
        if origen == origen_id:
            pokedex.obtener(destino)
            resultado.append(destino)
            resultado.extend(descendientes(destino, pokedex, aristas))
            
    return resultado

# TEORIA
# Traza de descendientes(4):
# 1. descendientes(4) entra, encuentra la arista (4, 5). Añade 5.
# 2. Llama a descendientes(5). Encuentra la arista (5, 6). Añade 6.
# 3. Llama a descendientes(6). No tiene aristas que salgan de él. Retorna [] (caso base).
# 4. descendientes(5) recibe [] y finaliza devolviendo [6].
# 5. descendientes(4) finaliza y retorna [5, 6].