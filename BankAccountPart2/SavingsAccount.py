from BankAccount import BankAccount
class SavingsAccount(BankAccount):
   def __init__(self, customer_name, current_balance, minimum_balance, interest, account_number, routing_number):
       super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
       self.interest = interest


   def print_customer_information(self):
       print(
           '''
           Hello {}, Thank you for using {}. Here is your savings account information
           Current Balance: ${}
           Minimum Balance: ${}
           Interest: ${} %
           '''.format(self.customer_name, self.bank_title, self.current_balance, self.minimum_balance, self.interest)
       )