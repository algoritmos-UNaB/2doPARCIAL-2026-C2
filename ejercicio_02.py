from ejercicio_01 import Receta


class RecetaNoEncontrada(Exception):
    pass


class LibroRecetas:
    def __init__(self):
        self.recetas = []

    def agregar(self, receta):
        for i, existente in enumerate(self.recetas):
            if existente.id == receta.id:
                self.recetas[i] = receta
                return

        self.recetas.append(receta)

    def obtener(self, id):
        for receta in self.recetas:
            if receta.id == id:
                return receta

        raise RecetaNoEncontrada(
            f"No existe una receta con id {id}"
        )

    def listar(self):
        return self.recetas.copy()

    def cantidad(self):
        return len(self.recetas)


# TEORIA:
# Quien llama al método obtiene una señal explícita del error
# y puede manejar la ausencia de la receta correctamente.