"""Ejercicio 10. Registros binarios fijos y actualizacion por acceso directo."""

import struct

if __package__:
    from .ejercicio_01 import Cancion
    from .ejercicio_02 import Biblioteca
    from .ejercicio_09 import ArchivoInvalidoError
else:
    from ejercicio_01 import Cancion
    from ejercicio_02 import Biblioteca
    from ejercicio_09 import ArchivoInvalidoError


ENCABEZADO = struct.Struct("=4s1sI")
REGISTRO = struct.Struct("=I40s40s40s16sHH")
MAGIA = b"AYED"
TEMA = b"M"


def _codificar_texto(texto, ancho):
    # Si el límite corta un carácter UTF-8, se descarta ese carácter incompleto.
    datos = texto.encode("utf-8")[:ancho]
    return datos.decode("utf-8", errors="ignore").encode("utf-8")


def _empaquetar_cancion(cancion):
    # struct completa los campos de texto con bytes nulos hasta su ancho fijo.
    return REGISTRO.pack(
        cancion.id,
        _codificar_texto(cancion.titulo, 40),
        _codificar_texto(cancion.artista, 40),
        _codificar_texto(cancion.album, 40),
        _codificar_texto(cancion.genero, 16),
        cancion.anio,
        cancion.duracion_seg,
    )


def _decodificar_texto(datos):
    return datos.split(b"\0", 1)[0].decode("utf-8")


def _validar_archivo(archivo):
    """Valida encabezado y longitud, y deja el cursor en el primer registro."""
    archivo.seek(0)
    datos = archivo.read(ENCABEZADO.size)
    if len(datos) != ENCABEZADO.size:
        raise ArchivoInvalidoError("El encabezado binario está incompleto.")
    magia, tema, cantidad = ENCABEZADO.unpack(datos)
    if magia != MAGIA:
        raise ArchivoInvalidoError("La magia del archivo debe ser AYED.")
    if tema != TEMA:
        raise ArchivoInvalidoError("El tema del archivo debe ser M.")

    archivo.seek(0, 2)
    tamanio_esperado = ENCABEZADO.size + cantidad * REGISTRO.size
    if archivo.tell() != tamanio_esperado:
        raise ArchivoInvalidoError(
            f"El archivo debe tener exactamente {tamanio_esperado} bytes."
        )
    archivo.seek(ENCABEZADO.size)
    return cantidad


def guardar_binario(ruta, biblioteca):
    try:
        # Se preparan los registros antes de abrir el archivo de destino.
        registros = [_empaquetar_cancion(cancion) for cancion in biblioteca]
        encabezado = ENCABEZADO.pack(MAGIA, TEMA, len(registros))
        with open(ruta, "wb") as archivo:
            archivo.write(encabezado)
            for registro in registros:
                archivo.write(registro)
    except (OSError, UnicodeError, struct.error) as error:
        raise ArchivoInvalidoError(
            f"No se pudo guardar '{ruta}' con el formato binario de canciones."
        ) from error
    return len(registros)


def cargar_binario(ruta) -> Biblioteca:
    biblioteca = Biblioteca()
    try:
        with open(ruta, "rb") as archivo:
            cantidad = _validar_archivo(archivo)
            for posicion in range(cantidad):
                datos = archivo.read(REGISTRO.size)
                id, titulo, artista, album, genero, anio, duracion = REGISTRO.unpack(datos)
                biblioteca.agregar(Cancion(
                    id,
                    _decodificar_texto(titulo),
                    _decodificar_texto(artista),
                    _decodificar_texto(album),
                    _decodificar_texto(genero),
                    anio,
                    duracion,
                ))
    except (OSError, UnicodeError, struct.error) as error:
        raise ArchivoInvalidoError(
            f"No se pudo leer '{ruta}' con el formato binario de canciones."
        ) from error
    return biblioteca


def actualizar_registro(ruta, posicion, cancion):
    try:
        with open(ruta, "r+b") as archivo:
            cantidad = _validar_archivo(archivo)
            if not isinstance(posicion, int) or posicion < 0 or posicion >= cantidad:
                raise ArchivoInvalidoError(
                    f"La posición {posicion} está fuera del rango de registros."
                )
            registro = _empaquetar_cancion(cancion)
            archivo.seek(ENCABEZADO.size + posicion * REGISTRO.size)
            archivo.write(registro)
    except (OSError, UnicodeError, struct.error) as error:
        raise ArchivoInvalidoError(
            f"No se pudo actualizar el registro en el archivo '{ruta}'."
        ) from error
    return cancion


# El registro de poscion K empiecza en el byte
# tamaño_encabezado + k * tamaño_registro = 9 + k * 144
# los bytesse cuentan desde 0, por lo que el primer registro empieza en el byte 9