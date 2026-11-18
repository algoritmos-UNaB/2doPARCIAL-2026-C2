
def busqueda_lineal(pokemones, campo, valor):
    resultado = []

    for p in pokemones:
        if campo == "nombre":
            if p.nombre == valor:
                resultado.append(p)
        elif campo == "tipo":
            if p.tipo1 == valor or p.tipo2 == valor:
                resultado.append(p)
        elif campo == "nro":
            if p.id == valor:
                resultado.append(p)
    return resultado        

def busqueda_binaria(pokemones, campo, valor):
    izq = 0
    der = len(pokemones)-1

    while izq <= der:
        medio = (izq + der) // 2
        if campo == "nombre":
            actual = pokemones[medio].nombre
        else:
            actual = pokemones[medio].id

        if actual == valor:
            return pokemones[medio]
        elif actual < valor:
            izq = medio + 1
        else: 
            der = medio - 1 
    return None        
# TEORIA
# No, porque la búsqueda binaria descarta la mitad de la lista suponiendo que está ordenada por nombre, y si está ordenada por ataque puede descartar justo la mitad donde estaba el que busco.