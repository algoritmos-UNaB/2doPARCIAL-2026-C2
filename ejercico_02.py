
class RecetaNoEncontrada(Exception):
    pass

class LibroRecetas:
    def _init_(self):
        self.recetas = []

    def agregar(self, receta):
        for i, r in enumerate(self.recetas):
            if r.id == receta.id:
                self.recetas[i] = receta
                return
        self.recetas.append(receta)

    def obtener(self, id):
        for r in self.recetas:
            if r.id == id:
                return r
        raise RecetaNoEncontrada(f"No se encontró la receta con id {id}")

    def listar(self):
        return list(self.recetas)

    def cantidad(self):
        return len(self.recetas)

# TEORIA: Quien llama al método gana seguridad operativa, porque se ve forzado a manejar la excepción si la receta no existe, en lugar de arrastrar un error silencioso por operar con un None .