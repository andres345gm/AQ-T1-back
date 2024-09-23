import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class AddPurchaseToUser:
    def __init__(self, user_repository, purchase_repository):
        self.user_repository = user_repository
        self.purchase_repository = purchase_repository

    def execute(self, purchase_id):
        purchase = self.purchase_repository.read(purchase_id)
        if purchase is None:
            return False
        if purchase.id_user is None:
            return False
        user_id = purchase.id_user
        user = self.user_repository.read(user_id)
        if user is None:
            return False
        try:
            user.add_purchase(purchase)
            self.user_repository.update(user.id, user)
            return True
        except Exception as e:
            return False