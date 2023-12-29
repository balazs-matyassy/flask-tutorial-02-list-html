import base64


class Recipe:
    def __init__(self, category='', name='', description='', difficulty=1, recipe_id=None):
        self.recipe_id = recipe_id
        self.category = category
        self.name = name
        self.description = description
        self.difficulty = difficulty

    @property
    def difficulty_description(self):
        if self.difficulty == 1:
            return 'Very easy'
        elif self.difficulty == 2:
            return 'Easy'
        elif self.difficulty == 3:
            return 'Medium'
        elif self.difficulty == 4:
            return 'Difficult'
        elif self.difficulty == 5:
            return 'Very difficult'

        return 'Unknown'

    @staticmethod
    def create_from_line(line):
        values = line.strip().split('\t')
        description = (base64
                       .b64decode(values[3].strip().encode('utf-8'))
                       .decode('utf-8'))

        return Recipe(
            recipe_id=int(values[0].strip()),
            category=values[1].strip(),
            name=values[2].strip(),
            description=description,
            difficulty=int(values[4].strip())
        )


def find_all():
    with open('recipes.txt', encoding='utf-8') as file:
        recipes = []

        file.readline()  # header

        for line in file:
            recipe = Recipe.create_from_line(line)
            recipes.append(recipe)

        return recipes


def find_by_id(recipe_id):
    for recipe in find_all():
        if recipe.recipe_id == recipe_id:
            return recipe

    return None


def find_by_name(name):
    recipes = []

    for recipe in find_all():
        if name.lower() in recipe.name.lower():
            recipes.append(recipe)

    return recipes
