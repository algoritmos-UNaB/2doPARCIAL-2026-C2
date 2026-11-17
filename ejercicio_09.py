from ejercicio_01 import Receta
from ejercicio_02 import LibroRecetas

class ArchivoInvalidoError(Exception):
    pass

def guardar_recetas_csv(ruta, libro):
    with open(ruta, "w", encoding="utf-8") as f:
        f.write("id,nombre,tiempo_min,dificultad,categoria\n")
        for r in libro.listar():
            f.write(f"{r.id},{r.nombre},{r.tiempo_min},{r.dificultad},{r.categoria}\n")

def cargar_recetas_csv(ruta):
    libro = LibroRecetas()
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            encabezado = f.readline().strip()
            if encabezado != "id,nombre,tiempo_min,dificultad,categoria":
                raise ArchivoInvalidoError("Encabezado inválido o faltante.")
            
            for linea in f:
                campos = linea.strip().split(',')
                if len(campos) != 5:
                    raise ArchivoInvalidoError("Cantidad de columnas incorrecta.")
                try:
                    r_id = int(campos[0])
                    tiempo = int(campos[2])
                except ValueError:
                    raise ArchivoInvalidoError("Error de tipo numérico en fila.")
                libro.agregar(Receta(r_id, campos[1], tiempo, campos[3], campos[4]))
    except FileNotFoundError:
        raise ArchivoInvalidoError("El archivo de recetas no existe.")
    return libro


def guardar_ingredientes_csv(ruta, ingredientes):
    with open(ruta, "w", encoding="utf-8") as f:
        f.write("receta_id,nombre,cantidad,unidad\n")
        for r_id, nom, cant, uni in ingredientes:
            f.write(f"{r_id},{nom},{cant},{uni}\n")

def cargar_ingredientes_csv(ruta):
    ingredientes = []
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            encabezado = f.readline().strip()
            if encabezado != "receta_id,nombre,cantidad,unidad":
                raise ArchivoInvalidoError("Encabezado inválido o faltante.")
            
            for linea in f:
                campos = linea.strip().split(',')
                if len(campos) != 4:
                    raise ArchivoInvalidoError("Cantidad de columnas incorrecta.")
                try:
                    r_id = int(campos[0])
                    cant = int(campos[2])
                except ValueError:
                    raise ArchivoInvalidoError("Error de tipo numérico en fila.")
                ingredientes.append((r_id, campos[1], cant, campos[3]))
    except FileNotFoundError:
        raise ArchivoInvalidoError("El archivo de ingredientes no existe.")
    return ingredientes

# TEORIA: Sí hace falta leer los anteriores, dado que los archivos CSV tienen registros de longitud variable en bytes y su forma de lectura es obligatoriamente secuencial, no directa.