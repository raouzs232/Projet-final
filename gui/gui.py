import tkinter as tk
from tkinter import messagebox

class PokemonSearchGUI:
    def __init__(self, search_function):
        self.root = tk.Tk()
        self.search_function = search_function
        self.setup_gui()

    def setup_gui(self):
        self.pokemon_name_label = tk.Label(self.root)
        self.similar_names_buttons = []
        self.pokemon_card_frame = tk.Frame(self.root)
        self.not_found_label = tk.Label(self.root)
        self.card_background_color = "#C3E2C2"
        self.card_background_color2 = "#EAECCC"

    def search_pokemon(self, random_pokemon=False):
        pokemon_name = None if random_pokemon else self.entry.get().strip().lower()
        if pokemon_name or random_pokemon:
            loading_label = tk.Label(self.root, text="Searching for Pokémon...")
            loading_label.pack()
            self.not_found_label.pack_forget()
            self.root.update()  
            try:
                pokemon_details, similar_names_list = self.search_function(pokemon_name)
            except Exception as e:
                loading_label.pack_forget()
                self.not_found_label.configure(text="Something went wrong!")
                self.not_found_label.pack()
                print(str(e))
                return
            loading_label.pack_forget()
            if pokemon_details is None:
                self.pokemon_card_frame.pack_forget()
                if similar_names_list and len(similar_names_list):
                    self.display_similar_pokemon(similar_names_list)
                else:
                    self.remove_similar_pokemon()
                    self.not_found_label.configure(text='Pokémon could not be found!')
                    self.not_found_label.pack()
            else:
                self.remove_similar_pokemon()
                self.not_found_label.pack_forget()
                self.pokemon_card_frame.pack_forget()
                self.display_pokemon_details(pokemon_details)
        else:
            messagebox.showerror("Error", "Please enter a Pokemon name.")

    def search_random(self):
        self.search_pokemon(random_pokemon=True)

    def display_pokemon_details(self, pokemon_details):
        for element in self.pokemon_card_frame.winfo_children():
            element.destroy()
        self.pokemon_card_frame.configure(background=self.card_background_color, borderwidth=2, relief='raised')
        self.pokemon_card_frame.pack(pady=(10, 10), side='top')
        image_label = tk.Label(self.pokemon_card_frame, image=pokemon_details['picture'], borderwidth=1, relief='groove', background='#E5E1DA')
        image_label.image = pokemon_details['picture']
        image_label.pack(padx=10, pady=10)
        details_frame = tk.Frame(self.pokemon_card_frame, width=150, background=self.card_background_color2, borderwidth=1, relief='sunken')
        details_frame.pack(pady=(0, 10))
        name_label = tk.Label(details_frame, text=pokemon_details['name'], font=("Helvetica", 14, "bold"), foreground="#FF0000", background=self.card_background_color2)
        name_label.pack()

        if len(pokemon_details['abilities']) > 0:
            abilities_frame = tk.Frame(details_frame, background=self.card_background_color2)
            abilities_label = tk.Label(abilities_frame, text="Abilities", font=("Helvetica", 10, "bold"), background=self.card_background_color2)
            abilities_label.pack(side="top")

            abilities_list = ", ".join(pokemon_details['abilities'])
            abilities_list_label = tk.Label(abilities_frame, text=abilities_list, foreground='#0055AA', wraplength=150, background=self.card_background_color2)
            abilities_list_label.pack()
            abilities_frame.pack()

        if len(pokemon_details['moves']) > 0:
            moves_frame = tk.Frame(details_frame, background=self.card_background_color2)
            moves_label = tk.Label(moves_frame, text="Moves", font=("Helvetica", 10, "bold"), background=self.card_background_color2)
            moves_label.pack(side="top")

            moves_list = ", ".join(pokemon_details['moves'])
            moves_list_label = tk.Label(moves_frame, text=moves_list, foreground='#0055AA', wraplength=150, background=self.card_background_color2)
            moves_list_label.pack()
            moves_frame.pack()

    def display_similar_pokemon(self, similar_names_list):
        self.remove_similar_pokemon()
        label = tk.Label(self.root, text="Did you mean:")
        self.similar_names_buttons.append(label)
        label.pack()

        for name in similar_names_list:
            button = tk.Button(self.root, text=name, command=lambda n=name: self.search_similar_pokemon(n))
            self.similar_names_buttons.append(button)
            button.pack()
    
    def remove_similar_pokemon(self):
        for element in self.similar_names_buttons:
            element.destroy()
        self.similar_names_buttons.clear()

    def search_similar_pokemon(self, pokemon_name):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, pokemon_name)
        self.search_pokemon()

    def draw_gui(self):
        screen_width = 500
        screen_height = 500

        self.root.geometry(f"{screen_width}x{screen_height}")
        self.root.title("Pokemon API")

        label = tk.Label(self.root, text="Enter Pokemon Name:")
        label.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=5)

        button_frame = tk.Frame(self.root)  
        button_frame.pack(pady=5)

        search_button = tk.Button(button_frame, text="Search", command=self.search_pokemon)
        search_button.pack(side="left", padx=(0, 5))

        random_button = tk.Button(button_frame, text="Random", command=self.search_random)
        random_button.pack(side="right", padx=(5, 0))
        
        self.root.mainloop()