from python_advanced_and_oop.OOP.first_steps_oop.project.pokemon import Pokemon


class Trainer:

    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, poke_name: Pokemon):
        if poke_name in self.pokemons:
            return "This pokemon is already caught"
        self.pokemons.append(poke_name)
        return f"Caught {poke_name.pokemon_details()}"

    def release_pokemon(self, pokemon_name):
        for poke in self.pokemons:
            if poke.name == pokemon_name:
                self.pokemons.remove(poke)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\n"
        result += f"Pokemon count {len(self.pokemons)}\n"

        for pokemon in self.pokemons:
            result += f"- {Pokemon.pokemon_details(pokemon)}" + "\n"
        return result.strip()
