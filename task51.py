def  student_marks():
    
    # 1. Create a dictionary where student names are keys and their marks are values.
    student_marks = {
        "Alice": 85,
        "Bob": 92,
        "Charlie": 78,
        "David": 65,
        "Eve": 95
    }

    # 2. Ask the user to input a student's name.
    student_name = input("Enter the student's name: ")

    # 3. Retrieves and displays the corresponding marks.
    # 4. If the student’s name is not found, display an appropriate message.
    if student_name in student_marks:
        print(f"Marks for {student_name}: {student_marks[student_name]}")
    else:
        print(f"Student '{student_name}' not found in the records.")

# Call the function to execute the program
student_marks()