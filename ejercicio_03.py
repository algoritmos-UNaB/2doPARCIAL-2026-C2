def versiones_de(biblioteca, versiones, cancion_id) -> list:
    biblioteca.obtener(cancion_id)

    directas = []

    for version in versiones:
        if version[1] == cancion_id:
            directas.append(version)

    if len(directas) == 0:
        return []

    resultado = []

    while len(directas) > 0:
        menor = directas[0]

        for version in directas:
            if version[0] < menor[0]:
                menor = version

        directas.remove(menor)

        cancion = biblioteca.obtener(menor[0])
        resultado.append((cancion.titulo, menor[2]))

        derivadas = versiones_de(biblioteca, versiones, menor[0])
        resultado.extend(derivadas)

    return resultado

# El caso base ocurre cuando la canción encontrada no tiene versiones directas, devolviendo []

# Secuencia de llamadas:

# versiones_de(12)
    # versiones_de(13)
        # versiones_de(70)

# y cada llamada devuelve lo siguiente:

# 70: [] porque no tiene versiones
# 13: [("Ji ji ji (Remix)", "remix")]
# 12: [("Ji ji ji", "live"), "Ji ji ji (Remix)", "remix"]