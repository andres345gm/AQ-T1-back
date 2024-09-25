class User:
    def __init__(self, id: int, user: str, password: str, balance: int = 5, purchases: list = []):
        self.id_ = id
        self.user = user
        self.password = password
        self.balance = balance
        self.purchases = purchases

    def add_purchase(self, purchase):
        if purchase.price > self.balance:
            raise Exception("Not enough balance")
        self.purchases.append(purchase)
        self.balance -= purchase.price
        return self
