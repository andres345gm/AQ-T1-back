import random

import requests
from pythonProject.app.domain.model.pokemon import Pokemon
from pythonProject.app.domain.ports.pokemon_repository import IPokemonRepository

class PokeApiAdapter(IPokemonRepository):
    BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
    SPECIES_URL = "https://pokeapi.co/api/v2/pokemon-species/"

    def get_pokemon(self, name_or_id: str) -> Pokemon:
        response = requests.get(f"{self.BASE_URL}{name_or_id}")
        if response.status_code == 200:
            data = response.json()

            # Recoger todas las posibles URLs de imágenes (que no sean nulas)
            sprite_options = [
                data["sprites"]["back_default"],
                data["sprites"]["back_female"],
                data["sprites"]["back_shiny"],
                data["sprites"]["back_shiny_female"],
                data["sprites"]["front_default"],
                data["sprites"]["front_female"],
                data["sprites"]["front_shiny"],
                data["sprites"]["front_shiny_female"],
            ]

            # Filtrar solo los que no son None
            available_sprites = [
                sprite for sprite in sprite_options if sprite is not None
            ]

            # Seleccionar una imagen aleatoria de las disponibles
            chosen_image = random.choice(available_sprites)

            # Obtener hp y attack
            hp = next(
                stat["base_stat"]
                for stat in data["stats"]
                if stat["stat"]["name"] == "hp"
            )
            attack = next(
                stat["base_stat"]
                for stat in data["stats"]
                if stat["stat"]["name"] == "attack"
            )

            # Crear la entidad Pokémon con la imagen seleccionada aleatoriamente
            pokemon = Pokemon(
                id=data["id"],
                name=data["name"],
                height=data["height"],
                weight=data["weight"],
                hp=hp,  # Solo hp
                attack=attack,  # Solo attack
                image=chosen_image,  # Imagen aleatoria
            )
            return pokemon
        else:
            raise Exception(f"Error fetching data from PokeAPI: {response.status_code}")

    def get_multiple_pokemons(self, n: int) -> list[Pokemon]:
        
        response = requests.get(self.SPECIES_URL)
        if response.status_code == 200:
            data = response.json()
            max_pokemon_id = data["count"]
            
            # Inicializar la lista de pokemons
            pokemons = []  # Asegúrate de inicializar la lista aquí

            for _ in range(n):
                random_id = random.randint(1, max_pokemon_id)
                try:
                    pokemon = self.get_pokemon(random_id)
                    pokemons.append(pokemon)
                except Exception as e:
                    print(f"Error fetching Pokémon with ID {random_id}: {e}")

            return pokemons
        else:
            raise Exception(
                f"Error fetching total Pokémon count: {response.status_code}"
            )

