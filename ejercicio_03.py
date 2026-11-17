from ejercicio_02 import Biblioteca


def versiones_de(biblioteca, versiones, cancion_id) -> list:
    """Devuelve las versiones derivadas de una canción."""

    # verifico que la canción existe
    biblioteca.obtener(cancion_id)

    # se buscan las versiones que salen de la canción
    directas = []
    for cid, version_de_id, tipo in versiones:
        if version_de_id == cancion_id:
            directas.append((cid, tipo))

    # si no hay versiones va devolver una lista vacía
    if not directas:
        return []

    # Ordeno las versiones por id
    directas.sort()

    resultado = []

    for cid, tipo in directas:
        cancion = biblioteca.obtener(cid)

        # primero agrego la versión encontrada
        resultado.append((cancion.titulo, tipo))

        # luego se busca si esa versión tiene otras versiones
        resultado.extend(versiones_de(biblioteca, versiones, cid))

    return resultado


# Caso base: cuando una canción no tiene versiones derivadas, la función va devolver una lista vacía [].
# Secuencia de llamadas:
# 1. Con el id 12 encuentra la canción 13 (live) y llama otra vez a la función
# 2. Con el id 13 encuentra la canción 70 (remix) y de nuevo vuelve a llamar
# 3. Con el id 70 no encuentra más versiones, por eso devuelve []
# 4. La llamada del id 13 te  devuelve [("Ji Ji Ji (Remix)", "remix")]
# 5. Finalmente, la llamada del id 12 devuelve [("Ji Ji Ji", "live"), ("Ji Ji Ji (Remix)", "remix")]