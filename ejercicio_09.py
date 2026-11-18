"""Ejercicio 9 — Archivo de texto: recetas e ingredientes en CSV.

CSV con encabezado, UTF-8 y separador coma. Se usa el módulo csv de la
biblioteca estándar, que además resuelve los nombres que tengan comas.
"""

import csv

from ejercicio_01 import Receta
from ejercicio_04 import LibroRecetas

ENCABEZADO_RECETAS = ["id", "nombre", "tiempo_min", "dificultad", "categoria"]
ENCABEZADO_INGREDIENTES = ["receta_id", "nombre", "cantidad", "unidad"]


class ArchivoInvalidoError(Exception):
    """El archivo no tiene el formato esperado."""


def _a_entero(texto, ruta, numero_linea):
    try:
        return int(texto)
    except ValueError:
        raise ArchivoInvalidoError(f"{ruta}, línea {numero_linea}: {texto!r} no es un número entero.") from None


def _a_numero(texto, ruta, numero_linea):
    """Entero si se puede (50); si no, decimal (0.5)."""
    try:
        return int(texto)
    except ValueError:
        pass
    try:
        return float(texto)
    except ValueError:
        raise ArchivoInvalidoError(f"{ruta}, línea {numero_linea}: {texto!r} no es un número.") from None


def _leer_filas(ruta, encabezado):
    """Lee el CSV en forma secuencial y devuelve [(numero_linea, fila)] sin el encabezado.

    Valida que la primera línea sea el encabezado y que cada fila tenga la
    cantidad de columnas de la tabla. Las líneas en blanco se ignoran.
    """
    filas = []
    try:
        with open(ruta, encoding="utf-8", newline="") as archivo:
            lector = csv.reader(archivo)
            primera = True
            for fila in lector:
                if len(fila) == 0:
                    continue
                if primera:
                    primera = False
                    if [campo.strip() for campo in fila] != encabezado:
                        raise ArchivoInvalidoError(
                            f"{ruta}: falta el encabezado {','.join(encabezado)} (primera línea: {','.join(fila)})."
                        )
                    continue
                if len(fila) != len(encabezado):
                    raise ArchivoInvalidoError(
                        f"{ruta}, línea {lector.line_num}: tiene {len(fila)} columnas y deberían ser {len(encabezado)}."
                    )
                filas.append((lector.line_num, [campo.strip() for campo in fila]))
    except UnicodeDecodeError:
        raise ArchivoInvalidoError(f"{ruta} no está en UTF-8.") from None
    if primera:
        raise ArchivoInvalidoError(f"{ruta} está vacío: no tiene encabezado.")
    return filas


def guardar_recetas_csv(ruta, libro):
    with open(ruta, "w", encoding="utf-8", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(ENCABEZADO_RECETAS)
        for receta in libro.listar():
            escritor.writerow([receta.id, receta.nombre, receta.tiempo_min, receta.dificultad, receta.categoria])


def cargar_recetas_csv(ruta):
    libro = LibroRecetas()
    for numero, (id, nombre, tiempo_min, dificultad, categoria) in _leer_filas(ruta, ENCABEZADO_RECETAS):
        libro.agregar(Receta(
            _a_entero(id, ruta, numero),
            nombre,
            _a_entero(tiempo_min, ruta, numero),
            dificultad,
            categoria,
        ))
    return libro


def guardar_ingredientes_csv(ruta, ingredientes):
    with open(ruta, "w", encoding="utf-8", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(ENCABEZADO_INGREDIENTES)
        for receta_id, nombre, cantidad, unidad in ingredientes:
            escritor.writerow([receta_id, nombre, cantidad, unidad])


def cargar_ingredientes_csv(ruta):
    ingredientes = []
    for numero, (receta_id, nombre, cantidad, unidad) in _leer_filas(ruta, ENCABEZADO_INGREDIENTES):
        ingredientes.append((_a_entero(receta_id, ruta, numero), nombre, _a_numero(cantidad, ruta, numero), unidad))
    return ingredientes


# TEORIA
# Sí, hace falta leer los anteriores: las líneas del CSV tienen largo variable,
# así que no se puede calcular en qué byte empieza el registro 10 y hay que
# leer línea por línea hasta llegar. El acceso es secuencial.


if __name__ == "__main__":
    import os
    import tempfile

    from ejercicio_02 import libro_examen
    from ejercicio_03 import INGREDIENTES_EXAMEN

    carpeta = tempfile.mkdtemp()   # los archivos de prueba van a una carpeta temporal
    ruta_recetas = os.path.join(carpeta, "recetas.csv")
    ruta_ingredientes = os.path.join(carpeta, "ingredientes.csv")
    ruta_mala = os.path.join(carpeta, "sin_encabezado.csv")
    guardar_recetas_csv(ruta_recetas, libro_examen(LibroRecetas()))
    guardar_ingredientes_csv(ruta_ingredientes, INGREDIENTES_EXAMEN)
    libro = cargar_recetas_csv(ruta_recetas)
    print(libro.cantidad(), "recetas leídas; la 9 es", libro.obtener(9))
    ingredientes = cargar_ingredientes_csv(ruta_ingredientes)
    print(len(ingredientes), "ingredientes; iguales a los originales:", ingredientes == INGREDIENTES_EXAMEN)

    with open(ruta_mala, "w", encoding="utf-8") as archivo:
        archivo.write("1,Chimichurri,15,baja,salsa\n")
    try:
        cargar_recetas_csv(ruta_mala)
    except ArchivoInvalidoError as error:
        print("ArchivoInvalidoError:", error)
