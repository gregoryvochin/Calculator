def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
    }

def calculator():
    """
    Basic calculator for addition, multiplication, subtraction, and division.
    """
    on = ""

    cont = "n"

    answer = None

    while on == "":

        if cont == "n":
            num1 = float(input("What's the first number?: "))
        else:
            num1 = answer
            print(f"Your first number is: {answer}.")

        for key in operations:
            print(key)
            
        operation_symbol = input("Pick an operation from the line above: ")

        num2 = float(input("What's the next number?: "))

        answer = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        cont = input(f"Type 'y' to continue calculating with {answer}, or "
                     "type 'n' to start a new calculation: ")

        on = input("Enter any input to exit the program, otherwise just hit the enter key: ")

        if on != "":
            break
        
calculator()
