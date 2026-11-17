import struct
from ejercicio_01 import Cancion
from ejercicio_02 import Biblioteca
from ejercicio_09 import ArchivoInvalidoError


FORMATO_ENCABEZADO = "=4s1sI"
FORMATO_CANCION = "=I40s40s40s16sHH"

TAMANIO_ENCABEZADO = 9
TAMANIO_REGISTRO = 144


def convertir_texto(texto, tamanio):
    return texto.encode("utf-8")[:tamanio].ljust(tamanio, b"\0")


def leer_texto(texto):
    return texto.split(b"\0", 1)[0].decode("utf-8")


def guardar_binario(ruta, biblioteca):
    with open(ruta, "wb") as archivo:
        archivo.write(struct.pack(
            FORMATO_ENCABEZADO,
            b"AYED",
            b"M",
            biblioteca.cantidad()
        ))

        for cancion in biblioteca:
            registro = struct.pack(
                FORMATO_CANCION,
                cancion.id,
                convertir_texto(cancion.titulo, 40),
                convertir_texto(cancion.artista, 40),
                convertir_texto(cancion.album, 40),
                convertir_texto(cancion.genero, 16),
                cancion.anio,
                cancion.duracion_seg
            )

            archivo.write(registro)


def cargar_binario(ruta) -> Biblioteca:
    biblioteca = Biblioteca()

    try:
        with open(ruta, "rb") as archivo:
            encabezado = archivo.read(TAMANIO_ENCABEZADO)

            if len(encabezado) != TAMANIO_ENCABEZADO:
                raise ArchivoInvalidoError("Encabezado incompleto.")

            magia, tema, cantidad = struct.unpack(
                FORMATO_ENCABEZADO, encabezado
            )

            if magia != b"AYED":
                raise ArchivoInvalidoError("Magia incorrecta.")

            if tema != b"M":
                raise ArchivoInvalidoError("Tema incorrecto.")

            if len(archivo.read()) != cantidad * TAMANIO_REGISTRO:
                raise ArchivoInvalidoError("Tamaño de archivo incorrecto.")

            archivo.seek(TAMANIO_ENCABEZADO)

            for i in range(cantidad):
                datos = archivo.read(TAMANIO_REGISTRO)

                id_cancion, titulo, artista, album, genero, anio, duracion = (
                    struct.unpack(FORMATO_CANCION, datos)
                )

                cancion = Cancion(
                    id_cancion,
                    leer_texto(titulo),
                    leer_texto(artista),
                    leer_texto(album),
                    leer_texto(genero),
                    anio,
                    duracion
                )

                biblioteca.agregar(cancion)

    except FileNotFoundError:
        raise ArchivoInvalidoError("El archivo no existe.")

    return biblioteca


def actualizar_registro(ruta, posicion, cancion):
    try:
        with open(ruta, "r+b") as archivo:
            encabezado = archivo.read(TAMANIO_ENCABEZADO)

            if len(encabezado) != TAMANIO_ENCABEZADO:
                raise ArchivoInvalidoError("Encabezado incompleto.")

            magia, tema, cantidad = struct.unpack(
                FORMATO_ENCABEZADO, encabezado
            )

            if magia != b"AYED":
                raise ArchivoInvalidoError("Magia incorrecta.")

            if tema != b"M":
                raise ArchivoInvalidoError("Tema incorrecto.")

            archivo.seek(0, 2)

            if archivo.tell() != TAMANIO_ENCABEZADO + cantidad * TAMANIO_REGISTRO:
                raise ArchivoInvalidoError("Tamaño de archivo incorrecto.")

            if posicion < 0 or posicion >= cantidad:
                raise ArchivoInvalidoError("Posición fuera de rango.")

            registro = struct.pack(
                FORMATO_CANCION,
                cancion.id,
                convertir_texto(cancion.titulo, 40),
                convertir_texto(cancion.artista, 40),
                convertir_texto(cancion.album, 40),
                convertir_texto(cancion.genero, 16),
                cancion.anio,
                cancion.duracion_seg
            )

     
            archivo.seek(posicion * TAMANIO_REGISTRO)
            archivo.write(registro)

    except FileNotFoundError:
        raise ArchivoInvalidoError("El archivo no existe.")



# El byte donde empieza el registro de posición k se calcula como: 9 + k * 144
# Se suman los 9 bytes del encabezado y los 144 bytes de cada registro previo