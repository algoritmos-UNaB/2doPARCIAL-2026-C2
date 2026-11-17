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
        tipos = self.tipo1

        if self.tipo2 != "":
            tipos += "/" + self.tipo2

        return f"#{self.id} {self.nombre} ({tipos})"

    def __eq__(self, otro):
        return isinstance(otro, Pokemon) and self.id == otro.id

# Respuesta a la pregunta: El ID representa la identidad y los demas atributos representan estados del pokémon, no, la identidad no deberia cambiar despues de construir el objeto.