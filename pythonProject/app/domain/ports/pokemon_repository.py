from abc import ABC, abstractmethod
from typing import List
from pythonProject.app.domain.model.pokemon import Pokemon

class IPokemonRepository(ABC):
    @abstractmethod
    def get_pokemon(self, name_or_id: str) -> Pokemon:
        pass

    @abstractmethod
    def get_multiple_pokemons(self, n: int) -> list[Pokemon]:
        pass