# This will be our bad code
##entire file no comments so violates documentation
def main():
    
    answer = ""
    
    while answer != "off":
        
        desiredInput = input("What operation do you want to do with this calculator add, subtract, multiply, divide or off: ")
        
        if desiredInput == "off":
            break
        else:
            number1 = input("what is the first number you want to perform the operation on")
            number2 = input("what is the second number you want to perform the operation on")
            
            
        possibleInputs15 = [add, subtract, multiply, divide]
        possibleInputs155555= ['add', 'subtract', 'multiply', 'divide']
        
        print("Result" + str(possibleInputs15[possibleInputs155555.index(desiredInput)](int(number1), int(number2)))) #just horrible and not clean code in the slightest
        
def divide(number1, number2):
    
    return number1 / number2
def add(number1, number2): 
    sum = 0
    numberarray = [number1, number2]#Violates KISS
    for i in numberarray:
        sum += i
    return sum      
def subtract(number1, number2):
    return number1 - number2 - number1 + number2  
