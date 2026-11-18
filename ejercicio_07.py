def busqueda_lineal(canciones, campo, valor) -> list:
    coincidiencias = []

    for cancion in canciones:
        if campo == "titulo" and cancion.titulo = valor:
            coincidiencias.append(cancion)
        elif campo == "artista" and cancion.artista == valor:
            coincidiencias.append(cancion)
        elif campo == "genero" and cancion.genero == valor:
            coincidiencias.append(cancion)
    
    return coincidiencias

def busqueda_binaria_por_titulo(canciones_ordenadas, titulo) -> Cancion:
    pos_inicio = 0
    pos_fin = len(canciones_ordenadas) - 1 

    while pos_inicial <= pos_final:
        pos_media = (pos_inicio + pos_fin) // 2
        cancion_media = canciones_ordenadas[pos_media]

        if cancion_media.titulo == titulo:
            return cancion_media
        elif cancion_media.titulo < titulo:
            pos_inicio = pos_media + 1
        else:
            pos_fin = pos_media - 1
    raise CancionNoEncontradaError("No se encontró una canción con el título " + titulo)

    # La búsqueda binaria necesita la lista ordenada por título para saber qué mitad descartar después de las comparaciones. Su complejidad es O(log n) y la complejidad 
    # de la búsqueda lineal es O(n) porque recorrer todas las canciones.