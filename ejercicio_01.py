class Pokemon:
    def __init__(self, id, nombre, tipo1, tipo2, hp, ataque, defensa, velocidad, generacion):
        self.id = id
        self.nombre = nombre
        self.tipo1 = tipo1
        self.tipo2 = tipo2
        self.hp = hp
        self.ataque = ataque
        self.defensa = defensa
        self.velocidad = velocidad
        self.generacion = generacion

    def __str__(self):
        if self.tipo2 == "":
            texto = f"#{self.id} {self.nombre} ({self.tipo1})"
        else:
            texto = f"#{self.id} {self.nombre} ({self.tipo1}/{self.tipo2})"
        return texto

    def __eq__(self, otro):
        if isinstance(otro, Pokemon):
            return self.id == otro.id
        return False

# TEORIA:  La identidad es el id y el resto de los atributos el estado. La identidad no debería cambiar ya que es unica y es lo que lo define
