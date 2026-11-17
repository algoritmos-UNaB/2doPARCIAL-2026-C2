import csv
from ejercicio_01 import Pokemon


class ArchivoInvalidoError(Exception):
    pass


ENCABEZADO = [
    "id",
    "nombre",
    "tipo1",
    "tipo2",
    "hp",
    "ataque",
    "defensa",
    "velocidad",
    "generacion"
]


def guardar_csv(pokemones, ruta):
    with open(ruta, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)

        escritor.writerow(ENCABEZADO)

        for pokemon in pokemones:
            escritor.writerow([
                pokemon.id,
                pokemon.nombre,
                pokemon.tipo1,
                pokemon.tipo2 if pokemon.tipo2 is not None else "",
                pokemon.hp,
                pokemon.ataque,
                pokemon.defensa,
                pokemon.velocidad,
                pokemon.generacion
            ])


def cargar_csv(ruta):
    pokemones = []

    try:
        with open(ruta, "r", newline="", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)

            encabezado = next(lector, None)

            if encabezado != ENCABEZADO:
                raise ArchivoInvalidoError("Encabezado incorrecto")

            for numero_fila, fila in enumerate(lector, start=2):
                if len(fila) != 9:
                    raise ArchivoInvalidoError(
                        f"La fila {numero_fila} no tiene 9 columnas"
                    )

                try:
                    identificador = int(fila[0])
                    hp = int(fila[4])
                    ataque = int(fila[5])
                    defensa = int(fila[6])
                    velocidad = int(fila[7])
                    generacion = int(fila[8])
                except ValueError:
                    raise ArchivoInvalidoError(
                        f"Hay un valor numérico inválido en la fila {numero_fila}"
                    )

                pokemon = Pokemon(
                    identificador,
                    fila[1],
                    fila[2],
                    fila[3] if fila[3] != "" else None,
                    hp,
                    ataque,
                    defensa,
                    velocidad,
                    generacion
                )

                pokemones.append(pokemon)

    except OSError as error:
        raise ArchivoInvalidoError(
            f"No se pudo abrir o leer el archivo: {error}"
        )

    return pokemones


#Teoria
#No, porque en un archivo CSV el acceso es secuencial, por lo que hay que
# leer las filas anteriores para llegar al registro numero 10