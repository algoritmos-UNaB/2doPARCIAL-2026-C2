import struct
from ejercicio_01 import Receta
from ejercicio_02 import LibroRecetas
from ejercicio_09 import ArchivoInvalidoError

ENCABEZADO_FMT = "<4scI" # 9 bytes
REGISTRO_FMT = "<I32sH8s16s" # 62 bytes

def formatear_str(texto, ancho):
    return texto.encode('utf-8').ljust(ancho, b'\0')[:ancho]

def leer_str(b_texto):
    return b_texto.decode('utf-8').rstrip('\0')

def guardar_binario(ruta, libro):
    recetas = libro.listar()
    with open(ruta, "wb") as f:
        f.write(struct.pack(ENCABEZADO_FMT, b"AYED", b"R", len(recetas)))
        for r in recetas:
            f.write(struct.pack(REGISTRO_FMT, r.id, 
                                formatear_str(r.nombre, 32), 
                                r.tiempo_min, 
                                formatear_str(r.dificultad, 8), 
                                formatear_str(r.categoria, 16)))

def cargar_binario(ruta):
    libro = LibroRecetas()
    try:
        with open(ruta, "rb") as f:
            buf_enc = f.read(9)
            if len(buf_enc) < 9:
                raise ArchivoInvalidoError("Archivo trunco.")
            magia, tema, cantidad = struct.unpack(ENCABEZADO_FMT, buf_enc)
            if magia != b"AYED":
                raise ArchivoInvalidoError("Firma mágica incorrecta.")
            
            for _ in range(cantidad):
                buf_reg = f.read(62)
                if len(buf_reg) < 62:
                    raise ArchivoInvalidoError("Registro incompleto.")
                r_id, b_nom, t, b_dif, b_cat = struct.unpack(REGISTRO_FMT, buf_reg)
                libro.agregar(Receta(r_id, leer_str(b_nom), t, leer_str(b_dif), leer_str(b_cat)))
    except FileNotFoundError:
        raise ArchivoInvalidoError("El archivo binario no existe.")
    return libro

def actualizar_registro(ruta, posicion, receta):
    try:
        with open(ruta, "r+b") as f:
            buf_enc = f.read(9)
            if len(buf_enc) < 9:
                raise ArchivoInvalidoError("Archivo trunco.")
            magia, tema, cantidad = struct.unpack(ENCABEZADO_FMT, buf_enc)
            
            if magia != b"AYED":
                raise ArchivoInvalidoError("Firma mágica incorrecta.")
            if posicion < 0 or posicion >= cantidad:
                raise ArchivoInvalidoError("Posición del registro fuera de rango.")
            
            offset = 9 + (posicion * 62)
            f.seek(offset)
            f.write(struct.pack(REGISTRO_FMT, receta.id, 
                                formatear_str(receta.nombre, 32), 
                                receta.tiempo_min, 
                                formatear_str(receta.dificultad, 8), 
                                formatear_str(receta.categoria, 16)))
    except FileNotFoundError:
        raise ArchivoInvalidoError("El archivo binario no existe.")

# TEORIA: Al tener un layout de longitud estrictamente fija, se sabe que cada registro pesa exactamente 62 bytes y el encabezado 9, calculando el byte inicial con la fórmula (9 + posición * 62).