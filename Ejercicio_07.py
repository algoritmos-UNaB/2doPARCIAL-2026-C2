from Ejercicios_02 import CancionNoEncontradaError

## Ejercicio 7 — Búsqueda (10 pts)

#Las funciones reciben una `list` de `Cancion`. Se implementan a mano.

#```python
#def busqueda_lineal(canciones, campo, valor) -> list: ...
#def busqueda_binaria_por_titulo(canciones_ordenadas, titulo) -> Cancion: ...
#```

#- `busqueda_lineal`: `campo` es `"titulo"`, `"artista"` o `"genero"`. Devuelve todas las canciones cuyo campo es igual a `valor`, en el orden original. Si no hay ninguna, lista vacía. `"Rock"` y `"Soda Stereo"` tienen que poder buscarse por este camino.
#- Binaria por `titulo`, sobre una lista ya ordenada alfabéticamente por `titulo`. Si el título no está, `CancionNoEncontradaError`. Si hubiera dos canciones con el mismo título, devuelve la primera que encuentre la búsqueda.

#**Teoría.** ¿Por qué `busqueda_binaria_por_titulo` pide la lista ordenada por título? ¿Qué complejidad tiene sobre `n` canciones, y qué complejidad tiene la búsqueda lineal por artista?

#---

def busqueda_lineal (canciones, campo, valor):
    canciones_encontradas = []
    
    if campo == "titulo":
        for cancion in canciones:
            if cancion.titulo == valor:
                canciones_encontradas.append(cancion)
        
    if campo == "artista":
        for cancion in canciones:
            if cancion.artista == valor:
                canciones_encontradas.append (cancion)

    if campo == "genero":
        for cancion in canciones:
            if cancion.genero == valor:
                canciones_encontradas.append(cancion)
    
    return canciones_encontradas


def busqueda_binaria_por_titulo (canciones_ordenadas, titulo):
    posicion_inicial = 0
    posicion_final = len (canciones_ordenadas) - 1

    while posicion_inicial <= posicion_final:
        posicion_del_medio =  (posicion_inicial + posicion_final) // 2
        cancion_del_medio = canciones_ordenadas [posicion_del_medio]

        if cancion_del_medio.titulo == titulo:
            return cancion_del_medio
        
        va_antes_abc =  titulo < cancion_del_medio.titulo
        if va_antes_abc:
            posicion_final = posicion_del_medio - 1

        va_despues_abc = titulo > cancion_del_medio.titulo
        if va_despues_abc:
            posicion_inicial = posicion_del_medio + 1

    raise CancionNoEncontradaError("No se encontro la cancion")


    #RTA Teoria: Pide la lista ordenada por descarta de a mitades comparando alfabeticamente, La busqueda binaria es O(log n) y la lineal es O(n)
                    