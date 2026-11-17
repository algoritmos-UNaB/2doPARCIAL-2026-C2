from ejercicio_01 import Pokemon
from ejercicio_02 import Pokedex

class ArchivoInvalidoError(Exception):
    pass

ENCABEZADO = ["id", "nombre", "tipo1", "tipo2", "hp", "ataque", "defensa", "velocidad", "generacion"]

def guardar_csv(ruta, pokedex):
    with open(ruta, "w", encoding="utf-8") as archivo:
        archivo.write(",".join(ENCABEZADO) + "\n")
        for pokemon in pokedex.listar():
            campos = [
                str(pokemon.id),
                pokemon.nombre,
                pokemon.tipo1,
                pokemon.tipo2,
                str(pokemon.hp),
                str(pokemon.ataque),
                str(pokemon.defensa),
                str(pokemon.velocidad),
                str(pokemon.generacion),
            ]
            archivo.write(",".join(campos) + "\n")

def cargar_csv(ruta):
    pokedex = Pokedex()
    with open(ruta, "r", encoding="utf-8") as archivo:
        lineas = archivo.read().splitlines()

    if len(lineas) == 0 or lineas[0].split(",") != ENCABEZADO:
        raise ArchivoInvalidoError("El archivo no tiene encabezado valido")

    for linea in lineas[1:]:
        if linea == "":
            continue
        columnas = linea.split(",")
        if len(columnas) != 9:
            raise ArchivoInvalidoError("Fila con cantidad de columnas incorrecta")
        try:
            pokemon = Pokemon(
                int(columnas[0]),
                columnas[1],
                columnas[2],
                columnas[3],
                int(columnas[4]),
                int(columnas[5]),
                int(columnas[6]),
                int(columnas[7]),
                int(columnas[8]),
            )
        except ValueError:
            raise ArchivoInvalidoError("Hay un numero que no se puede convertir")
        pokedex.agregar(pokemon)
    return pokedex

# TEORIA -> Si, hay que leer los anteriores ya que el largo varía, por ende el acceso es secuencial