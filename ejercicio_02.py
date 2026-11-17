class PokemonNoEncontrado(exception):
    pass

class Pokedex:
    def __init__(self):
        self.pokemones = []

    def agregar(self, pokemon):
        for indice in range(len(self.pokemones)):
            if self.pokemones[indice].id == pokemon.id:
                self.pokemones[inidice] = pokemon
                return

        self.pokemones.append(pokemon)

    def obtener(self, id):
        for pokemon in self.pokemones:
            if pokemon.id == id:
                return pokemon

        raise PokemonNoEncontrado("No existe el Pokémon con ID {id}")

    def listar(self):
        return self.pokemones.copy()

    def cantidad(self):
        return len(self.pokemones)