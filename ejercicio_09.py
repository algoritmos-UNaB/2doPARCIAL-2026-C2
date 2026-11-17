"""Ejercicio 9. Persistencia del catalogo  en CSV con codif  UTF-8."""

import csv

if __package__:
    from .ejercicio_01 import Cancion
    from .ejercicio_02 import Biblioteca
else:
    from ejercicio_01 import Cancion
    from ejercicio_02 import Biblioteca


class ArchivoInvalidoError(Exception):
    """El archivo no se puede procesar con el formato solicitado."""


ENCABEZADO = ["id", "titulo", "artista", "album", "genero", "anio", "duracion_seg"]


def guardar_canciones_csv(ruta, biblioteca):
    try:
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
    except (OSError, UnicodeError, csv.Error) as error:
        raise ArchivoInvalidoError(f"No se pudo guardar el CSV '{ruta}'.") from error
    return biblioteca.cantidad()


def cargar_canciones_csv(ruta) -> Biblioteca:
    biblioteca = Biblioteca()
    try:
        with open(ruta, "r", encoding="utf-8", newline="") as archivo:
            lector = csv.reader(archivo, delimiter=",", strict=True)
            if next(lector, None) != ENCABEZADO:
                raise ArchivoInvalidoError("El encabezado del CSV es incorrecto.")

            for numero_fila, fila in enumerate(lector, start=2):
                if len(fila) < len(ENCABEZADO):
                    raise ArchivoInvalidoError(
                        f"La fila {numero_fila} tiene menos de siete columnas."
                    )
                try:
                    cancion = Cancion(
                        int(fila[0]), fila[1], fila[2], fila[3], fila[4],
                        int(fila[5]), int(fila[6]),
                    )
                except ValueError as error:
                    raise ArchivoInvalidoError(
                        f"La fila {numero_fila} tiene un id, año o duración inválidos."
                    ) from error
                biblioteca.agregar(cancion)
    except (OSError, UnicodeError, csv.Error) as error:
        raise ArchivoInvalidoError(f"No se pudo leer el CSV '{ruta}'.") from error
    return biblioteca


# hay que recorrer las filas anteriores porque los registros del CSV tienen
# longitud variable y se identifican al interpretar sus separadores y saltos de linea.
