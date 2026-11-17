class Receta:
    def _init_(self, id, nombre, tiempo_min, dificultad, categoria):
        self.id = id
        self.nombre = nombre
        self.tiempo_min = tiempo_min
        self.dificultad = dificultad
        self.categoria = categoria

    def _str_(self):
        return f"#{self.id} {self.nombre} — {self.tiempo_min} min, {self.dificultad}, {self.categoria}"

    def _eq_(self, other):
        if not isinstance(other, Receta):
            return False
        return self.id == other.id

# TEORIA: El atributo 'id' es la identidad y el resto de los atributos forman el estado; la identidad no debería cambiar después de construido el objeto.