import struct
import os

from ejercicio_1 import Receta
from ejercicio_2 import LibroRecetas
from ejercicio_9 import ArchivoInvalidoError


FORMATO_ENCABEZADO = "<4scI"
FORMATO_REGISTRO = "<I32sH8s16s"

TAMANIO_ENCABEZADO = struct.calcsize(FORMATO_ENCABEZADO)
TAMANIO_REGISTRO = struct.calcsize(FORMATO_REGISTRO)


def convertir_bytes(texto, ancho):

    datos = str(texto).encode("utf-8")

    if len(datos) > ancho:

        datos = datos[:ancho]

        while True:
            try:
                datos.decode("utf-8")
                break
            except UnicodeDecodeError:
                datos = datos[:-1]

    return datos.ljust(ancho, b"\0")


def empaquetar_receta(receta):

    try:
        return struct.pack(
            FORMATO_REGISTRO,
            int(receta.id),
            convertir_bytes(receta.nombre, 32),
            int(receta.tiempo_min),
            convertir_bytes(receta.dificultad, 8),
            convertir_bytes(receta.categoria, 16)
        )

    except (ValueError, TypeError, struct.error) as error:
        raise ArchivoInvalidoError(
            "Datos de receta inválidos"
        ) from error


def desempaquetar_receta(datos):

    id_receta, nombre, tiempo, dificultad, categoria = struct.unpack(
        FORMATO_REGISTRO,
        datos
    )

    try:
        return Receta(
            id_receta,
            nombre.rstrip(b"\0").decode("utf-8"),
            tiempo,
            dificultad.rstrip(b"\0").decode("utf-8"),
            categoria.rstrip(b"\0").decode("utf-8")
        )

    except UnicodeDecodeError as error:
        raise ArchivoInvalidoError(
            "Texto inválido en archivo binario"
        ) from error


def guardar_binario(ruta, libro):

    recetas = libro.listar()

    try:
        with open(ruta, "wb") as archivo:

            encabezado = struct.pack(
                FORMATO_ENCABEZADO,
                b"AYED",
                b"R",
                len(recetas)
            )

            archivo.write(encabezado)

            for receta in recetas:
                archivo.write(empaquetar_receta(receta))

    except OSError as error:
        raise ArchivoInvalidoError(
            "Error al guardar archivo binario"
        ) from error


def cargar_binario(ruta):

    try:
        with open(ruta, "rb") as archivo:

            encabezado = archivo.read(TAMANIO_ENCABEZADO)

            if len(encabezado) != TAMANIO_ENCABEZADO:
                raise ArchivoInvalidoError(
                    "Archivo incompleto"
                )

            magia, tema, cantidad = struct.unpack(
                FORMATO_ENCABEZADO,
                encabezado
            )

            if magia != b"AYED" or tema != b"R":
                raise ArchivoInvalidoError(
                    "Encabezado inválido"
                )

            tamanio_esperado = (
                TAMANIO_ENCABEZADO +
                cantidad * TAMANIO_REGISTRO
            )

            if os.fstat(archivo.fileno()).st_size != tamanio_esperado:
                raise ArchivoInvalidoError(
                    "Tamaño de archivo incorrecto"
                )

            libro = LibroRecetas()

            for i in range(cantidad):

                datos = archivo.read(TAMANIO_REGISTRO)

                if len(datos) != TAMANIO_REGISTRO:
                    raise ArchivoInvalidoError(
                        "Registro incompleto"
                    )

                receta = desempaquetar_receta(datos)

                libro.agregar(receta)

            return libro

    except OSError as error:
        raise ArchivoInvalidoError(
            "Error al leer archivo binario"
        ) from error


def actualizar_registro(ruta, posicion, receta):

    if not isinstance(posicion, int) or posicion < 0:
        raise ArchivoInvalidoError("Posición inválida")

    try:
        with open(ruta, "r+b") as archivo:

            encabezado = archivo.read(TAMANIO_ENCABEZADO)

            if len(encabezado) != TAMANIO_ENCABEZADO:
                raise ArchivoInvalidoError(
                    "Archivo incompleto"
                )

            magia, tema, cantidad = struct.unpack(
                FORMATO_ENCABEZADO,
                encabezado
            )

            if magia != b"AYED" or tema != b"R":
                raise ArchivoInvalidoError(
                    "Encabezado inválido"
                )

            if posicion >= cantidad:
                raise ArchivoInvalidoError(
                    "Posición fuera de rango"
                )

            tamanio_esperado = (
                TAMANIO_ENCABEZADO +
                cantidad * TAMANIO_REGISTRO
            )

            if os.fstat(archivo.fileno()).st_size != tamanio_esperado:
                raise ArchivoInvalidoError(
                    "Tamaño de archivo incorrecto"
                )

            desplazamiento = (
                TAMANIO_ENCABEZADO +
                posicion * TAMANIO_REGISTRO
            )

            archivo.seek(desplazamiento)

            archivo.write(empaquetar_receta(receta))

    except OSError as error:
        raise ArchivoInvalidoError(
            "Error al actualizar archivo"
        ) from error


# TEORIA:
# El tamaño fijo de cada registro permite calcular su posición.
# Se utiliza el encabezado de 9 bytes más la posición multiplicada
# por el tamaño de cada registro (62 bytes).