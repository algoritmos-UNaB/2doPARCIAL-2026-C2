import struct
from ejercicio_01 import Pokemon
from ejercicio_02 import Pokedex
from ejercicio_09 import ArchivoInvalidoError

FMT_ENCABEZADO = "<4scI"
TAM_ENCABEZADO = struct.calcsize(FMT_ENCABEZADO)
FMT_REGISTRO = "<I20s12s12s4H" 
TAM_REGISTRO = struct.calcsize(FMT_REGISTRO)

def _preparar_str(texto, longitud):
    return texto.encode("utf-8").ljust(longitud, b"\0")[:longitud]

def _limpiar_str(b_texto):
    return b_texto.decode("utf-8").rstrip("\0")

def guardar_binario(ruta, pokedex):
    pokemones = pokedex.listar()
    with open(ruta, "wb") as f:
        f.write(struct.pack(FMT_ENCABEZADO, b"AYED", b"P", len(pokemones)))
        for p in pokemones:
            f.write(struct.pack(
                FMT_REGISTRO, p.id,
                _preparar_str(p.nombre, 20),
                _preparar_str(p.tipo1, 12),
                _preparar_str(p.tipo2, 12),
                p.hp, p.ataque, p.defensa, p.velocidad
            ))

def cargar_binario(ruta):
    pokedex = Pokedex()
    try:
        with open(ruta, "rb") as f:
            header_data = f.read(TAM_ENCABEZADO)
            if len(header_data) < TAM_ENCABEZADO:
                raise ArchivoInvalidoError("Archivo demasiado corto para el encabezado.")
                
            magia, tema, cantidad = struct.unpack(FMT_ENCABEZADO, header_data)
            if magia != b"AYED":
                raise ArchivoInvalidoError("Firma mágica incorrecta.")
                
            for _ in range(cantidad):
                reg_data = f.read(TAM_REGISTRO)
                if len(reg_data) < TAM_REGISTRO:
                    raise ArchivoInvalidoError("Faltan bytes de un registro esperado.")
                    
                datos = struct.unpack(FMT_REGISTRO, reg_data)
                pokedex.agregar(Pokemon(
                    id=datos[0],
                    nombre=_limpiar_str(datos[1]),
                    tipo1=_limpiar_str(datos[2]),
                    tipo2=_limpiar_str(datos[3]),
                    hp=datos[4], ataque=datos[5],
                    defensa=datos[6], velocidad=datos[7],
                    generacion=1
                ))
    except FileNotFoundError:
        raise ArchivoInvalidoError("El archivo no existe.")
    return pokedex

def actualizar_registro(ruta, posicion, pokemon):
    try:
        with open(ruta, "r+b") as f:
            f.seek(0, 2)
            peso_archivo = f.tell()
            offset = TAM_ENCABEZADO + (posicion * TAM_REGISTRO)
            
            if offset + TAM_REGISTRO > peso_archivo:
                raise ArchivoInvalidoError("Posición fuera de rango.")
                
            f.seek(0)
            magia, = struct.unpack("<4s", f.read(4))
            if magia != b"AYED":
                raise ArchivoInvalidoError("Firma mágica incorrecta.")
                
            f.seek(offset)
            f.write(struct.pack(
                FMT_REGISTRO, pokemon.id,
                _preparar_str(pokemon.nombre, 20),
                _preparar_str(pokemon.tipo1, 12),
                _preparar_str(pokemon.tipo2, 12),
                pokemon.hp, pokemon.ataque, pokemon.defensa, pokemon.velocidad
            ))
    except FileNotFoundError:
        raise ArchivoInvalidoError("Archivo no encontrado.")

# TEORIA
# Al tener un layout de longitud fija, se sabe que el registro de cada Pokémon pesa exactamente 56 bytes y el encabezado 9, permitiendo calcular el byte inicial con la fórmula (9 + posición * 56).