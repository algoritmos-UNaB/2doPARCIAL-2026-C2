""" ejercicio 3. Recorrido de versiones en preorden"""

def versiones_de(biblioteca, versiones, cancion_id) -> list:
    """Devuelve los pares (titulo, tipo) de las versiones y sus derivadas."""
    biblioteca.obtener(cancion_id)
    directas = []
    for version in versiones:
        if version[1] == cancion_id:
            directas.append(version)

    # Caso base. Esta canción no tiene versiones derivadas.
    if not directas:
        return []

    # Inserción por id para recorrer las versiones directas de menor a mayor.
    for i in range(1, len(directas)):
        actual = directas[i]
        j = i - 1
        while j >= 0 and directas[j][0] > actual[0]:
            directas[j + 1] = directas[j]
            j -= 1
        directas[j + 1] = actual

    resultado = []
    for id_version, version_de_id, tipo in directas:
        cancion = biblioteca.obtener(id_version)
        resultado.append((cancion.titulo, tipo))
        resultado.extend(versiones_de(biblioteca, versiones, id_version))
    return resultado



#El caso base pasa cuando nunguna tupla tiene  como version_de_id el id actual.
#devuelve []
#la secuencia de llamada devuelve,
#versiones_de(..., 12) -> versiones_de(..., 13) -> versiones_de(..., 70).
#Al volver, la llamada para 70 devuelve [].
#La llamada para 13 devuelv [(" Ji Ji Ji (remix)", "remix")].
#La llamada para 12 devuelve 
#[("Ji Ji Ji", "live"), ("Ji Ji Ji (Remix)", "remix")].
