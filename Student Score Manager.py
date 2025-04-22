"""
Student Score Manager  
This script allows you to manage student scores, including adding new students,  
calculating the average score, and finding top scorers (students with score > 90).  
"""

# Initialize an empty list to store students as dictionaries with 'name' and 'score'
students = []

def add_student(name, score):
    """
    Adds a new student with the given name and score to the students list.
    :param name: str, the student's name
    :param score: float or int, the student's score
    """
    # Create a dictionary for the student and append to the list
    student = {"name": name, "score": score}
    students.append(student)

def calculate_average():
    """
    Calculates and returns the average score of all students.
    :return: float, the average score, or None if there are no students.
    """
    if len(students) == 0:
        return None  # No students to calculate average
    # Compute sum of all scores and divide by number of students
    total = sum(student["score"] for student in students)
    average = total / len(students)
    return average

def get_top_scorers():
    """
    Returns a list of students (dictionaries) who have a score greater than 90.
    :return: list of dicts, each containing 'name' and 'score' of a top scoring student.
    """
    # Filter the students with score > 90
    top_students = [student for student in students if student["score"] > 90]
    return top_students

# Main program loop for CLI menu
if __name__ == "__main__":
    # Print a welcome message or title
    print("Student Score Manager")
    while True:
        # Display the menu options
        print("\nMenu:")
        print("1. Add a new student")
        print("2. View average score")
        print("3. View top scorers")
        print("4. Exit")
        # Prompt the user to enter a choice
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            # Option 1: Add a new student
            name = input("Enter student name: ").strip()
            # Continuously prompt for score until a valid number is entered
            while True:
                score_input = input("Enter student score: ").strip()
                try:
                    # Try to convert to float (this will also handle int values)
                    score_value = float(score_input)
                    break  # exit loop if conversion is successful
                except ValueError:
                    print("Invalid score. Please enter a numeric value.")
            
            # Add the student using the add_student function
            add_student(name, score_value)
            print(f"Student '{name}' with score {score_value} added successfully!")
        
        elif choice == "2":
            # Option 2: View average score
            avg = calculate_average()
            if avg is None:
                print("No students available to calculate an average.")
            else:
                # Format to two decimal places
                print(f"Average score of {len(students)} student(s) is: {avg:.2f}")
        
        elif choice == "3":
            # Option 3: View top scorers
            top_students = get_top_scorers()
            if not top_students:
                print("No students with a score above 90.")
            else:
                print("Students with scores above 90:")
                for student in top_students:
                    print(f"{student['name']} - {student['score']}")
        
        elif choice == "4":
            # Option 4: Exit the program
            print("Exiting Student Score Manager. Goodbye!")
            break
        
        else:
            # Handle invalid menu choices
            print("Invalid choice. Please enter a number from 1 to 4.")
# End of the script