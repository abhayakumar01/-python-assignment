# task1.py

# Get input from the user for two numbers
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input. Please enter valid numbers.")
    exit()

# Perform basic mathematical operations
addition = num1 + num2
subtract = num1 - num2
multiply = num1 * num2

# Handle division by zero
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (division by zero)"

# Display the results
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtract}")
print(f"Multiplication: {num1} * {num2} = {multiply}")
print(f"Division: {num1} / {num2} = {division}")