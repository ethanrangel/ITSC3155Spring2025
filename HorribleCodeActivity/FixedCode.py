def main():

    pass

def main():

    answer = ""

    while answer != "off":

        desiredInput = input("What operation do you want to do with this calculator add, subtract, multiply, divide or off: ")

        if desiredInput == "off":

            print("You are already tired of making calculations...... well have a good day!!!")
            break

        else:

            number1 = input("what is the first number you want to perform the operation on")
            number2 = input("what is the second number you want to perform the operation on")


        if desiredInput == "add":

            print("The result is: " + str(add(number1, number2)))

        if desiredInput == "subtract":

            print("The result is: " + str(subtract(number1, number2)))

        if desiredInput == "multiply":

            print("The result is: " + str(multiply(number1, number2)))

        if desiredInput == "divide":

            print("The result is: " + str(divide(number1, number2)))


def divide(number1, number2):
    """Return a int
    Division result between two numbers (number1 and number2)
    """
    return number1 / number2


def add(number1, number2): 
    """Return a int
    Addition result between two numbers (number1 and number2)
    """
    number1 + number2
    
def subtract(number1, number2):
    """Return a int
    Subtraction result between two numbers (number1 and number2)
    """
    return number1 - number2

def multiply(number1, number2):
    """Return a int
    Multiplication result between two numbers (number1 and number2)
    """
    return number1 * number2