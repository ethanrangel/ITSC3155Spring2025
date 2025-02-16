class Cashier:
    def __init__(self):
        pass

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
