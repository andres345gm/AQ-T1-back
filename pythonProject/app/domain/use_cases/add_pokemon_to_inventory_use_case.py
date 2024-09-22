from abc import ABC, abstractmethod

class AddPokemonToInventoryUseCase(ABC):
    @abstractmethod
    def add_pokemon_to_inventory(self, username: str, pokemon_name: str) -> bool:
        pass