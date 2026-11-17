
import struct

from ejercicio_01 import Receta
from ejercicio_02 import LibroRecetas
from ejercicio_09 import ArchivoInvalidoError


FORMATO_ENCABEZADO = "<4scI"
FORMATO_REGISTRO = "<I32sH8s16s"

TAMANIO_ENCABEZADO = struct.calcsize(FORMATO_ENCABEZADO)
TAMANIO_REGISTRO = struct.calcsize(FORMATO_REGISTRO)


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
                registro = struct.pack(
                    FORMATO_REGISTRO,
                    receta.id,
                    receta.nombre.encode("utf-8")[:32].ljust(32, b"\0"),
                    receta.tiempo_min,
                    receta.dificultad.encode("utf-8")[:8].ljust(8, b"\0"),
                    receta.categoria.encode("utf-8")[:16].ljust(16, b"\0")
                )

                archivo.write(registro)

    except (OSError, struct.error):
        raise ArchivoInvalidoError("No se pudo guardar el archivo")


def cargar_binario(ruta):
    libro = LibroRecetas()

    try:
        with open(ruta, "rb") as archivo:
            encabezado = archivo.read(TAMANIO_ENCABEZADO)

            if len(encabezado) != TAMANIO_ENCABEZADO:
                raise ArchivoInvalidoError("Encabezado incompleto")

            magia, tema, cantidad = struct.unpack(
                FORMATO_ENCABEZADO, encabezado
            )

            if magia != b"AYED":
                raise ArchivoInvalidoError("Magia incorrecta")

            if tema != b"R":
                raise ArchivoInvalidoError("Tema incorrecto")

            for i in range(cantidad):
                datos = archivo.read(TAMANIO_REGISTRO)

                if len(datos) != TAMANIO_REGISTRO:
                    raise ArchivoInvalidoError("Registro incompleto")

                id_receta, nombre, tiempo, dificultad, categoria = struct.unpack(
                    FORMATO_REGISTRO, datos
                )

                receta = Receta(
                    id_receta,
                    nombre.rstrip(b"\0").decode("utf-8"),
                    tiempo,
                    dificultad.rstrip(b"\0").decode("utf-8"),
                    categoria.rstrip(b"\0").decode("utf-8")
                )

                libro.agregar(receta)

    except (OSError, struct.error, UnicodeDecodeError):
        raise ArchivoInvalidoError("Archivo binario invalido")

    return libro


def actualizar_registro(ruta, posicion, receta):
    try:
        with open(ruta, "r+b") as archivo:
            encabezado = archivo.read(TAMANIO_ENCABEZADO)

            if len(encabezado) != TAMANIO_ENCABEZADO:
                raise ArchivoInvalidoError("Encabezado incompleto")

            magia, tema, cantidad = struct.unpack(
                FORMATO_ENCABEZADO, encabezado
            )

            if magia != b"AYED":
                raise ArchivoInvalidoError("Magia incorrecta")

            if tema != b"R":
                raise ArchivoInvalidoError("Tema incorrecto")

            if posicion < 0 or posicion >= cantidad:
                raise ArchivoInvalidoError("Posicion fuera de rango")

            archivo.seek(
                TAMANIO_ENCABEZADO + posicion * TAMANIO_REGISTRO
            )

            registro = struct.pack(
                FORMATO_REGISTRO,
                receta.id,
                receta.nombre.encode("utf-8")[:32].ljust(32, b"\0"),
                receta.tiempo_min,
                receta.dificultad.encode("utf-8")[:8].ljust(8, b"\0"),
                receta.categoria.encode("utf-8")[:16].ljust(16, b"\0")
            )

            archivo.write(registro)

    except (OSError, struct.error):
        raise ArchivoInvalidoError("No se pudo actualizar el archivo")


# TEORIA
# El tamano fijo de cada registro permite calcular su posicion.Se suma el tamano del encabezado y se multiplica la posicion por el tamano del registro.
