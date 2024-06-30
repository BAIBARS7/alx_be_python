# Prompting for user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Asking for the type of operation
operation = input("Choose the operation (+, -, *, /): ")

# Performing the calculation using a match case statement
result = None

# Using match case (available in Python 3.10+)
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

# Displaying the result
if result is not None:
    print(f"The result of {num1} {operation} {num2} is: {result}")
