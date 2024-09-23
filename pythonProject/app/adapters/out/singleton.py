from pythonProject.app.adapters.out.mock_purchase_repository import MockPurchaseRepository
from pythonProject.app.adapters.out.mock_user_repository import MockUserRepository

singletonUserRepository = MockUserRepository()
singletonPurchaseRepository = MockPurchaseRepository()