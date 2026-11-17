from ejercicio_01 import Pokemon


def ordenar_seleccion(pokemones, campo, ascendente=True):
    n = len(pokemones)

    for i in range(n - 1):
        posicion_menor = i

        for j in range(i + 1, n):
            if campo == "ataque":
                valor_j = pokemones[j].ataque
                valor_menor = pokemones[posicion_menor].ataque
            elif campo == "velocidad":
                valor_j = pokemones[j].velocidad
                valor_menor = pokemones[posicion_menor].velocidad
            elif campo == "nro":
                valor_j = pokemones[j].id
                valor_menor = pokemones[posicion_menor].id
            else:
                raise ValueError("Campo de ordenamiento inválido")

            if ascendente:
                if valor_j < valor_menor:
                    posicion_menor = j
            else:
                if valor_j > valor_menor:
                    posicion_menor = j

        pokemones[i], pokemones[posicion_menor] = (
            pokemones[posicion_menor],
            pokemones[i]
        )

    return pokemones


def ordenar_insercion(pokemones, campo, ascendente=True):
    for i in range(1, len(pokemones)):
        actual = pokemones[i]

        if campo == "ataque":
            valor_actual = actual.ataque
        elif campo == "velocidad":
            valor_actual = actual.velocidad
        elif campo == "nro":
            valor_actual = actual.id
        else:
            raise ValueError("Campo de ordenamiento inválido")

        j = i - 1

        while j >= 0:
            if campo == "ataque":
                valor_anterior = pokemones[j].ataque
            elif campo == "velocidad":
                valor_anterior = pokemones[j].velocidad
            else:
                valor_anterior = pokemones[j].id

            if ascendente:
                if valor_anterior > valor_actual:
                    pokemones[j + 1] = pokemones[j]
                    j -= 1
                else:
                    break
            else:
                if valor_anterior < valor_actual:
                    pokemones[j + 1] = pokemones[j]
                    j -= 1
                else:
                    break

        pokemones[j + 1] = actual

    return pokemones


#Teoria
#El algoritmo de insercion es estable porque mantiene el orden original de
# los elementos que tienen el mismo valor