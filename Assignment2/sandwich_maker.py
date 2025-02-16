
class SandwichMaker:
    def __init__(self, resources, recipes):
        self.machine_resources = resources
        self.recipes = recipes

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        if self.machine_resources["bread"] < ingredients["bread"]:
            print("Sorry there is not enough bread.")
            return False
        elif self.machine_resources["ham"] < ingredients["ham"]:
            print("Sorry there is not enough ham.")
            return False
        elif self.machine_resources["cheese"] < ingredients["cheese"]:
            print("Sorry there is not enough cheese.")
            return False
        else:
            return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for ingredient in order_ingredients:
            amount = order_ingredients[ingredient]
            self.machine_resources[ingredient] -= amount
        print(sandwich_size + " sandwich is ready. Bon appetit!")