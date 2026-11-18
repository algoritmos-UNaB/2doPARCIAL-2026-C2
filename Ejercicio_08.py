## Ejercicio 8 — Ordenamiento (10 pts)

#Ordenar in-place una `list` de `Cancion` y devolver esa misma lista. Dos algoritmos distintos, escritos a mano:

#```python
#def ordenar_por_anio_seleccion(canciones) -> list:
#    """Selección. Año de mayor a menor."""

#def ordenar_por_duracion_insercion(canciones) -> list:
#    """Inserción. duracion_seg de menor a mayor."""
#```

#Con los datos de prueba, el remix (2020) queda antes que el unplugged (1996) al ordenar por año, y De Música Ligera (213 s) queda antes que Jijiji (316 s) al ordenar por duración.

#**Teoría.** Dar la complejidad de peor caso de cada algoritmo. ¿Cuál de los dos conserva el orden relativo de dos canciones con la misma clave?

#---


def ordenar_por_anio_seleccion (canciones):
    cantidad = len (canciones)

    for pos_actual in range (cantidad):
        pos_mayor = pos_actual

        for pos_siguiente in range (pos_actual + 1, cantidad):
            cancion_siguiente = canciones [pos_siguiente]
            cancion_mayor = canciones [pos_mayor]

            if cancion_siguiente.anio > cancion_mayor.anio:
                pos_mayor = pos_siguiente
            
        aux = canciones [pos_actual]
        canciones [pos_actual] = canciones[pos_mayor]
        canciones [pos_mayor] = aux

        return canciones


def ordenar_por_duracion_insercion (canciones):
    cantidad = len (canciones)

    for i in range(1, cantidad):
        pos = i

        while pos > 0:
            cancion_izquierda = canciones[pos - 1]
            cancion_actual = canciones[pos]

            if cancion_actual.duracion_seg < cancion_izquierda.duracion_seg:
                canciones [pos - 1] = cancion_actual
                canciones [pos] = cancion_izquierda
                pos = pos - 1
            else:
                break

    return canciones

    