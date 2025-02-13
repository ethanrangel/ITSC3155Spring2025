from BankAccount import BankAccount
class CheckingAccount(BankAccount):
   def __init__(self, customer_name, current_balance, minimum_balance, transfer_limit):
       super().__init__(customer_name, current_balance, minimum_balance)
       self.transfer_limit = transfer_limit
def print_customer_information(self):
       print(
           '''
           Hello {}, Thank you for using {}. Here is your checking account information
           Current Balance: ${}
           Minimum Balance: ${}
           Transfer Limit: ${} %
           '''.format(self.customer_name, self.bank_title, self.current_balance, self.minimum_balance, self.transfer_limit)
       )
