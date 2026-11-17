import struct
from ejercicio_01 import Pokemon
from ejercicio_09 import ArchivoInvalidoError


# Encabezado:
# 4 bytes de magia + 1 byte de tema + 4 bytes de cantidad = 9 bytes
FORMATO_ENCABEZADO = "<4scI"

# Registro:
# id (4), nombre (20), tipo1 (12), tipo2 (12),
# hp (2), ataque (2), defensa (2), velocidad (2) = 56 bytes
FORMATO_REGISTRO = "<I20s12s12s4H"

TAMANO_ENCABEZADO = struct.calcsize(FORMATO_ENCABEZADO)
TAMANO_REGISTRO = struct.calcsize(FORMATO_REGISTRO)

MAGIA = b"AYED"
TEMA = b"P"


def guardar_binario(pokemones, ruta):
    with open(ruta, "wb") as archivo:
        encabezado = struct.pack(
            FORMATO_ENCABEZADO,
            MAGIA,
            TEMA,
            len(pokemones)
        )

        archivo.write(encabezado)

        for pokemon in pokemones:
            nombre = pokemon.nombre.encode("utf-8")
            tipo1 = pokemon.tipo1.encode("utf-8")
            tipo2 = (
                pokemon.tipo2.encode("utf-8")
                if pokemon.tipo2 is not None
                else b""
            )

            if len(nombre) > 20 or len(tipo1) > 12 or len(tipo2) > 12:
                raise ArchivoInvalidoError(
                    "Un nombre o tipo supera el tamaño permitido"
                )

            registro = struct.pack(
                FORMATO_REGISTRO,
                pokemon.id,
                nombre,
                tipo1,
                tipo2,
                pokemon.hp,
                pokemon.ataque,
                pokemon.defensa,
                pokemon.velocidad
            )

            archivo.write(registro)


def cargar_binario(ruta):
    pokemones = []

    try:
        with open(ruta, "rb") as archivo:
            datos_encabezado = archivo.read(TAMANO_ENCABEZADO)

            if len(datos_encabezado) != TAMANO_ENCABEZADO:
                raise ArchivoInvalidoError("Encabezado incompleto")

            magia, tema, cantidad = struct.unpack(
                FORMATO_ENCABEZADO,
                datos_encabezado
            )

            if magia != MAGIA or tema != TEMA:
                raise ArchivoInvalidoError("Formato de archivo incorrecto")

            datos = archivo.read()

            if len(datos) != cantidad * TAMANO_REGISTRO:
                raise ArchivoInvalidoError("Tamaño de archivo incorrecto")

            for i in range(cantidad):
                inicio = i * TAMANO_REGISTRO
                fin = inicio + TAMANO_REGISTRO

                registro = struct.unpack(
                    FORMATO_REGISTRO,
                    datos[inicio:fin]
                )

                identificador = registro[0]
                nombre = registro[1].split(b"\0")[0].decode("utf-8")
                tipo1 = registro[2].split(b"\0")[0].decode("utf-8")
                tipo2 = registro[3].split(b"\0")[0].decode("utf-8")

                hp = registro[4]
                ataque = registro[5]
                defensa = registro[6]
                velocidad = registro[7]

                pokemon = Pokemon(
                    identificador,
                    nombre,
                    tipo1,
                    tipo2 if tipo2 != "" else None,
                    hp,
                    ataque,
                    defensa,
                    velocidad,
                    1
                )

                pokemones.append(pokemon)

    except OSError as error:
        raise ArchivoInvalidoError(
            f"No se pudo abrir o leer el archivo: {error}"
        )

    return pokemones


def actualizar_registro(ruta, posicion, pokemon):
    try:
        with open(ruta, "r+b") as archivo:
            datos_encabezado = archivo.read(TAMANO_ENCABEZADO)

            if len(datos_encabezado) != TAMANO_ENCABEZADO:
                raise ArchivoInvalidoError("Encabezado incompleto")

            magia, tema, cantidad = struct.unpack(
                FORMATO_ENCABEZADO,
                datos_encabezado
            )

            if magia != MAGIA or tema != TEMA:
                raise ArchivoInvalidoError("Formato de archivo incorrecto")

            if posicion < 0 or posicion >= cantidad:
                raise ArchivoInvalidoError("Posición fuera de rango")

            archivo.seek(0, 2)
            tamano_archivo = archivo.tell()

            if tamano_archivo != TAMANO_ENCABEZADO + cantidad * TAMANO_REGISTRO:
                raise ArchivoInvalidoError("Tamaño de archivo incorrecto")

            nombre = pokemon.nombre.encode("utf-8")
            tipo1 = pokemon.tipo1.encode("utf-8")
            tipo2 = (
                pokemon.tipo2.encode("utf-8")
                if pokemon.tipo2 is not None
                else b""
            )

            if len(nombre) > 20 or len(tipo1) > 12 or len(tipo2) > 12:
                raise ArchivoInvalidoError(
                    "Un nombre o tipo supera el tamaño permitido"
                )

            registro = struct.pack(
                FORMATO_REGISTRO,
                pokemon.id,
                nombre,
                tipo1,
                tipo2,
                pokemon.hp,
                pokemon.ataque,
                pokemon.defensa,
                pokemon.velocidad
            )

            posicion_archivo = (
                TAMANO_ENCABEZADO + posicion * TAMANO_REGISTRO
            )

            archivo.seek(posicion_archivo)
            archivo.write(registro)

    except OSError as error:
        raise ArchivoInvalidoError(
            f"No se pudo modificar el archivo: {error}"
        )


#Teoria
#El tamanio fijo de cada registro y el tamanio del encabezado, porque 
# permiten calcular el byte exacto donde comienza el Pokemon que queremos
# modificar