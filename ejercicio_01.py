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
            return f"#{self.id} {self.nombre} ({self.tipo1})"
        else:
            return f"#{self.id} {self.nombre} ({self.tipo1}/{self.tipo2})"

    def __eq__(self, value):
        return isinstance(value, Pokemon) and self.id == value.id 

    # TEORIA
    # Identidad es id y estado nombre, tipo1, tipo2, hp, ataque, defensa, velocidad, generacion.
    # No, nunca deberia cambiar la identidad por que es la referencia de caracter unico que tiene el objeto, si cambiara se perderia el dato