def ordenar_seleccion(pokemones, campo, descendente):
    for i in range(len(pokemones)):
        posicion = i

        for j in range(i + 1, len(pokemones)):
            if campo == "ataque":
                valor_actual = pokemones[j].ataque
                valor_menor = pokemones[posicion].ataque

            elif campo == "velocidad":
                valor_actual = pokemones[j].velocidad
                valor_menor = pokemones[posicion].velocidad

            else:
                valor_actual = pokemones[j].id
                valor_menor = pokemones[posicion].id

            if descendente:
                if valor_actual > valor_menor:
                    posicion = j
            else:
                if valor_actual < valor_menor:
                    posicion = j

        auxiliar = pokemones[i]
        pokemones[i] = pokemones[posicion]
        pokemones[posicion] = auxiliar

    return pokemones


    def ordenar_insercion(pokemones, campo, descendente):

        for i in range(1, len(pokemones)):

            actual = pokemones[i]
            j = i - 1

            if campo == "ataque":
                valor_actual = actual.ataque
            elif campo == "velocidad":
                valor_actual = actual.velocidad
            else:
                valor_actual = actual.id

            while j >= 0:

                if campo == "ataque":
                    valor_anterior = pokemones[j].ataque
                elif campo == "velocidad":
                    valor_anterior = pokemones[j].velocidad
                else:
                    valor_anterior = pokemones[j].id

                if descendente:
                    if valor_anterior < valor_actual:
                        pokemones[j + 1] = pokemones[j]
                        j -= 1
                    else:
                        break

                else:
                    if valor_anterior > valor_actual:
                        pokemones[j + 1] = pokemones[j]
                        j -= 1
                    else:
                        break

            pokemones[j + 1] = actual

        return pokemones
# TEORIA
# Inserción es estable. Estable significa que los elementos con el mismo valor mantienen el orden que tenían antes de ordenar.