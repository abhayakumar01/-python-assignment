# Take an integer input from the user
try:
    number = int(input("Enter an integer: "))
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    exit()

# Check whether the number is even or odd using an if-else statement
if number % 2 == 0:
    print(f"The number {number} is Even.")
else:
    print(f"The number {number} is Odd.")