## Ejercicio 3 — Versiones (12 pts)

def versiones_de(biblioteca, versiones, cancion_id):
    """Lista de (titulo, tipo) de todo lo derivado, sin incluir la original."""
    biblioteca.obtener(cancion_id)  # valida que exista; lanza si no

    directas = [
        (cid, tipo) for (cid, padre, tipo) in versiones if padre == cancion_id
    ]
    directas.sort(key=lambda par: par[0])

    resultado = []
    for cid, tipo in directas:
        titulo = biblioteca.obtener(cid).titulo
        resultado.append((titulo, tipo))
        resultado.extend(versiones_de(biblioteca, versiones, cid))
    return resultado
