from api.api import fetch_data
from api.image_process import process_image
from utils.name_checker import check_pokemon_name

def fetch_pokemon_details(pokemon_name=None):
    found, names_list = check_pokemon_name(pokemon_name)
    if not found:
        return None, names_list

    url = f"https://pokeapi.co/api/v2/pokemon/{names_list[0]}"
    response_json = fetch_data(url)

    if response_json is None:
        return None, None

    pokemon_details = dict()

    image_url = response_json['sprites']['front_default']
    pokemon_image = process_image(image_url)

    pokemon_details['name'] = response_json['name'].capitalize()
    pokemon_details['picture'] = pokemon_image
    pokemon_details['abilities'] = [x['ability']['name'].capitalize() for x in response_json['abilities']][:5]
    pokemon_details['moves'] = [x['move']['name'].capitalize() for x in response_json['moves']][:5]

    return pokemon_details, None