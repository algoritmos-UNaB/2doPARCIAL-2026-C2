
import csv

from ejercicio_01 import Receta
from ejercicio_02 import LibroRecetas


class ArchivoInvalidoError(Exception):
    pass


def guardar_recetas_csv(ruta, libro):
    try:
        with open(ruta, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)

            escritor.writerow([
                "id", "nombre", "tiempo_min", "dificultad", "categoria"
            ])

            for receta in libro.listar():
                escritor.writerow([
                    receta.id,
                    receta.nombre,
                    receta.tiempo_min,
                    receta.dificultad,
                    receta.categoria
                ])

    except OSError:
        raise ArchivoInvalidoError("No se pudo guardar el archivo")


def cargar_recetas_csv(ruta):
    libro = LibroRecetas()

    try:
        with open(ruta, "r", newline="", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)

            encabezado = next(lector, None)

            if encabezado != [
                "id", "nombre", "tiempo_min", "dificultad", "categoria"
            ]:
                raise ArchivoInvalidoError("Encabezado incorrecto")

            for fila in lector:
                if len(fila) != 5:
                    raise ArchivoInvalidoError("Cantidad de columnas incorrecta")

                try:
                    receta = Receta(
                        int(fila[0]),
                        fila[1],
                        int(fila[2]),
                        fila[3],
                        fila[4]
                    )
                except ValueError:
                    raise ArchivoInvalidoError("Dato numerico incorrecto")

                libro.agregar(receta)

    except (OSError, csv.Error):
        raise ArchivoInvalidoError("No se pudo leer el archivo")

    return libro


def guardar_ingredientes_csv(ruta, ingredientes):
    try:
        with open(ruta, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)

            escritor.writerow([
                "receta_id", "nombre", "cantidad", "unidad"
            ])

            escritor.writerows(ingredientes)

    except OSError:
        raise ArchivoInvalidoError("No se pudo guardar el archivo")


def cargar_ingredientes_csv(ruta):
    ingredientes = []

    try:
        with open(ruta, "r", newline="", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)

            encabezado = next(lector, None)

            if encabezado != [
                "receta_id", "nombre", "cantidad", "unidad"
            ]:
                raise ArchivoInvalidoError("Encabezado incorrecto")

            for fila in lector:
                if len(fila) != 4:
                    raise ArchivoInvalidoError("Cantidad de columnas incorrecta")

                try:
                    receta_id = int(fila[0])
                    cantidad = int(fila[2])
                except ValueError:
                    raise ArchivoInvalidoError("Dato numerico incorrecto")

                ingredientes.append((
                    receta_id, fila[1], cantidad, fila[3]
                ))

    except (OSError, csv.Error):
        raise ArchivoInvalidoError("No se pudo leer el archivo")

    return ingredientes


# TEORIA
# No, porque la lectura de un archivo de texto es secuencial. Hay que leer los registros anteriores para llegar al numero 10.
