import csv

from ejercicio_01 import Pokemon
from ejercicio_02 import Pokedex

ENCABEZADO = ["id", "nombre", "tipo1", "tipo2", "hp", "ataque", "defensa", "velocidad", "generacion"]


class ArchivoInvalidoError(Exception):
    pass


def guardar_csv(ruta, pokedex):
    with open(ruta, "w", encoding="utf-8", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(ENCABEZADO)
        for p in pokedex.listar():
            escritor.writerow([p.id, p.nombre, p.tipo1, p.tipo2, p.hp, p.ataque, p.defensa, p.velocidad, p.generacion])


def cargar_csv(ruta):
    pokedex = Pokedex()
    try:
        with open(ruta, "r", encoding="utf-8", newline="") as archivo:
            lector = csv.reader(archivo)
            if next(lector, None) != ENCABEZADO:
                raise ArchivoInvalidoError("Falta el encabezado")
            for fila in lector:
                if fila == []:
                    continue
                if len(fila) != 9:
                    raise ArchivoInvalidoError("La fila no tiene 9 columnas")
                try:
                    pokemon = Pokemon(int(fila[0]), fila[1], fila[2], fila[3], int(fila[4]),
                                      int(fila[5]), int(fila[6]), int(fila[7]), int(fila[8]))
                except ValueError:
                    raise ArchivoInvalidoError("Número inválido")
                pokedex.agregar(pokemon)
    except (UnicodeDecodeError, csv.Error):
        raise ArchivoInvalidoError("No es un CSV válido")
    return pokedex


# TEORIA
# Sí, hay que leer los 9 anteriores porque cada línea tiene distinto largo y no se sabe dónde empieza la 10. El acceso es secuencial.