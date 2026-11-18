"""Ejercicio 1 — Entidad del catálogo: la clase Receta."""


class Receta:
    """Una receta del catálogo.

    El id es la identidad: se guarda en un atributo "privado" (_id) y se expone
    con una property SIN setter, así no se puede cambiar después de construir
    el objeto. El resto de los atributos es estado y sí puede cambiar.
    """

    def __init__(self, id, nombre, tiempo_min, dificultad, categoria):
        self._id = id
        self.nombre = nombre
        self.tiempo_min = tiempo_min
        self.dificultad = dificultad
        self.categoria = categoria

    @property
    def id(self):
        return self._id

    def __str__(self):
        return f"#{self._id} {self.nombre} — {self.tiempo_min} min, {self.dificultad}, {self.categoria}"

    def __repr__(self):
        return f"Receta({self._id}, {self.nombre!r})"

    def __eq__(self, otro):
        # Dos recetas son "la misma" si tienen el mismo id, aunque el resto difiera.
        if not isinstance(otro, Receta):
            return False
        return self._id == otro._id

    def __hash__(self):
        
        return hash(self._id)


# TEORIA
# La identidad es el id; nombre, tiempo_min, dificultad y categoria son estado.
# No: la identidad no debería poder cambiar después de construido el objeto,
# porque __eq__ (y cualquier búsqueda o índice por id) depende de que el id
# sea siempre el mismo; por eso id es una property sin setter.


if __name__ == "__main__":
    asado = Receta(9, "Asado", 180, "media", "principal")
    print(asado)                                                        
    print(asado == Receta(9, "Otro nombre", 1, "alta", "postre"))       
        print(asado == Receta(10, "Asado", 180, "media", "principal"))     
    print(asado == "Asado")                                             
