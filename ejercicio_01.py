class Pokemon:
    def _init_(self, id, nombre, tipo1, tipo2, hp, ataque, defensa, velocidad, generacion):
        self.id = int(id)
        self.nombre = nombre
        self.tipo1 = tipo1
        self.tipo2 = tipo2
        self.hp = int(hp)
        self.ataque = int(ataque)
        self.defensa = int(defensa)
        self.velocidad = int(velocidad)
        self.generacion = int(generacion)

    def _str_(self):
        if self.tipo2:
            return f"#{self.id} {self.nombre} ({self.tipo1}/{self.tipo2})"
        return f"#{self.id} {self.nombre} ({self.tipo1})"

    def _eq_(self, otro):
        if isinstance(otro, Pokemon):
            return self.id == otro.id
        return False

# TEORIA
# La identidad del Pokémon que es su atributo  es el 'id', el resto de  los atributos definen su estado. 
# No,la identidad no debería poder cambiar despues de construido el objeto porque es lo que individualiza a ese objeto en su existencia.