def demonstrate_list_slicing():
    
    # 1. Creates a list of numbers from 1 to 10.
    numbers = list(range(1, 11))
    print(f"Original list: {numbers}")

    # 2. Extracts the first five elements from the list.
    first_five_elements = numbers[0:5] 
    print(f"Extracted first five elements: {first_five_elements}")

    # 3. Reverses these extracted elements.
    reversed_elements = first_five_elements[::-1] 
    print(f"Reversed extracted elements: {reversed_elements}")
 
demonstrate_list_slicing()