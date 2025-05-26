def read_file(filename):
   
    try:
        with open(filename, 'r') as file:
            print(f"Content of {filename}:")
            for line in file:
                print(line.strip()) 
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

read_file("sample.txt")

# Example of a file that does not exist
print("\n--- Testing with a non-existent file ---")
read_file("nonexistent_file.txt")