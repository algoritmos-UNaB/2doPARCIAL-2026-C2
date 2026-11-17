from ejercicio_01 import Pokemon

class PokemonNoEncontrado(Exception):
    pass

class Pokedex:
    def _init_(self):
        self.pokemones = []

    def agregar(self, pokemon):
        for i, p in enumerate(self.pokemones):
            if p.id == pokemon.id:
                self.pokemones[i] = pokemon
                return
        self.pokemones.append(pokemon)

    def obtener(self, id):
        for p in self.pokemones:
            if p.id == id:
                return p
        raise PokemonNoEncontrado(f"No existe un Pokémon con id {id}.")

    def listar(self):
        return list(self.pokemones)

    def cantidad(self):
        return len(self.pokemones)

# TEORIA: Quien llama al método gana seguridad operativa, porque se ve forzado a manejar la excepción si la receta no existe, en lugar de arrastrar un error silencioso por operar con un NoneType.