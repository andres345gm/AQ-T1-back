from abc import ABC, abstractmethod
from typing import List
from app.domain.model.pokemon import Pokemon

class PokemonRepository(ABC):
    @abstractmethod
    def get_pokemon(self, id: int) -> Pokemon:
        pass

    @abstractmethod
    def get_pokemons(self) -> List[Pokemon]:
        pass

    @abstractmethod
    def create_pokemon(self, name: str, height: int, weight: int, stats: dict) -> Pokemon:
        pass

    @abstractmethod
    def update_pokemon(self, id: int, name: str, height: int, weight: int, stats: dict) -> Pokemon:
        pass

    @abstractmethod
    def delete_pokemon(self, id: int) -> Pokemon:
        pass