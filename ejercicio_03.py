from ejercicio_02 import Biblioteca, CancionNoEncontradaError

def versiones_de(biblioteca, versiones, cancion_id) -> list:
    """Lista de (titulo, tipo) de todo lo derivado, sin incluir la canción original."""
    biblioteca.obtener(cancion_id)  # lanza CancionNoEncontradaError si no existe

    directas = sorted(
        [v for v in versiones if v[1] == cancion_id],
        key=lambda v: v[0],
    )

    resultado = []  # caso base: si no hay directas, queda vacía
    for version_id, _, tipo in directas:
        cancion = biblioteca.obtener(version_id)
        resultado.append((cancion.titulo, tipo))  # primero la directa
        resultado.extend(versiones_de(biblioteca, versiones, version_id))  # luego lo que cuelga
    return resultado

# Teoria:
# Caso base: nadie es versión de la canción recibida -> devuelve [].
# Secuencia de llamadas: versiones_de(..., 12): directas = [13]. Agrega ("Ji Ji Ji", "live") y llama a
# versiones_de(..., 13): directas = [70]. Agrega ("Ji Ji Ji (Remix)", "remix") y llama a
# versiones_de(..., 70): directas = [] -> caso base, devuelve [].
# Al volver: versiones_de(70) devuelve []
# versiones_de(13) devuelve [("Ji Ji Ji (Remix)", "remix")]
# versiones_de(12) devuelve [("Ji Ji Ji", "live"), ("Ji Ji Ji (Remix)", "remix")]