import random
from pythonProject.app.adapters.out.poke_api_Repository import PokeApiAdapter
from pythonProject.app.domain.model.pokemon import Pokemon

class PokemonUseCase:
    def __init__(self, pokemon_adapter: PokeApiAdapter):
        self.pokemon_adapter = pokemon_adapter

    def get_pokemon_by_name_or_id(self, name_or_id: str):
        return self.pokemon_adapter.get_pokemon(name_or_id)
    
    def get_multiple_pokemons(self, n: int) -> list[Pokemon]:
        return self.pokemon_adapter.get_multiple_pokemons(n) # Se le pasa el número de Pokémon a obtener
