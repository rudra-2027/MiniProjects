def report():
    # Open the grades.txt file in read mode
    with open("grades.txt", 'r') as f1:
        file1 = f1.readlines()

    data = []  # Subject: English, Score: 80, Grade: B
    record = []

    # Input validation for roll number
    while True:
        try:
            roll = int(input("Enter the student roll number: "))
            break
        except ValueError:
            print("Please enter a valid roll number.")

    found = False
    for i in range(1, len(file1),5):
         if file1[i] == f'Student Roll Number: {roll}\n':
            found = True
            print("Record Found")
            # Printing report card
            heading = "Report Card"
            line_length = 40
            e = (line_length - len(heading) - 2) // 2

            print("=" * (line_length - 1))
            print('|' + "=" * e + heading + "=" * e + "|")
            print("=" * (line_length - 1))
            file1=file1[i].strip("\n")
            # file2=file1[i-1].strip("\n")
            print(file1)
            print(file1[i-1].strip().split(":-")[1])
            print('|'+file1[i-1]+''*(line_length-len(file1[i]))+'|')
            print(file1[i])
            break
            


            for i in range(0, len(file1),5):
                if file1[i] == f'Student Roll Number: {roll}\n':
                    record.append(file1[i].strip("\n"))
                    print(file1[i-1])
                    print(file1[i])
                    break
            print(record)
            for i in range(2, len(file1)):
                data.append(file1[i].strip('\n'))

            # Extracting final grades
            finall = data[-2:]
            data = data[:-2]

            # Filter data for the first 5 subjects
            data_for_roll = [subject for subject in data if f"Roll Number: {roll}" in subject][:5]

            
            for i in record:
                key, value = i.split(":")
                padding = 1
                padding_right = line_length - len(key) - len(value) - 5 - padding
                print(f'| {key.strip()} : {value.strip()} {" " * padding_right}|')
            print("=" * (line_length - 1))
            print("|  Subject Name    |  Score  |  Grade |")

            # Calculate maximum subject name length for formatting
            max_length = max(len(subject.split(': ')[1]) for subject in data_for_roll)

            for subject_info in data_for_roll:
                subject, score, grade = subject_info.split(', ')
                s_n = subject.split(': ')[1]
                s_p = max_length - len(s_n)
                print(f'| {s_n}{" " * s_p} | {score.split(": ")[1]} | {grade.split(": ")[1]} |')
            print('=' * (line_length - 1))

            # Printing final grades
            for i in finall:
                for j in i.split(', '):
                    print(f'| {j}{" " * (line_length - len(j) - 3)} |')
            print('=' * (line_length - 1))
            break

    if not found:
        print("Record not found for the provided roll number.")

# Call the function to generate the report
report()
