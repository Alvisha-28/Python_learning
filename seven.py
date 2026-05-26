# Grading system along with the average of marks of students and also checks for invalid marks 
# and also takes the average of the score and finds the topper

def get_grade(marks):
    """Assign grade based on marks"""
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    elif marks >= 50:
        return 'E'
    else:
        return 'F'

def validate_marks(marks):
    """Check if marks are valid (0-100)"""
    try:
        marks_float = float(marks)
        if 0 <= marks_float <= 100:
            return True, marks_float
        else:
            return False, None
    except ValueError:
        return False, None

def main():
    students = {}
    print("=" * 60)
    print("        STUDENT GRADING SYSTEM")
    print("=" * 60)
    
    # Input number of students
    while True:
        try:
            n = int(input("\nEnter number of students: "))
            if n <= 0:
                print("Number of students must be positive!")
                continue
            break
        except ValueError:
            print("Please enter a valid integer!")
    
    # Input student data
    print("\n" + "-" * 60)
    for i in range(n):
        print(f"\nStudent {i+1}:")
        name = input("Enter student name: ").strip()
        
        while True:
            marks_input = input("Enter marks (0-100): ")
            is_valid, marks = validate_marks(marks_input)
            
            if not is_valid:
                print("❌ Invalid marks! Please enter a number between 0 and 100.")
                continue
            
            students[name] = marks
            break
    
    # Calculate and display results
    print("\n" + "=" * 60)
    print("           RESULTS")
    print("=" * 60)
    
    print(f"\n{'Student Name':<20} {'Marks':<10} {'Grade':<10}")
    print("-" * 60)
    
    total_marks = 0
    topper_name = ""
    topper_marks = -1
    
    for name, marks in students.items():
        grade = get_grade(marks)
        print(f"{name:<20} {marks:<10.2f} {grade:<10}")
        total_marks += marks
        
        # Find topper
        if marks > topper_marks:
            topper_marks = marks
            topper_name = name
    
    # Calculate statistics
    average_marks = total_marks / len(students)
    
    print("-" * 60)
    print(f"\nTotal Students: {len(students)}")
    print(f"Total Marks: {total_marks:.2f}")
    print(f"Average Marks: {average_marks:.2f}")
    print(f"\n🏆 TOPPER: {topper_name}")
    print(f"   Marks: {topper_marks:.2f}")
    print(f"   Grade: {get_grade(topper_marks)}")
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()

