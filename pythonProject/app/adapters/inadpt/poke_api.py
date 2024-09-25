from typing import List
from fastapi import APIRouter, FastAPI, HTTPException
import logging  # Importar el módulo logging
from pythonProject.app.adapters.out.poke_api_Repository import PokeApiAdapter
from pythonProject.app.domain.use_cases.pokemon_api_use_case import PokemonUseCase
from pythonProject.app.adapters.DTOs.poke_info_dto import PokeInfoDTO, map_poke_to_dto
from pythonProject.app.adapters.DTOs.poke_mini_info_dto import PokeMiniInfoDTO

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

poke_router = APIRouter()
poke_api = PokeApiAdapter()
poke_petition = PokemonUseCase(poke_api)


@poke_router.get("/poke/{poke_id}", response_model=PokeInfoDTO)
def get_user(poke_id: str):
    # obtener info del pokemon
    logger.info(f"Fetching Pokémon with id {poke_id}")
    poke = poke_petition.get_pokemon_by_name_or_id(poke_id)
    if poke:
        poke_response = map_poke_to_dto(poke)
        return poke_response  # FastAPI convierte el objeto a PokeInfoDTO
    raise HTTPException(status_code=404, detail="Poke not found")


@poke_router.get("/poke/all/{n}", response_model=List[PokeMiniInfoDTO])
def get_user(n: int):
    # Obtener info de los Pokémon
    logger.info(f"Fetching {n} Pokémons")
    pokes = poke_petition.get_multiple_pokemons(n)

    if pokes:
        return [
            PokeMiniInfoDTO(id=poke.id_, name=poke.name, image=poke.image)
            for poke in pokes
        ]

    raise HTTPException(status_code=404, detail="Pokémon not found")
