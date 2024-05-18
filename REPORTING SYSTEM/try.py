def report():
    f = open("Record.txt", 'r')
    f1 = open("grades.txt", 'r')
    
    file1 = f1.readlines()
    print(file1)
    data = []  # Subject: English, Score: 80, Grade: B
    record = []
    while True:
        try:
            roll=int(input("Enter the student roll number "))
            break
        except ValueError:
            print("Please Enter Convert Format of Roll number")
    found = False
    for line in file1:
        print(line)
        if f"Student Roll Number: {roll}\n" in line:
            found = True
            print("Record Found")
            break

    if not found:
        print("Record not found for the provided roll number.")
        return  # Exit the function if record not found
    for i in range(0, 2):
        record.append(file1[i].strip("\n"))

    for i in range(2, len(file1)):
        data.append(file1[i].strip('\n'))

    finall = []
    for i in range(-1, -3, -1):
        finall.append(data[i])

    data = data[:-2]
    finall = finall[1:2:1]

    heading = "Report Card"
    line_length = 40

    e = (line_length - len(heading) - 2) // 2

    print("=" * (line_length - 1))
    print('|' + "=" * e + heading + "=" * e + "|")
    print("=" * (line_length - 1))
    for i in record:
        i = i.strip()
        key, value = i.split(":")
        padding = 1
        padding_right = line_length - len(key) - len(value) - 5 - padding
        print('|' + ' ' * padding + key + ': ' + value + ' ' * padding_right + '|')
    print("=" * (line_length - 1))
    print("|  Subject Name    |  Score  |  Grade |")
    
    max_length = max(len(subject.split(': ')[1]) for subject in data)
    
    for i in data:
        subject, score, grade = i.split(', ')
        s_n = subject.split(': ')[1]
        s_p = max_length - len(s_n)
        print('|    {}{}|   {}    |    {}   |'.format(s_n, ' ' * s_p, score.split(': ')[1], grade.split(': ')[1]))
    print('='*(line_length - 1))

    for i in finall:
        i=i.split(', ')
        for j in i:
            a=len(j)
            # print(a)
            print('|'+j+" "*(line_length-a-3)+'|')
    print('='*(line_length-1))
report()
