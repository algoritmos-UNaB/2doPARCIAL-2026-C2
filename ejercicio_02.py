"""Ejercicio 2 — Catálogo: LibroRecetas y la excepción RecetaNoEncontrada.

En este ejercicio el libro guarda las recetas en un list de Python (lo permite
la consigna). En ejercicio_04.py hay una versión de LibroRecetas con la misma
interfaz que guarda las recetas en la ListaEnlazada propia; esa es la que usan
los ejercicios 9 y 10.
"""

from ejercicio_01 import Receta


class RecetaNoEncontrada(Exception):
    """No hay ninguna receta con ese id (o ese día del menú no tiene receta)."""


class LibroRecetas:
    def __init__(self):
        self._recetas = []

    def agregar(self, receta):
        """Agrega la receta al final. Si ya había una con ese id, la reemplaza en su lugar."""
        for i in range(len(self._recetas)):
            if self._recetas[i].id == receta.id:
                self._recetas[i] = receta
                return
        self._recetas.append(receta)

    def obtener(self, id):
        for receta in self._recetas:
            if receta.id == id:
                return receta
        raise RecetaNoEncontrada(f"No hay ninguna receta con id {id}.")

    def listar(self):
        """Las recetas en el orden en que quedaron cargadas (una copia: quien
        la recibe puede ordenarla sin desordenar el libro)."""
        copia = []
        for receta in self._recetas:
            copia.append(receta)
        return copia

    def cantidad(self):
        return len(self._recetas)



RECETAS_EXAMEN = (
    (1, "Chimichurri", 15, "baja", "salsa"),
    (2, "Salsa criolla", 20, "baja", "salsa"),
    (3, "Sofrito", 25, "baja", "base"),
    (5, "Masa de empanadas", 90, "media", "base"),
    (9, "Asado", 180, "media", "principal"),
    (10, "Empanadas de carne", 150, "media", "principal"),
    (12, "Locro", 150, "alta", "principal"),
)


def libro_examen(libro=None):
    """Carga las 7 recetas del examen en `libro` (o en un LibroRecetas nuevo) y lo devuelve."""
    if libro is None:
        libro = LibroRecetas()
    for id, nombre, tiempo_min, dificultad, categoria in RECETAS_EXAMEN:
        libro.agregar(Receta(id, nombre, tiempo_min, dificultad, categoria))
    return libro


# TEORIA
# Quien llama gana que el error no pasa inadvertido: no tiene que acordarse de
# comparar con None (si se olvida, el programa falla más adelante con un
# AttributeError confuso), y puede manejar el caso con un try/except
# RecetaNoEncontrada en el lugar que corresponda.


if __name__ == "__main__":
    libro = libro_examen()
    print(libro.cantidad(), "recetas")
    print(libro.obtener(9))
    libro.agregar(Receta(9, "Asado al asador", 240, "alta", "principal"))   # mismo id: reemplaza
    print(libro.obtener(9), "| siguen siendo", libro.cantidad())
    try:
        libro.obtener(99)
    except RecetaNoEncontrada as error:
        print("RecetaNoEncontrada:", error)
