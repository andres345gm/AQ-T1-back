import requests
import random
from app.domain.model.pokemon import Pokemon

class PokeApiAdapter:
    BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
    SPECIES_URL = "https://pokeapi.co/api/v2/pokemon-species/"

    def get_pokemon(self, name_or_id: str) -> Pokemon:
        response = requests.get(f"{self.BASE_URL}{name_or_id}")
        if response.status_code == 200:
            data = response.json()

            # Recoger todas las posibles URLs de imágenes (que no sean nulas)
            sprite_options = [
                data['sprites']['back_default'],
                data['sprites']['back_female'],
                data['sprites']['back_shiny'],
                data['sprites']['back_shiny_female'],
                data['sprites']['front_default'],
                data['sprites']['front_female'],
                data['sprites']['front_shiny'],
                data['sprites']['front_shiny_female']
            ]

            # Filtrar solo los que no son None
            available_sprites = [sprite for sprite in sprite_options if sprite is not None]

            # Seleccionar una imagen aleatoria de las disponibles
            chosen_image = random.choice(available_sprites)

            # Crear la entidad Pokémon con la imagen seleccionada aleatoriamente
            pokemon = Pokemon(
                id=data['id'],
                name=data['name'],
                height=data['height'],
                weight=data['weight'],
                stats={stat['stat']['name']: stat['base_stat'] for stat in data['stats']},
                image=chosen_image  # Imagen aleatoria
            )
            return pokemon
        else:
            raise Exception(f"Error fetching data from PokeAPI: {response.status_code}")
        
    def get_total_pokemon_count(self) -> int:
        response = requests.get(self.SPECIES_URL)
        if response.status_code == 200:
            data = response.json()
            return data['count']
        else:
            raise Exception(f"Error fetching total Pokémon count: {response.status_code}")
