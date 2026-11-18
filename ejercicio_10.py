import os
import struct

from ejercicio_01 import Cancion
from ejercicio_02 import Biblioteca
from ejercicio_09 import ArchivoInvalidoError

FORMATO_ENCABEZADO = "=4s1sI"
FORMATO_REGISTRO = "=I40s40s40s16sHH"
TAMANIO_ENCABEZADO = struct.calcsize(FORMATO_ENCABEZADO) # 9
TAMANIO_REGISTRO = struct.calcsize(FORMATO_REGISTRO)     # 144


def _empaquetar(c):
    return struct.pack(FORMATO_REGISTRO, c.id,
                       c.titulo.encode("utf-8"), c.artista.encode("utf-8"),
                       c.album.encode("utf-8"), c.genero.encode("utf-8"),
                       c.anio, c.duracion_seg)


def texto(datos):
    # se corta en el primer \0
    return datos.split(b"\0")[0].decode("utf-8", errors="ignore")


def leer_cantidad(ruta, archivo):
    """Valida el encabezado y el tamaño. Devuelve la cantidad de registros."""
    if os.path.getsize(ruta) < TAMANIO_ENCABEZADO:
        raise ArchivoInvalidoError("El archivo no tiene encabezado completo")
    magia, tema, cantidad = struct.unpack(FORMATO_ENCABEZADO, archivo.read(TAMANIO_ENCABEZADO))
    if magia != b"AYED":
        raise ArchivoInvalidoError("La magia no es AYED")
    if tema != b"M":
        raise ArchivoInvalidoError("El tema no es M")
    if os.path.getsize(ruta) != TAMANIO_ENCABEZADO + cantidad * TAMANIO_REGISTRO:
        raise ArchivoInvalidoError("El tamaño del archivo no coincide")
    return cantidad


def guardar_binario(ruta, biblioteca):
    canciones = list(biblioteca)
    with open(ruta, "wb") as archivo:
        archivo.write(struct.pack(FORMATO_ENCABEZADO, b"AYED", b"M", len(canciones)))
        for c in canciones:
            archivo.write(empaquetar(c))


def cargar_binario(ruta) -> Biblioteca:
    biblioteca = Biblioteca()
    with open(ruta, "rb") as archivo:
        cantidad = leer_cantidad(ruta, archivo)
        for _ in range(cantidad):
            id, titulo, artista, album, genero, anio, dur = struct.unpack(
                FORMATO_REGISTRO, archivo.read(TAMANIO_REGISTRO))
            biblioteca.agregar(Cancion(id, texto(titulo), texto(artista),
                                       texto(album), texto(genero), anio, dur))
    return biblioteca


def actualizar_registro(ruta, posicion, cancion):
    with open(ruta, "r+b") as archivo:
        cantidad = leer_cantidad(ruta, archivo)
        if posicion < 0 or posicion >= cantidad:
            raise ArchivoInvalidoError("La posición está fuera de rango")
        archivo.seek(TAMANIO_ENCABEZADO + posicion * TAMANIO_REGISTRO)
        archivo.write(empaquetar(cancion))


# TEORIA
# El registro de posición k empieza en el byte:
# TAMANIO_ENCABEZADO + k * TAMANIO_REGISTRO = 9 + k * 144
# (se salta el encabezado de 9 bytes y k registros completos de 144 bytes).