## Ejercicio 3 — Versiones (12 pts)

#Implementar una función recursiva que lista las versiones derivadas de una canción (cover, live, remix), también las versiones de esas versiones:

#```python
#def versiones_de(biblioteca, versiones, cancion_id) -> list:
#    """Lista de (titulo, tipo) de todo lo derivado, sin incluir la canción original."""
#```

#`versiones` es una lista de tuplas `(cancion_id, version_de_id, tipo)`.

#- Caso base: nadie es versión de esta canción. El resultado es la lista vacía.
#- Si hay varias versiones directas, recorrerlas de menor a mayor `cancion_id`.
#- Cada llamada recursiva trae lo derivado de esa versión. El resultado es preorden: primero la versión directa `(titulo, tipo)`, después lo que cuelga de ella.
#- Si `cancion_id` no está en la biblioteca, lanzar `CancionNoEncontradaError`.

#Con los datos de prueba, Jijiji (12) tiene el vivo Ji Ji Ji (13) y, debajo, el remix (70). Gracias a la Vida de Violeta Parra (61) tiene el cover de Mercedes Sosa (16).

#**Teoría.** Escribir el caso base y la secuencia de llamadas de `versiones_de(..., 12)`, indicando qué lista devuelve cada llamada al volver.

#---
def versiones_de(biblioteca, versiones, cancion_id):
    biblioteca.obtener(cancion_id)
    canciones_directas = []
    for id_cancion, version_de_id, tipo in versiones:
        if version_de_id== cancion_id:
            canciones_directas.append((id_cancion,tipo))
    if not canciones_directas: #<------Caso base
        return []
    canciones_directas.sort()
    resultado=[]
    for id_version, tipo in canciones_directas:
        cancion= biblioteca.obtener(id_version)
        resultado.append((cancion.titulo,tipo))
        resultado+= versiones_de(biblioteca,versiones,id_version)
    return resultado
#El for recorre las id de las canciones, y las compara con la version_de_id, las carga en versiones_directas hasta que no se encuentran mas versiones . De  no haer se devueve una lista vacia. 