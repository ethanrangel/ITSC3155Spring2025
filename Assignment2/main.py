import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources, recipes)
cashier_instance = Cashier()




def main():
    ###  write the rest of the codes ###
    while True:
        users_choice = input("What would you like? (small/ medium/ large/ off/ report): ").lower()
        if users_choice == "report":
            print("Bread: {} slice(s)".format(resources['bread']))
            print("Ham: {} slice(s)".format(resources['ham']))
            print("Cheese: {} ounce(s)".format(resources['cheese']))
        elif users_choice in recipes:
            item = recipes[users_choice]
            if sandwich_maker_instance.check_resources(item["ingredients"]):
                total = cashier_instance.process_coins()
                if cashier_instance.transaction_result(total, item["cost"]):
                    sandwich_maker_instance.make_sandwich(users_choice, item["ingredients"])
        elif users_choice == "off":
            break
        else:
            print("Try again.")

if __name__=="__main__":
    main()
