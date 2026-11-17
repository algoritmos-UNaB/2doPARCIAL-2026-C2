from ejercicio_01 import Pokemon
from ejercicio_02 import Pokedex

class ArchivoInvalidoError(Exception):
    pass

def guardar_csv(ruta, pokedex):
    with open(ruta, "w", encoding="utf-8") as f:
        f.write("id,nombre,tipo1,tipo2,hp,ataque,defensa,velocidad,generacion\n")
        for p in pokedex.listar():
            f.write(f"{p.id},{p.nombre},{p.tipo1},{p.tipo2},{p.hp},{p.ataque},{p.defensa},{p.velocidad},{p.generacion}\n")

def cargar_csv(ruta):
    pokedex = Pokedex()
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            lineas = f.readlines()
    except Exception:
        raise ArchivoInvalidoError("No se pudo leer el archivo.")

    if not lineas:
        raise ArchivoInvalidoError("Archivo vacío.")

    encabezado = lineas[0].strip().split(",")
    if encabezado != ["id", "nombre", "tipo1", "tipo2", "hp", "ataque", "defensa", "velocidad", "generacion"]:
        raise ArchivoInvalidoError("Encabezado inválido.")

    for linea in lineas[1:]:
        linea = linea.strip()
        if not linea: continue
        columnas = linea.split(",")
        if len(columnas) != 9:
            raise ArchivoInvalidoError("Número de columnas incorrecto.")
            
        try:
            p = Pokemon(
                id=columnas[0],
                nombre=columnas[1],
                tipo1=columnas[2],
                tipo2=columnas[3],
                hp=columnas[4],
                ataque=columnas[5],
                defensa=columnas[6],
                velocidad=columnas[7],
                generacion=columnas[8]
            )
            pokedex.agregar(p)
        except ValueError:
            raise ArchivoInvalidoError("Error convirtiendo tipos numéricos.")
            
    return pokedex

# TEORIA
# Sí, hace falta leer los registros anteriores, ya que los archivos de texto son de tamaño variable y requieren acceso secuencial.