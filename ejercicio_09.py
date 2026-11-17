# TEORÍA: Sí, hace falta leer los registros anteriores porque los archivos de texto (como CSV) tienen
# registros de longitud variable y el acceso es secuencial, por lo que no se puede calcular de antemano
# la posición exacta en bytes donde empieza el registro número 10 sin recorrer los saltos de línea previos.

import csv
from ejercicio_01 import Pokemon
from ejercicio_02 import Pokedex


class ArchivoInvalidoError(Exception):
    pass


ENCABEZADO_ESPERADO = [
    "id",
    "nombre",
    "tipo1",
    "tipo2",
    "hp",
    "ataque",
    "defensa",
    "velocidad",
    "generacion",
]


def guardar_csv(ruta, pokedex):
    with open(ruta, mode="w", encoding="utf-8", newline="") as archivo:
        escritor = csv.writer(archivo, delimiter=",")
        escritor.writerow(ENCABEZADO_ESPERADO)
        for pokemon in pokedex:
            escritor.writerow([
                pokemon.id,
                pokemon.nombre,
                pokemon.tipo1,
                pokemon.tipo2 if pokemon.tipo2 is not None else "",
                pokemon.hp,
                pokemon.ataque,
                pokemon.defensa,
                pokemon.velocidad,
                pokemon.generacion,
            ])


def cargar_csv(ruta):
    pokedex = Pokedex()
    with open(ruta, mode="r", encoding="utf-8", newline="") as archivo:
        lector = csv.reader(archivo, delimiter=",")
        encabezado = next(lector, None)
        if encabezado != ENCABEZADO_ESPERADO:
            raise ArchivoInvalidoError("El archivo CSV no tiene el encabezado esperado.")

        for fila in lector:
            if len(fila) != 9:
                raise ArchivoInvalidoError("Una fila no tiene exactamente 9 columnas.")
            try:
                id_poke = int(fila[0])
                nombre = fila[1]
                tipo1 = fila[2]
                tipo2 = fila[3] if fila[3] != "" else None
                hp = int(fila[4])
                ataque = int(fila[5])
                defensa = int(fila[6])
                velocidad = int(fila[7])
                generacion = int(fila[8])
            except ValueError as err:
                raise ArchivoInvalidoError("Un campo numérico no se pudo convertir a entero.") from err

            pokemon = Pokemon(
                id_poke,
                nombre,
                tipo1,
                tipo2,
                hp,
                ataque,
                defensa,
                velocidad,
                generacion,
            )
            pokedex.agregar(pokemon)

    return pokedex