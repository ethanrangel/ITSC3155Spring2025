### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

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

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input(how many quarters?: )"""
        print("Please insert coins.")
        dollars = int(input("How many large dollars?: "))
        half_dollars = int(input("How many half dollars?: ")) / 2
        quarters = int(input("How many quarters?: ")) / 4
        nickels = int(input("How many nickels?: ")) / 20
        total = dollars + half_dollars + quarters + nickels
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins < cost:
            print("Sorry that’s not enough money. Money refunded.")
            return False
        elif coins >= cost:
            change = float(coins - cost)
            print("Here is ${} in change.".format(change))
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""



### Make an instance of SandwichMachine class and write the rest of the codes ###


