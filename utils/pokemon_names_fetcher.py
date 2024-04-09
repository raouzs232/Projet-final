import requests

def list_all_pokemon(limit=100):
    url = f"https://pokeapi.co/api/v2/pokemon/?limit={limit}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        pokemon_names = ''
        for pokemon in data['results']:
            pokemon_names += f"{pokemon['name']}\n"
        with open('./data/pokemon_name_lists.txt', 'w') as file:
            file.write(pokemon_names)
    else:
        print("Failed to fetch data")

if __name__ == "__main__":
    list_all_pokemon(limit=1500)