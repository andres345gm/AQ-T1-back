class User:
    def __init__(self, id: int, user: str, password: str):
        self.id = id
        self.user = user
        self.password = password
        self.balance = 5
        self.purchases = []

    def add_purchase(self, purchase):
        self.purchases.append(purchase)
        self.balance -= purchase.price
        return self

