from ejercicio_01 import Pokemon

class PokemonNoEncontrado(Exception):
    pass

class Pokedex:

def __init__(self):
    self.pokemones = []

def agregar(self, pokemon):
    for i in range(len(self.pokemones)):
        if self.pokemones[i].id == pokemon.id:
            self.pokemones[i] == pokemon
            return

    self.pokemones.append(pokemon)

def obtener(self.id):
    for pokemon in self.pokemones:
        if pokemon.id == id:
            return pokemon
    
    raise PokemonNoEncontrado("Pokemon no encontrado")

def listar(self):
    return self.pokemones

def cantidad(self):
    return len(self.pokemones)


#Teoria
#Obtener lanza la excepcion q informa q el pokemon solicitado no existe
# asi evita confuciones con un resultado invalido