from datetime import datetime


class Purchase:
    def __init__(self, id: int, id_pokemon: int, date: str, price: int, id_user: int):
        self.id_ = id
        self.id_pokemon = id_pokemon
        self.date = date
        self.price = price
        self.id_user = id_user

    def to_dict(self):
        return {
            "id": self.id_,
            "id_pokemon": self.id_pokemon,
            "date": self.date,
            "price": self.price,
            "id_user": self.id_user
        }

