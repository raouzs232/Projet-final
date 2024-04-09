from utils.pokemon import fetch_pokemon_details
from gui.gui import PokemonSearchGUI

def main():
    gui = PokemonSearchGUI(fetch_pokemon_details)
    gui.draw_gui()

if __name__ == '__main__':
    main()