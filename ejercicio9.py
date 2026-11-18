import csv
import os

from ejercicio2 import Cancion, Biblioteca


class ArchivoInvalidoError(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)


ENCABEZADO = ["id", "titulo", "artista", "album", "genero", "anio", "duracion_seg"]


def guardar_canciones_csv(ruta, biblioteca):
    with open(ruta, "w", encoding="utf-8", newline="") as archivo:
        escritor = csv.writer(archivo, delimiter=",")
        escritor.writerow(ENCABEZADO)
        for cancion in biblioteca:
            escritor.writerow([
                cancion.id,
                cancion.titulo,
                cancion.artista,
                cancion.album,
                cancion.genero,
                cancion.anio,
                cancion.duracion_seg,
            ])


def cargar_canciones_csv(ruta):
    if not os.path.exists(ruta):
        raise ArchivoInvalidoError(f"El archivo '{ruta}' no existe.")

    with open(ruta, "r", encoding="utf-8", newline="") as archivo:
        lector = csv.reader(archivo, delimiter=",")
        encabezado = next(lector, None)
        if encabezado != ENCABEZADO:
            raise ArchivoInvalidoError(
                f"Encabezado inválido. Se esperaba {ENCABEZADO}."
            )

        biblioteca = Biblioteca()
        for numero_fila, fila in enumerate(lector, start=2):
            if len(fila) < len(ENCABEZADO):
                raise ArchivoInvalidoError(
                    f"La fila {numero_fila} tiene menos columnas de las esperadas."
                )
            cancion = Cancion(
                id=int(fila[0]),
                titulo=fila[1],
                artista=fila[2],
                album=fila[3],
                genero=fila[4],
                anio=int(fila[5]),
                duracion_seg=int(fila[6]),
            )
            biblioteca.agregar(cancion)
        return biblioteca

# **Teoría.**
# no hace falta recorrer las filas anteriores, porque el CSV guarda cada canción como una línea de texto independiente 
# (registros de longitud variable separados por saltos de línea), así que se puede saltar directamente a la fila 50 sin interpretar las anteriores.

