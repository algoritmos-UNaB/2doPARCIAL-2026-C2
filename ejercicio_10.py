# TEORÍA: El dato del layout que permite calcular el byte exacto donde empieza cada registro es el
# tamaño fijo del encabezado (9 bytes) junto con el tamaño fijo de cada registro (56 bytes), ya que
# permite aplicar la fórmula de acceso directo: desplazamiento = 9 + posicion * 56.

import struct
from ejercicio_01 import Pokemon
from ejercicio_02 import Pokedex
from ejercicio_09 import ArchivoInvalidoError

FORMATO_ENCABEZADO = "<4sci"
TAM_ENCABEZADO = struct.calcsize(FORMATO_ENCABEZADO)  # 9 bytes

FORMATO_REGISTRO = "<i20s12s12s4H"
TAM_REGISTRO = struct.calcsize(FORMATO_REGISTRO)  # 56 bytes

MAGIA_ESPERADA = b"AYED"
TIPO_REGISTRO_POKEMON = b"P"


def _codificar_cadena(texto, ancho):
    if texto is None:
        texto = ""
    datos = texto.encode("utf-8")[:ancho]
    return datos.ljust(ancho, b"\x00")


def _decodificar_cadena(datos):
    return datos.rstrip(b"\x00").decode("utf-8")


def _empaquetar_pokemon(pokemon):
    return struct.pack(
        FORMATO_REGISTRO,
        pokemon.id,
        _codificar_cadena(pokemon.nombre, 20),
        _codificar_cadena(pokemon.tipo1, 12),
        _codificar_cadena(pokemon.tipo2, 12),
        pokemon.hp,
        pokemon.ataque,
        pokemon.defensa,
        pokemon.velocidad,
    )


def guardar_binario(ruta, pokedex):
    lista_pokemones = list(pokedex)
    encabezado = struct.pack(
        FORMATO_ENCABEZADO,
        MAGIA_ESPERADA,
        TIPO_REGISTRO_POKEMON,
        len(lista_pokemones),
    )
    with open(ruta, mode="wb") as archivo:
        archivo.write(encabezado)
        for pokemon in lista_pokemones:
            archivo.write(_empaquetar_pokemon(pokemon))


def cargar_binario(ruta):
    with open(ruta, mode="rb") as archivo:
        datos_encabezado = archivo.read(TAM_ENCABEZADO)
        if len(datos_encabezado) < TAM_ENCABEZADO:
            raise ArchivoInvalidoError("El archivo es más corto que el encabezado.")

        magia, tipo, cantidad = struct.unpack(FORMATO_ENCABEZADO, datos_encabezado)
        if magia != MAGIA_ESPERADA:
            raise ArchivoInvalidoError("La magia del encabezado no es 'AYED'.")
        if cantidad < 0:
            raise ArchivoInvalidoError("La cantidad de registros en el encabezado es inválida.")

        pokedex = Pokedex()
        for _ in range(cantidad):
            datos_registro = archivo.read(TAM_REGISTRO)
            if len(datos_registro) < TAM_REGISTRO:
                raise ArchivoInvalidoError("El archivo está truncado y faltan registros.")

            (
                id_poke,
                nombre_bytes,
                tipo1_bytes,
                tipo2_bytes,
                hp,
                ataque,
                defensa,
                velocidad,
            ) = struct.unpack(FORMATO_REGISTRO, datos_registro)

            nombre = _decodificar_cadena(nombre_bytes)
            tipo1 = _decodificar_cadena(tipo1_bytes)
            tipo2_str = _decodificar_cadena(tipo2_bytes)
            tipo2 = tipo2_str if tipo2_str != "" else None

            pokemon = Pokemon(
                id_poke,
                nombre,
                tipo1,
                tipo2,
                hp,
                ataque,
                defensa,
                velocidad,
                1,
            )
            pokedex.agregar(pokemon)

    return pokedex


def actualizar_registro(ruta, posicion, pokemon):
    with open(ruta, mode="r+b") as archivo:
        datos_encabezado = archivo.read(TAM_ENCABEZADO)
        if len(datos_encabezado) < TAM_ENCABEZADO:
            raise ArchivoInvalidoError("El archivo es más corto que el encabezado.")

        magia, _, cantidad = struct.unpack(FORMATO_ENCABEZADO, datos_encabezado)
        if magia != MAGIA_ESPERADA:
            raise ArchivoInvalidoError("La magia del encabezado no es 'AYED'.")

        if posicion < 0 or posicion >= cantidad:
            raise ArchivoInvalidoError("La posición del registro está fuera de rango.")

        offset = TAM_ENCABEZADO + posicion * TAM_REGISTRO
        archivo.seek(0, 2)
        if archivo.tell() < offset + TAM_REGISTRO:
            raise ArchivoInvalidoError("El archivo está truncado para alcanzar esa posición.")

        archivo.seek(offset)
        archivo.write(_empaquetar_pokemon(pokemon))