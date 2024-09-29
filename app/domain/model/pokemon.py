class Pokemon:
    def __init__(self, id: int, name: str, height: int, weight: int,hp:int, attack: int, image: str):
        self.id_ = id
        self.name = name
        self.height = height
        self.weight = weight
        self.hp = hp
        self.attack = attack
        self.image = image  # Nueva propiedad para la imagen
