from BankAccount import BankAccount

class CheckingAccount(BankAccount):
   def __init__(self, customer_name, current_balance, minimum_balance, transfer_limit, account_number, routing_number):
       super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
       self.transfer_limit = transfer_limit


   def print_customer_information(self):
       print(
           '''
           Hello {}, Thank you for using {}. Here is your savings account information
           Current Balance: ${}
           Minimum Balance: ${}
           Interest: ${} %
           '''.format(self.customer_name, self.bank_title, self.current_balance, self.minimum_balance, self.transfer_limit)
       )