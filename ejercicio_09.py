import csv
from ejercicio_01 import Cancion
from ejercicio_02 import Biblioteca


class ArchivoInvalidoError(Exception):
    pass


def guardar_canciones_csv(ruta, biblioteca):
    with open(ruta, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)

        escritor.writerow([
            "id", "titulo", "artista", "album",
            "genero", "anio", "duracion_seg"
        ])

        for cancion in biblioteca:
            escritor.writerow([
                cancion.id,
                cancion.titulo,
                cancion.artista,
                cancion.album,
                cancion.genero,
                cancion.anio,
                cancion.duracion_seg
            ])


def cargar_canciones_csv(ruta) -> Biblioteca:
    biblioteca = Biblioteca()

    try:
        with open(ruta, "r", newline="", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)

            encabezado = next(lector, None)

            if encabezado != [
                "id", "titulo", "artista", "album",
                "genero", "anio", "duracion_seg"
            ]:
                raise ArchivoInvalidoError("Encabezado incorrecto.")

            for fila in lector:
                if len(fila) < 7:
                    raise ArchivoInvalidoError("Fila incompleta.")

                cancion = Cancion(
                    int(fila[0]),
                    fila[1],
                    fila[2],
                    fila[3],
                    fila[4],
                    int(fila[6]),  
                    int(fila[5])   
                )

                biblioteca.agregar(cancion)

    except FileNotFoundError:
        raise ArchivoInvalidoError("El archivo no existe.")

    return biblioteca



# Para leer la canción de la fila 50 hay que recorrer las filas anteriores, porque el CSV es un archivo de texto secuencial y no permite acceder directamente a una fila sin leer las filas previas