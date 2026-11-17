class PokemonNoEncontrado(Exception):
    pass

class Pokedex:
    def __init__(self):
        self.pokemones = []

    def agregar(self, pokemon):
        for posicion in range(len(self.pokemones)):
            if self.pokemones[posicion].id == pokemon.id:
                self.pokemones[posicion] = pokemon
                return
        self.pokemones.append(pokemon)

    def obtener(self, id):
        for pokemon in self.pokemones:
            if pokemon.id == id:
                return pokemon
        raise PokemonNoEncontrado(f"No existe el Pokemon con id {id}")

    def listar(self):
        return self.pokemones

    def cantidad(self):
        return len(self.pokemones)


# TEORIA: Le avisa a quien usa el metodo y le da la opción de handlear el error/escenario a su gusto