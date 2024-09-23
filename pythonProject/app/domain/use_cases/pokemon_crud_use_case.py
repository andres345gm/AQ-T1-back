from typing import List

from pythonProject.app.domain.model.pokemon import Pokemon
from pythonProject.app.domain.use_cases.repositories.pokemon_repository import PokemonRepository


class PokemonCrudUseCase:
    def __init__(self, pokemon_repo: PokemonRepository):
        self.pokemon_repo = pokemon_repo

    def get_pokemon(self, id: int) -> Pokemon:
        return self.pokemon_repo.get_pokemon(id)

    def get_pokemons(self) -> List[Pokemon]:
        return self.pokemon_repo.get_pokemons()

    def create_pokemon(self, name: str, height: int, weight: int, stats: dict) -> Pokemon:
        return self.pokemon_repo.create_pokemon(name, height, weight, stats)

    def update_pokemon(self, id: int, name: str, height: int, weight: int, stats: dict) -> Pokemon:
        return self.pokemon_repo.update_pokemon(id, name, height, weight, stats)

    def delete_pokemon(self, id: int) -> Pokemon:
        return self.pokemon_repo.delete_pokemon(id)