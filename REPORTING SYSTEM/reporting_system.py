def add():
    with open("Record.txt", 'r') as f:
        l = f.readlines()
    r=[]
    for i in range(2,len(l),5):
        r.append(l[i])

    while True:
        name = input("Enter the name of the student: ")
        roll = input("Enter the roll number of the student: ")
        section = input("Enter the section of the student: ")
        while True:
            percentage = input("Enter the percentage of the student (0-100): ")
            try:
                percentage = float(percentage)
                if 0 <= percentage <= 100:
                    break
                else:
                    print("Percentage must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid percentage.")

        if f'Roll Number:- {roll}\n' in r:  
            print("Roll number already exists. Please enter a different roll number.")
        else:
            break

    with open("Record.txt", 'a') as f:
        f.write("\nName of the student:- " + name)
        f.write("\nRoll Number:- " + roll)
        f.write("\nSection:- " + section)
        f.write("\nPercentage:- " + str(percentage))
        f.write("\n----------------------------------")

    re()  


def re():
    f=open("Record.txt",'r')
    a=f.read()
    print()
    print(a)
    f.close()


def modify():
    
    f=open("Record.txt","r")
    s=f.readlines()
    
    found = False
    ch=input("Enter the name of student to modify ")
    
    for i in range(len(s)):
        if "Name of the student:- "+ ch in s[i]:
            
            roll = input("Enter the roll number of the student ")
            section = input("Enter the section of the student ")
            percentage = input("Enter the percentage of the student ")
            
            
            s[i+1] = "Roll Number:- " + roll + '\n'
            s[i+2] = "Section:- " + section + '\n'
            s[i+3] = "Percentage:- " + percentage + '\n' 
            
            found = True
            break
        
    if found:
        with open("Record.txt","w") as f:
            f.writelines(s)
            print("Record Is modified!")
    else:
        print("Student not found!")
#--------------------------------------------------------------------------
def search():
    f=open('Record.txt','r')
    r=f.readlines()
    while True:
        try:
            roll=int(input("Enter the roll number "))
            break
        except ValueError:
            print("Please Enter Valid Roll Number")
    found = False
    for i in range(2,len(r),5):
        if r[i] == f'Roll Number:- {roll}\n':
            found=True
            print("Record Found\n   ")
            print("Name:",r[i-1].strip().split(":-")[1])
            print("Roll Number:",r[i].strip().split(":-")[1])
            print("Section:",r[i+1].strip().split(":-")[1])
            print("Percentage:",r[i+2].strip().split(":-")[1])  
            break
    if not found:
        print("Roll Number Not Found")
#------------------------------------------------------------------------------
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

def view_records():
    try:
        with open('grades.txt', 'r') as file:
            print("Student Records:")
            print(file.read())
    except FileNotFoundError:
        print("No records found.")

def save(name,roll, subjects, final, percentage):
    with open('grades.txt', 'a') as file:
        file.write(f"Student Name: {name}\n")
        file.write(f"Student Roll Number: {roll}\n")
        for subject, score, grade in subjects:
            file.write(f"Subject: {subject}, Score: {score}, Grade: {grade}\n")
        file.write(f"Final Grade: {final},Percentage: {percentage}%\n\n")
        # file.write(f"\n")

def grade():
    while True:
        try:
            roll = int(input("Enter the roll number: "))
            break
        except ValueError:
            print("Please Enter a Valid Roll Number")

    with open("Record.txt", 'r') as f:
        l = f.readlines()
    r = []
    
    for i in range(2, len(l), 5):
        r.append(l[i])
        
    if f'Roll Number:- {roll}\n' in r:
        found = False
        student_name = ""
        for i in range(2,len(l),5):
            if l[i] == f'Roll Number:- {roll}\n':
                found = True
                student_name = l[i-1].strip().split(":-")[1]
                print("Name:", student_name)
                break
        subjects = []
        total_score = 0
        no_of_subjects = int(input("Enter the number of subjects: "))
        for i in range(no_of_subjects):
            subject_name = input(f"Enter the name of subject {i+1}: ")
            while True:
                try:
                    subject_score = int(input(f"Enter the score of {subject_name}: "))
                    if 0 <= subject_score <= 100:
                        break
                    else:
                        print("Score must be between 0 and 100.")
                except ValueError:
                    print("Please Enter a Valid Score")
            subjects.append((subject_name, subject_score,calculate_grade(subject_score)))

        total_score = sum(score for _, score,_ in subjects)
        avreage = total_score / no_of_subjects

        if avreage < 0 or avreage > 100:
            print("Average score must be between 0 and 100")
        else:
            final = calculate_grade(avreage)
            print(f"The student's final grade is: {final}")

            percentage = (total_score / (no_of_subjects )) 

            save(student_name,roll, subjects, final, percentage)
    else:
        print("Roll Number not found. Please Add the Roll Number First")


#--------------------------------------------------------------------------------
def report():
    while True:
        try:
            roll = int(input("Enter the student roll number: "))
            break
        except ValueError:
            print("Please enter a valid roll number.")
    with open("grades.txt", 'r') as f1:
        file1 = f1.readlines()

    found = False
    for i in range(1, len(file1)+1, 9):
        if f'Student Roll Number: {roll}\n' in file1[i]:
            found = True
            print("Record Found")

            record1= file1[i-1].strip()
            record = file1[i].strip()
            
            data = [file1[j].strip() for j in range(i+1, i+6)]

            heading = "Report Card"
            line_length = 40
            e = (line_length - len(heading) - 2) // 2

            print("=" * (line_length - 1))
            print('|' + "=" * e + heading + "=" * e + "|")
            print("=" * (line_length - 1))
            print('|'+record1+' '*(line_length - len(record1)-3)+'|')
            print('|'+record+' '*(line_length - len(record)-3)+'|')  
            print("=" * (line_length - 1))
            print("|  Subject Name    |  Score  |  Grade |")
            total_marks = 500
            total_obtained_marks = 0
            for line in data:
                subject, score, grade = line.split(', ')
                subject_name = subject.split(': ')[1]
                score_value = score.split(': ')[1]
                total_obtained_marks+=int(score_value)
                grade_value = grade.split(': ')[1]
                print(f"| {subject_name:<16} | {score_value:>7} | {grade_value:>6} |")
            print("=" * (line_length - 1))
            
            
            percentage = (total_obtained_marks / total_marks) * 100
            if percentage >= 90:
                final_grade = 'A'
            elif percentage >= 80:
                final_grade = 'B'
            elif percentage >= 70:
                final_grade = 'C'
            elif percentage >= 60:
                final_grade = 'D'
            else:
                final_grade = 'F'
            a = f"Percentage: {percentage:.2f}%"
            b = f"Final Grade: {final_grade}"
            print('|'+f"Final Grade: {final_grade}"+' '*(40-len(b)-3)+'|')
            print('|'+f"Percentage: {percentage:.2f}%"+' '*(40-len(a)-3)+'|')
            
            
            print("=" * (line_length - 1))
            break  

    if not found:
        print("Record not found for the provided roll number.")

    




        
def main():
    while True:
        print("\nMenu:")
        print("1. Add a record")
        print("2. Read all records")
        print("3. Modify a record")
        print("4. Search Record")
        print("5. For adding result")
        print("6. Report Card")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add()
        elif choice == '2':
            re()
        elif choice == '3':
            modify()
        elif choice == '4':
            search()
        elif choice == '5':
            grade()
        elif choice == '6':
            report()
        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main()