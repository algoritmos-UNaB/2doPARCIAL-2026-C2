class Pokemon:
    def _init_(
        self,
        id: int,
        nombre: str,
        tipo1: str,
        tipo2: str,
        hp: int,
        ataque: int,
        defensa: int,
        velocidad: int,
        generacion: int,
    ):
        self.id = id
        self.nombre = nombre
        self.tipo1 = tipo1
        self.tipo2 = tipo2
        self.hp = hp
        self.ataque = ataque
        self.defensa = defensa
        self.velocidad = velocidad
        self.generacion = generacion

    def _str_(self) -> str:
        if self.tipo2:
            return f"#{self.id} {self.nombre} ({self.tipo1}/{self.tipo2})"
        return f"#{self.id} {self.nombre} ({self.tipo1})"

    def _eq_(self, other: object) -> bool:
        if not isinstance(other, Pokemon):
            return False
        return self.id == other.id

         
        # TEORÍA: La identidad del Pokémon es el atributo 'id' y su estado está compuesto por el resto de sus atributos (nombre, tipos y estadísticas); no, la identidad no debería poder cambiar después de construido el objeto porque dejaría de representar a la misma entidad dentro del sistema.
       






































