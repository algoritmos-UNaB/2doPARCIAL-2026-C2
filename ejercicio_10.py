import struct
from ejercicio_01 import Pokemon
from ejercicio_02 import Pokedex
from ejercicio_09 import ArchivoInvalidoError


FORMATO_ENCABEZADO = "<4scI"
FORMATO_REGISTRO = "<I20s12s12s4H"
TAM_ENCABEZADO = struct.calcsize(FORMATO_ENCABEZADO)
TAM_REGISTRO = struct.calcsize(FORMATO_REGISTRO)
MAGIA = b"AYED"
TEMA = b"P"


def empaquetar_registro(pokemon):
    return struct.pack(
        FORMATO_REGISTRO,
        pokemon.id,
        pokemon.nombre.encode("utf-8"),
        pokemon.tipo1.encode("utf-8"),
        pokemon.tipo2.encode("utf-8"),
        pokemon.hp,
        pokemon.ataque,
        pokemon.defensa,
        pokemon.velocidad,
    )


def leer_encabezado(archivo):
    datos = archivo.read(TAM_ENCABEZADO)
    if len(datos) < TAM_ENCABEZADO:
        raise ArchivoInvalidoError("El archivo es mas corto que el encabezado")
    magia, tema, cantidad = struct.unpack(FORMATO_ENCABEZADO, datos)
    if magia != MAGIA:
        raise ArchivoInvalidoError("Magia invalida")
    return cantidad


def guardar_binario(ruta, pokedex):
    pokemones = pokedex.listar()
    with open(ruta, "wb") as archivo:
        archivo.write(struct.pack(FORMATO_ENCABEZADO, MAGIA, TEMA, len(pokemones)))
        for pokemon in pokemones:
            archivo.write(empaquetar_registro(pokemon))


def cargar_binario(ruta):
    pokedex = Pokedex()
    with open(ruta, "rb") as archivo:
        cantidad = leer_encabezado(archivo)
        for i in range(cantidad):
            datos = archivo.read(TAM_REGISTRO)
            if len(datos) < TAM_REGISTRO:
                raise ArchivoInvalidoError("Registro incompleto")
            id, nombre, tipo1, tipo2, hp, ataque, defensa, velocidad = struct.unpack(FORMATO_REGISTRO, datos)
            pokemon = Pokemon(
                id,
                nombre.rstrip(b"\0").decode("utf-8", errors="ignore"),
                tipo1.rstrip(b"\0").decode("utf-8", errors="ignore"),
                tipo2.rstrip(b"\0").decode("utf-8", errors="ignore"),
                hp,
                ataque,
                defensa,
                velocidad,
                1,
            )
            pokedex.agregar(pokemon)
    return pokedex


def actualizar_registro(ruta, posicion, pokemon):
    with open(ruta, "r+b") as archivo:
        cantidad = leer_encabezado(archivo)
        if posicion < 0 or posicion >= cantidad:
            raise ArchivoInvalidoError("Posicion fuera de rango")
        archivo.seek(TAM_ENCABEZADO + posicion * TAM_REGISTRO)
        archivo.write(empaquetar_registro(pokemon))


# TEORIA -> Esto se puede ya que al saber el del encabezado y cada registro, se suma como base
# el del encabezado, y se multiplica el tamaño del registro por la posicion que me interesa