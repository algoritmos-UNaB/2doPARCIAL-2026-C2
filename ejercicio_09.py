import csv
import os

from ejercicio_01 import Cancion
from ejercicio_02 import Biblioteca

ENCABEZADO = ["id", "titulo", "artista", "album", "genero", "anio", "duracion_seg"]

class ArchivoInvalidoError(Exception):
    pass


def guardar_canciones_csv(ruta, biblioteca):
    with open(ruta, "w", encoding="utf-8", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(ENCABEZADO)
        for c in biblioteca:
            escritor.writerow([c.id, c.titulo, c.artista, c.album, c.genero, c.anio, c.duracion_seg])


def cargar_canciones_csv(ruta) -> Biblioteca:
    if not os.path.exists(ruta):
        raise ArchivoInvalidoError(f"El archivo {ruta!r} no existe")

    biblioteca = Biblioteca()
    with open(ruta, "r", encoding="utf-8", newline="") as archivo:
        lector = csv.reader(archivo)
        encabezado = next(lector, None)
        if encabezado != ENCABEZADO:
            raise ArchivoInvalidoError(
                f"Encabezado inválido: se esperaba {','.join(ENCABEZADO)}")
        for numero, fila in enumerate(lector, start=2):
            if not fila:  # línea en blanco
                continue
            if len(fila) < len(ENCABEZADO):
                raise ArchivoInvalidoError(
                    f"La fila {numero} tiene {len(fila)} columnas y se esperaban {len(ENCABEZADO)}")
            biblioteca.agregar(Cancion(
                int(fila[0]), fila[1], fila[2], fila[3], fila[4],
                int(fila[5]), int(fila[6])))
    return biblioteca


# Teoria:
# Sí, hay que recorrer las filas anteriores: el CSV es un archivo de texto. 
# Por dentro es una sola secuencia de caracteres, y las filas estan separadas 
# por saltos de línea, así que no se puede calcular en qué byte empieza la fila 50; 
# hay que leer desde el principio contando saltos de línea.