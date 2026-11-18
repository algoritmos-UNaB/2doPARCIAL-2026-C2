import os
import struct

from ejercicio_02 import Cancion, Biblioteca


class ArchivoInvalidoError(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)


FORMATO_ENCABEZADO = "=4s1sI"
FORMATO_REGISTRO = "=I40s40s40s16sHH"
TAM_ENCABEZADO = struct.calcsize(FORMATO_ENCABEZADO)      
TAM_REGISTRO = struct.calcsize(FORMATO_REGISTRO)          
MAGIA = b"AYED"
TEMA = b"M"


def _cadena_a_bytes(texto, ancho):
    return texto.encode("utf-8")[:ancho].ljust(ancho, b"\0")


def _bytes_a_cadena(datos):
    return datos.split(b"\0", 1)[0].decode("utf-8")


def _empaquetar_cancion(cancion):
    return struct.pack(
        FORMATO_REGISTRO,
        cancion.id,
        _cadena_a_bytes(cancion.titulo, 40),
        _cadena_a_bytes(cancion.artista, 40),
        _cadena_a_bytes(cancion.album, 40),
        _cadena_a_bytes(cancion.genero, 16),
        cancion.anio,
        cancion.duracion_seg,
    )


def _desempaquetar_cancion(datos):
    id, titulo, artista, album, genero, anio, duracion_seg = struct.unpack(
        FORMATO_REGISTRO, datos
    )
    return Cancion(
        id=id,
        titulo=_bytes_a_cadena(titulo),
        artista=_bytes_a_cadena(artista),
        album=_bytes_a_cadena(album),
        genero=_bytes_a_cadena(genero),
        anio=anio,
        duracion_seg=duracion_seg,
    )


def guardar_binario(ruta, biblioteca):
    canciones = list(biblioteca)
    with open(ruta, "wb") as archivo:
        archivo.write(struct.pack(FORMATO_ENCABEZADO, MAGIA, TEMA, len(canciones)))
        for cancion in canciones:
            archivo.write(_empaquetar_cancion(cancion))


def _leer_encabezado(archivo):
    datos = archivo.read(TAM_ENCABEZADO)
    if len(datos) != TAM_ENCABEZADO:
        raise ArchivoInvalidoError("El archivo no tiene un encabezado válido.")
    magia, tema, cantidad = struct.unpack(FORMATO_ENCABEZADO, datos)
    if magia != MAGIA:
        raise ArchivoInvalidoError("La magia del archivo no es AYED.")
    if tema != TEMA:
        raise ArchivoInvalidoError("El tema del archivo no es M.")
    return cantidad


def cargar_binario(ruta):
    if not os.path.exists(ruta):
        raise ArchivoInvalidoError(f"El archivo '{ruta}' no existe.")

    with open(ruta, "rb") as archivo:
        cantidad = _leer_encabezado(archivo)

        tamanio_esperado = TAM_ENCABEZADO + cantidad * TAM_REGISTRO
        tamanio_real = os.path.getsize(ruta)
        if tamanio_real != tamanio_esperado:
            raise ArchivoInvalidoError(
                f"Tamaño inválido: se esperaban {tamanio_esperado} bytes "
                f"y hay {tamanio_real}."
            )

        biblioteca = Biblioteca()
        for _ in range(cantidad):
            datos = archivo.read(TAM_REGISTRO)
            if len(datos) != TAM_REGISTRO:
                raise ArchivoInvalidoError("Registro incompleto.")
            biblioteca.agregar(_desempaquetar_cancion(datos))
        return biblioteca


def actualizar_registro(ruta, posicion, cancion):
    if not os.path.exists(ruta):
        raise ArchivoInvalidoError(f"El archivo '{ruta}' no existe.")

    with open(ruta, "r+b") as archivo:
        cantidad = _leer_encabezado(archivo)

        tamanio_esperado = TAM_ENCABEZADO + cantidad * TAM_REGISTRO
        tamanio_real = os.path.getsize(ruta)
        if tamanio_real != tamanio_esperado:
            raise ArchivoInvalidoError(
                f"Tamaño inválido: se esperaban {tamanio_esperado} bytes "
                f"y hay {tamanio_real}."
            )

        if posicion < 0 or posicion >= cantidad:
            raise ArchivoInvalidoError(
                f"Posición fuera de rango: {posicion} (cantidad={cantidad})."
            )

        archivo.seek(TAM_ENCABEZADO + posicion * TAM_REGISTRO)
        archivo.write(_empaquetar_cancion(cancion))


# Teoría:
# El registro de posición k (0-based) empieza en el byte
#     TAM_ENCABEZADO + k * TAM_REGISTRO
# es decir, 9 + k * 144.
