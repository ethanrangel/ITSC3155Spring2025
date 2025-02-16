
Modular Ham Sandwich Maker Machine Program
In this assignment, you will use what you have learned about Python modules to make our Ham Sandwich
Maker Machine code more object-oriented. The program should be split into four separate files. To
complete this assignment, follow these steps.
1- Code Skeleton:
• On Canvas, you can find the code skeleton on the assignment page.
2- Import all modules into main.py
• Three modules (data, sandwich_maker, cashier) should be imported at the top of
main.py. “import <file_name>”
• Create two variables based on data dictionaries (resources and recipes).
• Then you need to create instance from each. Pay attention sandwich_maker class has a
constructor variable (resources) which you imported in last step. “<var> =
<imported_name>.<class_name>”
3- Place functions in corresponding module:
• The simplest way to accomplish this is to copy and paste the function into the
corresponding module according to the instructions at the end of this document.
4- Fine tune main.py
• Change the variable names if necessary and run the program. To test your program, you
can use the same scenario as in assignment 1.
Project Structure:
SandwichMaker class in sandwich_makerr.py file:
• This class contains everything about making sandwiches. The check_resources() and
make_sandwich() functions should be placed in this class.
Cashier class in cashier.py file:
• This class contains everything about purchasing. The process_coins() and
transaction_result() functions should be placed in this class.
Data.py:
• This file keeps the data we need to run program like a database! Later in the course, we
will convert it into a Python class that stores and retrieves data.
Main.py:
• It acts as the starting point of execution for the program.
