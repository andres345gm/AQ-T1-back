class AddPurchaseToUser:
    def __init__(self, user_repository, purchase_repository):
        self.user_repository = user_repository
        self.purchase_repository = purchase_repository

    def execute(self, user_id, purchase_id):
        user = self.user_repository.get(user_id)
        purchase = self.purchase_repository.get(purchase_id)
        user.add_purchase(purchase)
        self.user_repository.update(user)