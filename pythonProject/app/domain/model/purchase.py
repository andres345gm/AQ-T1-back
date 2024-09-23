from datetime import datetime

class Purchase:
    def __init__(self, id: int, id_pokemon : int, date: datetime, price: int):
        self.id = id
        self.id_pokemon = id_pokemon
        self.date = date
        self.price = price

