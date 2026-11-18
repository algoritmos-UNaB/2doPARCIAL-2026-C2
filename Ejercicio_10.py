import struct
from Ejercicio_01 import Cancion
from Ejercicio_02 import Biblioteca
from Ejercicio_09 import ArchivoInvalidoError

## Ejercicio 10 — Registros binarios (9 pts)

#Archivo binario de registros de longitud fija, con `struct` y formato estándar (`=`, sin padding de alineación).

#Encabezado, 9 bytes: magia `4s` con `b"AYED"`, tema `1s` con `b"M"`, cantidad `I`.

#Registro, 144 bytes:

#| Campo | Formato |
#| --- | --- |
#| id | `I` |
#| titulo | `40s` |
#| artista | `40s` |
#| album | `40s` |
#| genero | `16s` |
#| anio | `H` |
#| duracion_seg | `H` |

#Las cadenas van en UTF-8, recortadas al ancho y completadas con `\0`. Al leer, se corta en el primer `\0`. El artista más largo de los datos de prueba entra en 40 bytes.

#```python
#def guardar_binario(ruta, biblioteca): ...
#def cargar_binario(ruta) -> Biblioteca: ...
#def actualizar_registro(ruta, posicion, cancion): ...
#```

#`posicion` es 0-based. `actualizar_registro` escribe un solo registro en su lugar (`seek`) y no reescribe el resto del archivo. Lanza `ArchivoInvalidoError` si la magia no es `AYED`, si el tema no es `M`, si el archivo no cierra justo en `9 + cantidad * 144` bytes, o si `posicion` está fuera de rango.

#**Teoría.** Escribir la fórmula del byte donde empieza el registro de posición `k`. Usar el tamaño del encabezado y el tamaño del registro.

def guardar_binario (ruta, biblioteca):
    canciones = []
    for cancion in biblioteca:
        canciones.append (cancion)

    cantidad = len (canciones)
    archivo = open (ruta, "wb")

    encabezado = struct.pack ("=4s1sI", b"AYED", b"M", cantidad)
    archivo.write (encabezado)

    for c in canciones:
        titulo = c.titulo.encode ("utf-8") [:40]
        artista = c.artista.encode ("utf-8") [:40]
        album = c.album.encode ("utf-8") [:40]
        genero = c.genero.encode ("utf-8") [:16]

        reg = struct.pack ("=I40s40s40s16sHH", c.id, titulo, artista, album, genero, c.anio, c.duracion_seg)
        archivo.write (reg)

    archivo.close ()


def cargar_binario (ruta):
    try:
        archivo = open (ruta, "rb")
    except FileNotFoundError:
        raise ArchivoInvalidoError ("No exite el archivo!")

    encabezado = archivo.read (9)
    if len(encabezado) < 9:
        archivo.close ()
        raise ArchivoInvalidoError ("Archivo invalido!")

    magia, tema, cantidad = struct.unpack ("=4s1sI", encabezado)

    if magia != b"AYED" or tema != b"M":
        archivo.close ()
        raise ArchivoInvalidoError ("Encabezado invalido!")

    resto = archivo.read ()
    if len (resto) != cantidad * 144:
        archivo.close()
        raise ArchivoInvalidoError ("Tamaño incorrecto!")

    archivo.seek(9)
    biblioteca = Biblioteca ()

    for i in range (cantidad)
        reg = archivo.read (144)
        datos = struct.unpack ("=I40s40s40s16sHH", reg)

        id_cancion = datos [0]
        titulo = datos [1].split(b"\x00")[0].decode ("utf-8")
        artista = datos [2].split(b"\x00")[0].decode ("utf-8")
        album = datos [3].split(b"\x00")[0].decode ("utf-8")
        genero = datos [4].split(b"\x00")[0].decode ("utf-8")
        anio = datos [5]
        duracion = datos [6]

        cancion = Cancion (id_cancion, titulo, artista, album, genero, anio, duracion)
        biblioteca.agregar (cancion)

    archivo.close ()
    return biblioteca


def actualizar_registro (ruta, posicion, cancion):
    try:
        archivo = open (ruta, "r+b")
    except FileNotFoundError:
        raise ArchivoInvalidoError ("No existe el archivo!")

    encabezado = archivo.read (9)
    if len (encabezado) < 9:
        archivo.close ()
        raise ArchivoInvalidoError ("Archivo invlido!")

    magia, tema, cantidad = struct.unpack("=4s1sI", encabezado)

    if magia != b"AYED" or tema != b"M":
        archivo.close ()
        raise ArchivoInvalidoError ("Encabezado invalido!")

    resto = archivo.read ()
    if len (resto) != cantidad * 144:
        archivo.close ()
        raise ArchivoInvalidoError ("Tamano incorrecto!")

    if posicion < 0 or posicion >= cantidad:
        archivo.close ()
        raise ArchivoInvalidoError ("Posicion fuera de rango!")

    byte_inicio = 9 + posicion * 144
    archivo.seek (byte_inicio)

    titulo = cancion.titulo.encode ("utf-8")[:40]
    artista = cancion.artista.encode ("utf-8")[:40]
    album = cancion.album.encode ("utf-8")[:40]
    genero = cancion.genero.encode ("utf-8")[:16]

    reg = struct.pack("=I40s40s40s16sHH", cancion.id, titulo, artista, album, genero, cancion.anio, cancion.duracion_seg)
    archivo.write (reg)
    archivo.close ()