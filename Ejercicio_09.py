from Ejercicio_01 import Cancion
from Ejercicio_02 import Biblioteca


## Ejercicio 9 — `canciones.csv` (9 pts)

#Persistir la biblioteca en CSV, UTF-8, separador coma, con encabezado:

#```text
#id,titulo,artista,album,genero,anio,duracion_seg
#```

#```python
#def guardar_canciones_csv(ruta, biblioteca): ...
#def cargar_canciones_csv(ruta) -> Biblioteca: ...
#```

#`cargar_canciones_csv` rearma objetos `Cancion`. Lanza `ArchivoInvalidoError` si el archivo no existe, si el encabezado no es el pedido o si una fila tiene menos columnas.

#Las versiones quedan fuera de este archivo.

#**Teoría.** Para leer la canción de la fila 50, ¿hay que recorrer las filas anteriores? Explicar en una oración por qué, a partir de cómo está guardado el CSV.


class ArchivoInvalidoError (Exception):
    pass

def guardar_canciones_csv (ruta, biblioteca):
    archivo = open (ruta, "w", encoding="utf-8")
    archivo.write ("id,titulo,artista,album,genero,anio,duracion_seg\n")

    for cancion in biblioteca:
        linea = (
            str(cancion.id) + ","
            + cancion.titulo + ","
            + cancion.artista + ","
            + cancion.album + ","
            + cancion.genero + ","
            + str(cancion.anio) + ","
            + str(cancion.duracion_seg) + "\n"
        )
        archivo.write(linea)

    archivo.close()

def cargar_canciones_csv (ruta)
    try:
        archivo = open (ruta, "r", encoding="utf-8")
        lineas = archivo.readlines ()
        archivo.close ()
    except FileNotFoundError:
        raise ArchivoInvalidoError("El archivo no existe!")

    if len(lineas) == 0:
        raise ArchivoInvalidoError("El archivo esta vacio!")

    encabezado = lineas [0].strip ()
    if encabezado != "id,titulo,artista,album,genero,anio,duracion_seg":
        raise ArchivoInvalidoError("El encabezado no es valido!")

    biblioteca = Biblioteca ()
    primera_linea = True

    for linea in lineas:
        if primera_linea == True:
            primera_linea = False
        else:
            linea_limpia = linea.strip ()

            if linea_limpia != "":
                datos = linea_limpia.split(",")

                if len(datos) < 7:
                    raise ArchivoInvalidoError("Una fila tiene menos columnas!")

                id_cancion = int(datos[0])
                titulo = datos [1]
                artista = datos [2]
                album = datos [3]
                genero = datos [4]
                anio = int(datos [5])
                duracion = int(datos [6])

                cancion = Cancion (id_cancion, titulo, artista, album, genero, anio, duracion)
                biblioteca.agregar (cancion)

    return biblioteca

    #RTA Teorica: Si, porque en un CSV las filas tienen distinto largo