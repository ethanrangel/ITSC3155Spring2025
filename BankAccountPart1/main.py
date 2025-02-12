class BankAccount:

    # class attribute (title of bank)
    bank_title = "Bank of America"

    # instance attributes (customer_name, current_balance, minimum_balance)
    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

    # deposit method
    def deposit(self, amount_to_deposit):
        self.current_balance += amount_to_deposit

    # withdraw method
    def withdraw(self, amount_to_withdraw):
        if self.current_balance - amount_to_withdraw >= self.minimum_balance:
            self.current_balance -= amount_to_withdraw
        # validation
        else:
            print("You are unable to deposit! You will be below the minimum balance amount.")

    # print customer info method
    def print_customer_information(self):
        print(
            '''
            Hello {}, Thank you for using {}. Here is your banking account information
            Current Balance: {}
            Minimum Balance: {}
            '''.format(self.customer_name, self.bank_title, self.current_balance, self.minimum_balance)
        )
# two instances
user1 = BankAccount("Ethan Rangel", 500, 100)
user2 = BankAccount("Rich Guy", 100000, 10000)

user1.deposit(1)
user2.deposit(10)

print(user1.current_balance)
print(user2.current_balance)

user1.withdraw(600)
user2.withdraw(50000)

user1.print_customer_information()
user2.print_customer_information()
