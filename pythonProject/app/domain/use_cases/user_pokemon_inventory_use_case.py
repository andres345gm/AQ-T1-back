class UserPokemonInventoryUseCase():
    def __init__(self, user_repo, pokemon_repo):
        self.user_repo = user_repo
        self.pokemon_repo = pokemon_repo

    def get_user_pokemon_inventory(self, user_id):
        user = self.user_repo.get_user(user_id)
        return user.pokemon_inventory

    def add_pokemon_to_user_inventory(self, user_id, pokemon_id):
        user = self.user_repo.get_user(user_id)
        pokemon = self.pokemon_repo.get_pokemon(pokemon_id)
        user.pokemon_inventory.append(pokemon)
        self.user_repo.update_user(user_id, user)
        return user.pokemon_inventory

    def remove_pokemon_from_user_inventory(self, user_id, pokemon_id):
        user = self.user_repo.get_user(user_id)
        pokemon = self.pokemon_repo.get_pokemon(pokemon_id)
        user.pokemon_inventory.remove(pokemon)
        self.user_repo.update_user(user_id, user)
        return user.pokemon_inventory
