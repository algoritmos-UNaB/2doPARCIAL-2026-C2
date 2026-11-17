import struct

from ejercicio_01 import Pokemon
from ejercicio_02 import Pokedex
from ejercicio_09 import ArchivoInvalidoError

FORMATO_ENCABEZADO = "<4scI"
FORMATO_REGISTRO = "<I20s12s12s4H"
TAM_ENCABEZADO = struct.calcsize(FORMATO_ENCABEZADO)
TAM_REGISTRO = struct.calcsize(FORMATO_REGISTRO)


def _a_bytes(texto, ancho):
    datos = texto.encode("utf-8")[:ancho]
    return datos.decode("utf-8", errors="ignore").encode("utf-8")


def _empaquetar(p):
    return struct.pack(FORMATO_REGISTRO, p.id, _a_bytes(p.nombre, 20), _a_bytes(p.tipo1, 12),
                       _a_bytes(p.tipo2, 12), p.hp, p.ataque, p.defensa, p.velocidad)


def _desempaquetar(registro):
    id, nombre, tipo1, tipo2, hp, ataque, defensa, velocidad = struct.unpack(FORMATO_REGISTRO, registro)
    try:
        nombre = nombre.rstrip(b"\0").decode("utf-8")
        tipo1 = tipo1.rstrip(b"\0").decode("utf-8")
        tipo2 = tipo2.rstrip(b"\0").decode("utf-8")
    except UnicodeDecodeError:
        raise ArchivoInvalidoError("Texto inválido")
    return Pokemon(id, nombre, tipo1, tipo2, hp, ataque, defensa, velocidad, 1)


def _leer_encabezado(archivo):
    encabezado = archivo.read(TAM_ENCABEZADO)
    if len(encabezado) < TAM_ENCABEZADO:
        raise ArchivoInvalidoError("Archivo más corto que el encabezado")
    magia, tema, cantidad = struct.unpack(FORMATO_ENCABEZADO, encabezado)
    if magia != b"AYED":
        raise ArchivoInvalidoError("Magia incorrecta")
    if tema != b"P":
        raise ArchivoInvalidoError("Tema incorrecto")
    return cantidad


def guardar_binario(ruta, pokedex):
    pokemones = pokedex.listar()
    with open(ruta, "wb") as archivo:
        archivo.write(struct.pack(FORMATO_ENCABEZADO, b"AYED", b"P", len(pokemones)))
        for pokemon in pokemones:
            archivo.write(_empaquetar(pokemon))


def cargar_binario(ruta):
    pokedex = Pokedex()
    with open(ruta, "rb") as archivo:
        cantidad = _leer_encabezado(archivo)
        for _ in range(cantidad):
            registro = archivo.read(TAM_REGISTRO)
            if len(registro) < TAM_REGISTRO:
                raise ArchivoInvalidoError("Archivo incompleto")
            pokedex.agregar(_desempaquetar(registro))
    return pokedex


def actualizar_registro(ruta, posicion, pokemon):
    with open(ruta, "r+b") as archivo:
        cantidad = _leer_encabezado(archivo)
        if posicion < 0 or posicion >= cantidad:
            raise ArchivoInvalidoError("Posición fuera de rango")
        inicio = TAM_ENCABEZADO + posicion * TAM_REGISTRO
        archivo.seek(0, 2)
        if archivo.tell() < inicio + TAM_REGISTRO:
            raise ArchivoInvalidoError("Archivo incompleto")
        archivo.seek(inicio)
        archivo.write(_empaquetar(pokemon))


# TEORIA
# Como todos los registros ocupan lo mismo (56 bytes), puedo ir directo al que quiero haciendo 9 + posicion * 56.