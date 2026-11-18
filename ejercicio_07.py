from ejercicio_02 import CancionNoEncontradaError

def busqueda_lineal(canciones, campo, valor) -> list:
    resultado = []
    for cancion in canciones:
        if campo == "titulo" and cancion.titulo == valor:
        resultado.append(cancion)
    elif campo == "artista" and cancion.artista == valor:
        resultado.append(cancion)
    elif campo == "genero" and cancion.genero == valor:
        resultado.append(cancion)
    return resultado

def busqueda_binaria_por_titulo(canciones_ordenadas, titulo):
    inicio = 0
    fin = len(canciones_ordenadas) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        actual = canciones_ordenadas[medio].titulo
        if actual == titulo:
            return canciones_ordenadas[medio]
        if actual < titulo:
            inicio = medio + 1
        else:
            fin = medio - 1
    raise CancionNoEncontradaError(
        f"No existe una canción con el título {titulo!r}")

    
# Teoria:
# La binaria pide la lista ordenada por título porque en cada paso compara con el elemento del medio
# y descartauna mitad entera; eso sólo es válido si segun el orden todo lo de un lado es menor y todo lo del otro es mayor.
# Complejidad: la binaria es 0(log n); la lineal por artista es 0(n), porque en el peor caso recorre las n canciones 
# (y siempre recorre todas para juntar todas las coincidencias).