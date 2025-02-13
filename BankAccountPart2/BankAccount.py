class BankAccount:

    # class attribute (title of bank)
    bank_title = "Bank of America"

    # instance attributes (customer_name, current_balance, minimum_balance)
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self._account_number = account_number
        self.__routing_number = routing_number

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
            Current Balance: ${}
            Minimum Balance: ${}
            '''.format(self.customer_name, self.bank_title, self.current_balance, self.minimum_balance)
        )