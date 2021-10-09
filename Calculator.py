from art import logo

print(logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1 / n2


def power(n1, n2):
    return n1 ** n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division,
    "**": power
}

num1 = int(input("First number: "))
num2 = int(input("Second number: "))

for op in operations:
    print(op)

operation = input('Please choose the operation: ')

function = operations[operation]
result = function(num1, num2)

print(result)