from ejercicio_01 import Pokemon

class PokemonNoEncontrado(Exception):
    pass


class Pokedex:

    def __init__(self):
        self.datos_pokedex = []


    def agregar(self, pokemon):
        for i in range(len(self.datos_pokedex)):
            if pokemon.id == self.datos_pokedex[i].id:
                self.datos_pokedex[i] = pokemon
                return
        self.datos_pokedex.append(pokemon)

    def obtener(self, id):
        for pokemon in self.datos_pokedex:
            if id == pokemon.id:
                return pokemon

        raise PokemonNoEncontrado("No se encontro el pokemon")

    def listar(self):
        return self.datos_pokedex    

    def cantidad(self):
        return len(self.datos_pokedex)


# TEORIA
# Al ultizar una exceptcion ganamos que diga cual fue el "error" de manera muy precisa