from datetime import datetime

class Purchase:
    def __init__(self, id: int, id_pokemon : int, date: str, price: int, id_user: int):
        self.id = id
        self.id_pokemon = id_pokemon
        self.date = date
        self.price = price
        self.id_user = id_user

