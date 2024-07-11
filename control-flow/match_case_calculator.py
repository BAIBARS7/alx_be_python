# Prompting for user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Asking for the type of operation
operation = input("Choose the operation (+, -, *, /): ")

# Performing the calculation using match case statement
result = None

# Using match case (available in Python 3.10+)
try:
    match operation:
        case '+':
            result = num1 + num2
        case '-':
            result = num1 - num2
        case '*':
            result = num1 * num2
        case '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero is not allowed.")
        case _:
            print(f"Error: Invalid operation '{operation}'.")
except SyntaxError:
# Handling SyntaxError in case the version of Python used does not support the match statement.
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print(f"Error: Invalid operation '{operation}'.")

# Displaying the result
if result is not None:
    print(f"The result is {result}")
