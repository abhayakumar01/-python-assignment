def write_and_append(filename):
 
    try:
        # 1. Take user input and write it to the file (overwrites if file exists)
        user_initial_input = input("Enter initial data to write to the file: ")
        with open(filename, 'w') as file:
            file.write(user_initial_input + "\n")
        print(f"Initial data written to '{filename}'.")

        # 2. Append additional data to the same file
        additional_data = input("Enter additional data to append to the file: ")
        with open(filename, 'a') as file:
            file.write(additional_data + "\n")
        print(f"Additional data appended to '{filename}'.")

        # 3. Read and display the final content of the file
        print(f"\nFinal content of '{filename}':")
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())

    except IOError as e:
        print(f"An I/O error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
 
write_and_append("output.txt")