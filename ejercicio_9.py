import csv

from ejercicio_1 import Receta
from ejercicio_2 import LibroRecetas


class ArchivoInvalidoError(Exception):
    pass


def guardar_recetas_csv(ruta, libro):

    encabezado = [
        "id",
        "nombre",
        "tiempo_min",
        "dificultad",
        "categoria"
    ]

    try:
        with open(ruta, "w", newline="", encoding="utf-8") as archivo:

            escritor = csv.writer(archivo)
            escritor.writerow(encabezado)

            for receta in libro.listar():

                escritor.writerow([
                    receta.id,
                    receta.nombre,
                    receta.tiempo_min,
                    receta.dificultad,
                    receta.categoria
                ])

    except OSError as error:
        raise ArchivoInvalidoError("Error al guardar recetas") from error


def cargar_recetas_csv(ruta):

    encabezado = [
        "id",
        "nombre",
        "tiempo_min",
        "dificultad",
        "categoria"
    ]

    libro = LibroRecetas()

    try:
        with open(ruta, "r", newline="", encoding="utf-8") as archivo:

            lector = csv.reader(archivo)

            primera_fila = next(lector, None)

            if primera_fila != encabezado:
                raise ArchivoInvalidoError("Encabezado inválido")

            for numero, fila in enumerate(lector, start=2):

                if len(fila) != 5:
                    raise ArchivoInvalidoError(
                        f"Cantidad de columnas incorrecta en fila {numero}"
                    )

                try:
                    id_receta = int(fila[0])
                    tiempo = int(fila[2])

                except ValueError as error:
                    raise ArchivoInvalidoError(
                        f"Número inválido en fila {numero}"
                    ) from error

                receta = Receta(
                    id_receta,
                    fila[1],
                    tiempo,
                    fila[3],
                    fila[4]
                )

                libro.agregar(receta)

    except (OSError, UnicodeError, csv.Error) as error:
        raise ArchivoInvalidoError("Error al leer recetas") from error

    return libro


def guardar_ingredientes_csv(ruta, ingredientes):

    encabezado = [
        "receta_id",
        "nombre",
        "cantidad",
        "unidad"
    ]

    try:
        with open(ruta, "w", newline="", encoding="utf-8") as archivo:

            escritor = csv.writer(archivo)
            escritor.writerow(encabezado)
            escritor.writerows(ingredientes)

    except OSError as error:
        raise ArchivoInvalidoError(
            "Error al guardar ingredientes"
        ) from error


def cargar_ingredientes_csv(ruta):

    encabezado = [
        "receta_id",
        "nombre",
        "cantidad",
        "unidad"
    ]

    resultado = []

    try:
        with open(ruta, "r", newline="", encoding="utf-8") as archivo:

            lector = csv.reader(archivo)

            primera_fila = next(lector, None)

            if primera_fila != encabezado:
                raise ArchivoInvalidoError("Encabezado inválido")

            for numero, fila in enumerate(lector, start=2):

                if len(fila) != 4:
                    raise ArchivoInvalidoError(
                        f"Cantidad de columnas incorrecta en fila {numero}"
                    )

                try:
                    receta_id = int(fila[0])
                    cantidad_float = float(fila[2])

                    if cantidad_float.is_integer():
                        cantidad = int(cantidad_float)
                    else:
                        cantidad = cantidad_float

                except ValueError as error:
                    raise ArchivoInvalidoError(
                        f"Número inválido en fila {numero}"
                    ) from error

                resultado.append((
                    receta_id,
                    fila[1],
                    cantidad,
                    fila[3]
                ))

    except (OSError, UnicodeError, csv.Error) as error:
        raise ArchivoInvalidoError(
            "Error al leer ingredientes"
        ) from error

    return resultado


# TEORIA:
# Sí, hace falta leer los registros anteriores porque el acceso
# a un archivo CSV es secuencial y no directo.