# TEORÍA: Quien llama al método evita tener que verificar si el resultado es None en cada llamada y previene errores inesperados posteriores, obligando a manejar la ausencia del Pokémon de forma explícita y controlada.

from ejercicio_01 import Pokemon


class PokemonNoEncontrado(Exception):
    pass


class Pokedex:
    def _init_(self):
        self._catalogo = []

    def agregar(self, pokemon: Pokemon) -> None:
        for i, actual in enumerate(self._catalogo):
            if actual.id == pokemon.id:
                self._catalogo[i] = pokemon
                return
        self._catalogo.append(pokemon)

    def obtener(self, id: int) -> Pokemon:
        for pokemon in self._catalogo:
            if pokemon.id == id:
                return pokemon
        raise PokemonNoEncontrado(f"No se encontró el Pokémon con id {id}.")

    def listar(self) -> list:
        return list(self._catalogo)

    def cantidad(self) -> int:
        return len(self._catalogo)