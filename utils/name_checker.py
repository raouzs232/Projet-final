import difflib
import random

def check_pokemon_name(pokemon_name=None):
    with open('./data/pokemon_name_list.txt', 'r') as file:
        saved_names = file.read().split('\n')

    if pokemon_name is not None:
        similarities = [(saved_name.strip(), difflib.SequenceMatcher(None, pokemon_name, saved_name).ratio()) for saved_name in saved_names]

        similarities.sort(key=lambda x: x[1], reverse=True)

        exact_matches = [similarity[0] for similarity in similarities if similarity[1] > .95]

        if exact_matches:
            return True, exact_matches
    else:
        return True, [random.choice(saved_names)]

    top_matches = [similarity[0] for similarity in similarities if similarity[1] >= 0.75][:5]

    return False, top_matches