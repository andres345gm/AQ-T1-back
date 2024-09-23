import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class AddPurchaseToUser:
    def __init__(self, user_repository, purchase_repository):
        self.user_repository = user_repository
        self.purchase_repository = purchase_repository

    def execute(self, user_id, purchase_id):
        user = self.user_repository.read(user_id)
        purchase = self.purchase_repository.read(purchase_id)
        user.add_purchase(purchase)
        self.user_repository.update(user.id, user)