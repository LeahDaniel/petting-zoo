class PettingZoo:

    def __init__(self, attraction_name, description):
        self.attraction_name = attraction_name
        self.description = description
        self.animals = list()

    def add_animal(self, new_animal):
        self.animals.append(new_animal)

    def __str__(self):
        string = f"{self.attraction_name} is where you'll find {self.description}, like"
        for animal in self.animals:
            string += f'\n * {animal.name} the {animal.species}'
        return string


class SnakePit:

    def __init__(self, attraction_name, description):
        self.attraction_name = attraction_name
        self.description = description
        self.animals = list()

    def add_animal(self, new_animal):
        self.animals.append(new_animal)

    def __str__(self):
        string = f"{self.attraction_name} is where you'll find {self.description}, like"
        for animal in self.animals:
            string += f'\n * {animal.name} the {animal.species}'
        return string


class Wetlands:

    def __init__(self, attraction_name, description):
        self.attraction_name = attraction_name
        self.description = description
        self.animals = list()

    def add_animal(self, new_animal):
        self.animals.append(new_animal)

    def __str__(self):
        string = f"{self.attraction_name} is where you'll find {self.description}, like"
        for animal in self.animals:
            string += f'\n * {animal.name} the {animal.species}'
        return string
    
    @property
    def last_critter_added(self):
        return f'{self.animals[-1].name} the {self.animals[-1].species}'
