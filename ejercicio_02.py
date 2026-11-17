class PokemonNoEncontrado(Exception):
    pass


class Pokedex:

    def __init__(self):
        self._pokemones = []

    def agregar(self, pokemon):
        for i in range(len(self._pokemones)):
            if self._pokemones[i].id == pokemon.id:
                self._pokemones[i] = pokemon
                return
        self._pokemones.append(pokemon)

    def obtener(self, id):
        for pokemon in self._pokemones:
            if pokemon.id == id:
                return pokemon
        raise PokemonNoEncontrado(f"No existe el id {id}")

    def listar(self):
        return list(self._pokemones)

    def cantidad(self):
        return len(self._pokemones)


# TEORIA
# Que no tiene que andar revisando si le volvió None: si el id no existe salta el error en el momento y lo puede manejar con un try/except.