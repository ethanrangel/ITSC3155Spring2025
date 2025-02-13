from CheckingAccount import CheckingAccount
from SavingsAccount import SavingsAccount 

# two instances
checking_user = CheckingAccount("Ethan Rangel", 500, 100, 50, 6831125, 809401499)
savings_user = SavingsAccount("Irfan Campara", 100000, 10000, 2.5, 6831126, 809401500)

checking_user.deposit(200)
checking_user.withdraw(300)
checking_user.print_customer_information()

savings_user.deposit(5000)
savings_user.print_customer_information()
