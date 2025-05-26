import math

try:
    num = float(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

# Calculate the square root, natural logarithm, and sine of the number
square_root = math.sqrt(num)
natural_log = math.log(num)
sine_value = math.sin(num)

# Display the calculated results
print(f"The square root of {num} is: {square_root}")
print(f"The natural logarithm (log base e) of {num} is: {natural_log}")
print(f"The sine of {num} radians is: {sine_value}")