from ejercicio_01 import Pokemon


def busqueda_lineal(pokemones, campo, valor):
    resultados = []

    for pokemon in pokemones:
        if campo == "nombre":
            dato = pokemon.nombre
        elif campo == "tipo":
            dato = pokemon.tipo1
        elif campo == "nro":
            dato = pokemon.id
        else:
            raise ValueError("Campo de búsqueda inválido")

        if dato == valor:
            resultados.append(pokemon)

    return resultados


def busqueda_binaria(pokemones, campo, valor):
    inicio = 0
    fin = len(pokemones) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        pokemon = pokemones[medio]

        if campo == "nombre":
            dato = pokemon.nombre
        elif campo == "nro":
            dato = pokemon.id
        else:
            raise ValueError("Campo de búsqueda inválido")

        if dato == valor:
            return pokemon
        elif dato < valor:
            inicio = medio + 1
        else:
            fin = medio - 1

    return None


#Teoria
#No, porque la busqueda binaria necesita que la lista este ordenada por el
# mismo criterio que se utiliza para buscar.