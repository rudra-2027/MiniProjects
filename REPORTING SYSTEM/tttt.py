def report():
    with open("grades.txt", 'r') as f1:
        file1 = f1.readlines()

    found = False
    for i in range(1, len(file1)+1, 5):
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

# Input validation for roll number
while True:
    try:
        roll = int(input("Enter the student roll number: "))
        break
    except ValueError:
        print("Please enter a valid roll number.")

# Call the function to generate the report
report()
