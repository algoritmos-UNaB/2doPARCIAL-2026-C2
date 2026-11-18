"""Ejercicio 10 — Archivo binario de recetas con struct (registros de longitud fija)."""

import struct

from ejercicio_01 import Receta
from ejercicio_04 import LibroRecetas
from ejercicio_09 import ArchivoInvalidoError

FORMATO_ENCABEZADO = "<4scI"           
FORMATO_REGISTRO = "<I32sH8s16s"       
TAM_ENCABEZADO = struct.calcsize(FORMATO_ENCABEZADO)   
TAM_REGISTRO = struct.calcsize(FORMATO_REGISTRO)       
MAGIA = b"AYED"
TEMA = b"R"


def _a_bytes(texto, ancho):
    """Texto -> UTF-8 recortado a `ancho` bytes (sin partir una letra como la ñ) y rellenado con \\0."""
    datos = texto.encode("utf-8")
    if len(datos) > ancho:
        datos = datos[:ancho].decode("utf-8", errors="ignore").encode("utf-8")
    return datos + b"\0" * (ancho - len(datos))


def _a_texto(datos):
    return datos.rstrip(b"\0").decode("utf-8")


def _empaquetar(receta):
    return struct.pack(
        FORMATO_REGISTRO,
        receta.id,
        _a_bytes(receta.nombre, 32),
        receta.tiempo_min,
        _a_bytes(receta.dificultad, 8),
        _a_bytes(receta.categoria, 16),
    )


def _desempaquetar(datos):
    id, nombre, tiempo_min, dificultad, categoria = struct.unpack(FORMATO_REGISTRO, datos)
    return Receta(id, _a_texto(nombre), tiempo_min, _a_texto(dificultad), _a_texto(categoria))


def _leer_encabezado(archivo, ruta):
    """Lee y valida el encabezado. Devuelve la cantidad de registros."""
    datos = archivo.read(TAM_ENCABEZADO)
    if len(datos) < TAM_ENCABEZADO:
        raise ArchivoInvalidoError(f"{ruta} es más corto que el encabezado ({TAM_ENCABEZADO} bytes).")
    magia, _tema, cantidad = struct.unpack(FORMATO_ENCABEZADO, datos)
    if magia != MAGIA:
        raise ArchivoInvalidoError(f"{ruta}: la magia es {magia!r} y debería ser {MAGIA!r}.")
    return cantidad


def guardar_binario(ruta, libro):
    recetas = libro.listar()
    with open(ruta, "wb") as archivo:
        archivo.write(struct.pack(FORMATO_ENCABEZADO, MAGIA, TEMA, len(recetas)))
        for receta in recetas:
            archivo.write(_empaquetar(receta))


def cargar_binario(ruta):
    libro = LibroRecetas()
    with open(ruta, "rb") as archivo:
        cantidad = _leer_encabezado(archivo, ruta)
        for posicion in range(cantidad):
            datos = archivo.read(TAM_REGISTRO)
            if len(datos) < TAM_REGISTRO:
                raise ArchivoInvalidoError(f"{ruta} está cortado: falta el registro {posicion}.")
            libro.agregar(_desempaquetar(datos))
    return libro


def actualizar_registro(ruta, posicion, receta):
    """Reescribe solo el registro `posicion` (desde 0). No toca el encabezado ni los demás registros."""
    with open(ruta, "r+b") as archivo:                        
        cantidad = _leer_encabezado(archivo, ruta)
        if not isinstance(posicion, int) or posicion < 0 or posicion >= cantidad:
            raise ArchivoInvalidoError(f"Posición {posicion} fuera de rango: hay {cantidad} registros (0 a {cantidad - 1}).")
        archivo.seek(TAM_ENCABEZADO + posicion * TAM_REGISTRO)   
        archivo.write(_empaquetar(receta))


# TEORIA
# Que todos los registros miden lo mismo (62 bytes, struct.calcsize del formato
# del registro) y el encabezado mide 9: el registro `posicion` empieza en el byte
# 9 + posicion * 62 (por ejemplo, la posición 3 empieza en el byte 195), y ahí se
# hace seek.


if __name__ == "__main__":
    import os
    import tempfile

    from ejercicio_02 import libro_examen

    ruta = os.path.join(tempfile.mkdtemp(), "recetas.bin")   # carpeta temporal
    guardar_binario(ruta, libro_examen(LibroRecetas()))
    print("tamaño:", os.path.getsize(ruta), "bytes = 9 + 7 x 62 =", 9 + 7 * 62)
    actualizar_registro(ruta, 4, Receta(9, "Asado con cuero", 300, "alta", "principal"))
    for receta in cargar_binario(ruta).listar():
        print("  ", receta)
    try:
        actualizar_registro(ruta, 7, Receta(99, "X", 1, "baja", "salsa"))
    except ArchivoInvalidoError as error:
        print("ArchivoInvalidoError:", error)
