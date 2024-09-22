class User:
    def __init__(self, id: int, user: str, password: str):
        self.id = id
        self.user = user
        self.password = password
        self.balance = 5
        self.pokemon_inventory = []

    def __init__(self, user: str, password: str):
        self.id = None
        self.user = user
        self.password = password
        self.balance = 5
        self.pokemon_inventory = []

