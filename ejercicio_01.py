class Pokemon:

    def __init__(self, id, nombre, tipo1, tipo2, hp, ataque, defensa, velocidad, generacion):
        self._id = id
        self.nombre = nombre
        self.tipo1 = tipo1
        self.tipo2 = tipo2
        self.hp = hp
        self.ataque = ataque
        self.defensa = defensa
        self.velocidad = velocidad
        self.generacion = generacion

    @property
    def id(self):
        return self._id

    def __str__(self):
        if self.tipo2 == "":
            return f"#{self.id} {self.nombre} ({self.tipo1})"
        return f"#{self.id} {self.nombre} ({self.tipo1}/{self.tipo2})"

    def __eq__(self, otro):
        if not isinstance(otro, Pokemon):
            return False
        return self.id == otro.id

    def __hash__(self):
        return hash(self.id)


# TEORIA
# La identidad es el id, lo demás (nombre, tipos, stats y generación) es el estado.
# No, el id no debería poder cambiar una vez creado el Pokémon.