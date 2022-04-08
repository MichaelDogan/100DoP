

# Calculator

# Add

def add(n1, n2):
    """Returns the result from adding n1 to n2. (n1+n2)"""
    return n1 + n2

# Subtract


def subtract(n1, n2):
    """Returns the result from subtracting n2 from n1. (n1-n2)"""
    return n1 - n2

# Multiply


def multiply(n1, n2):
    """Returns the result from multiplying n1 by n2. (n1 *n2)"""
    return n1 * n2

# Divide


def divide(n1, n2):
    """Returns the result from dividing n1 by n2 (n1/n2)"""
    return n1/n2


# Dictionary of math operation functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

num1 = int(input("What's the first number?: "))
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What's the second number?: "))
calculation_function = operations[operation_symbol]
# print(calculation_function)
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")
