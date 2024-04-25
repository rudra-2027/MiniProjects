def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def save_grade_to_file(student_name, score, grade):
    with open('grades.txt', 'a') as file:
        file.write(f"{student_name}: Score = {score}, Grade = {grade}\n")

def view_records():
    try:
        with open('grades.txt', 'r') as file:
            print("Student Records:")
            print(file.read())
    except FileNotFoundError:
        print("No records found.")

def main():
    while True:
        print("\n1. Enter student's score")
        print("2. View records")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                student_name = input("Enter the student's name: ")
                
                score=0
                no=int(input("Enter the number of subject "))
                for i in range(no):
                    subject=int(input(f"Enter the score of first subject {i+1} "))
                    score+=subject
                score = (score)/5
        
                if score < 0 or score > 100:
                    print("Score must be between 0 and 100")
                else:
                    grade = calculate_grade(score)
                    print("The student's grade is:", grade)
                    save_grade_to_file(student_name, score, grade)
                    
            except ValueError:
                print("Invalid input. Please enter a numeric score.")
        elif choice == '2':
            view_records()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
