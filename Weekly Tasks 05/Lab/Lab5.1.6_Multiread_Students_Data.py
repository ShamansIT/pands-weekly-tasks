# Initialize an empty list to store information for all students
all_students_info = []

# Loop to read information for multiple students
while True:
    student_info = {}  # Initialize an empty dictionary for the current student

    # Read student's name
    student_name = input(
        "Enter the student's name (or leave blank to finish): ")
    if student_name == "":  # Check for blank input to break the loop
        break

    student_info['name'] = student_name

    # Initialize an empty dictionary to store modules and grades for the current student
    modules_and_grades = {}

    # Loop to read module names and grades for the current student
    while True:
        module_name = input(
            "Enter module name (or leave blank to finish for this student): ")
        if module_name == "":  # Check for blank input to break the loop
            break
        # Read grade as float
        grade = float(input(f"Enter grade for {module_name}: "))
        # Add module and grade to the dictionary
        modules_and_grades[module_name] = grade

        choise = input("Do you wish CONTINUE or create NEW STUDENT(N)")
        if choise == 'N' or choise == 'n':
            break

    # Assign modules and grades to the current student's dictionary
    student_info['modules'] = modules_and_grades

    # Add the current student's information to the list of all students
    all_students_info.append(student_info)

# Print information for all students
for student in all_students_info:
    print(student)
