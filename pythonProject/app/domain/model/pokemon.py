class Pokemon:
    def __init__(self, id: int, name: str, height: int, weight: int, stats: dict, image: str):
        self.id = id
        self.name = name
        self.height = height
        self.weight = weight
        self.stats = stats
        self.image = image  # Nueva propiedad para la imagen
