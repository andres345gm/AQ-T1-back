class LoginUseCase:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def login(self, username, password):
        user = self.user_repo.get_user_by_username(username)
        if user is None:
            return False
        if user.password != password:
            return False
        return user
