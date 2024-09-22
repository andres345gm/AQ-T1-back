from fastapi import FastAPI, HTTPException
from app.domain.use_cases.pokemon_api_use_case import PokemonUseCase
from app.adapters.out.poke_api import PokeApiAdapter


app = FastAPI()

poke_api_adapter = PokeApiAdapter()
pokemon_use_case = PokemonUseCase(poke_api_adapter)

@app.get("/pokemon/{name_or_id}")
def get_pokemon(name_or_id: str):
    try:
        pokemon = pokemon_use_case.get_pokemon_by_name_or_id(name_or_id)
        return {
            "id": pokemon.id,
            "name": pokemon.name,
            "height": pokemon.height,
            "weight": pokemon.weight,
            "stats": pokemon.stats,
            "image": pokemon.image  
        }
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.get("/pokemons/{n}")
def get_multiple_pokemons(n: int):
    try:
        pokemons = pokemon_use_case.get_multiple_pokemons(n)
        return [
            {
                "id": pokemon.id,
                "name": pokemon.name,
                "height": pokemon.height,
                "weight": pokemon.weight,
                "stats": pokemon.stats,
                "image": pokemon.image
            } for pokemon in pokemons
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))