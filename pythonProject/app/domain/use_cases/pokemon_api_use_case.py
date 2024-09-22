import random
from app.adapters.out.poke_api import PokeApiAdapter
from app.domain.model.pokemon import Pokemon

class PokemonUseCase:
    def __init__(self, pokemon_adapter: PokeApiAdapter):
        self.pokemon_adapter = pokemon_adapter

    def get_pokemon_by_name_or_id(self, name_or_id: str):
        return self.pokemon_adapter.get_pokemon(name_or_id)
    
    def get_multiple_pokemons(self, n: int) -> list[Pokemon]:
        pokemons = []
        
        max_pokemon_id = self.pokemon_adapter.get_total_pokemon_count() 

        for _ in range(n): 
            random_id = random.randint(1, max_pokemon_id)  
            try:
                pokemon = self.pokemon_adapter.get_pokemon(random_id)
                pokemons.append(pokemon) 
            except Exception as e:
                print(f"Error fetching Pokémon with ID {random_id}: {e}")

        return pokemons
