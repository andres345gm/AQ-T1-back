import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AddPurchaseToUser:
    def __init__(self, user_repository, purchase_repository):
        self.user_repository = user_repository
        self.purchase_repository = purchase_repository

    def execute(self, purchase_data):
        user = self.user_repository.read(purchase_data.id_user)
        if not user:
            return None
        purchase = self.purchase_repository.create(purchase_data)
        if not purchase:
            logger.error("Purchase not created")
            return None
        user.add_purchase(purchase)
        self.user_repository.update(purchase_data.id_user, user)
        return user

