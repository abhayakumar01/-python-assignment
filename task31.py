def factorial(n):
    
    if n < 0:
        return  
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Call the function with a sample number and print the output
sample_number = 5
print(f"The factorial of {sample_number} is: {factorial(sample_number)}")

sample_number_zero = 0
print(f"The factorial of {sample_number_zero} is: {factorial(sample_number_zero)}")

sample_number_negative = -3
print(f"The factorial of {sample_number_negative} is: {factorial(sample_number_negative)}")