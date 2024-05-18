def report():
    f=open("Record.txt",'r')
    f1=open("grades.txt",'r')
    file=f.read()
    file1=f1.readlines()
    data=[] #Subject: English, Score: 80, Grade: B
    record=[]
    
    for i in range(0,2):
        record.append(file1[i].strip("\n"))
    # print(record)
    
    for i in range(2, len(file1)):
        data.append(file1[i].strip('\n'))
        # print(data)
    # data=data[:-1]
    finall = []
    for i in range(-1, -3, -1):  # Corrected the range and the direction of iteration
        finall.append(data[i])

    # Remove the last two elements from the data list
    data = data[:-2]
    finall=finall[1:2:1]

    # print(data)
    # print(finall) 
    
    
    heading = "Report Card"
    line_length = 40
    
    e = (line_length - len(heading)-2) // 2
    
    print("="*(line_length-1))
    print('|'+"=" * e + heading + "=" * e + "|")
    print("="*(line_length-1))
    for i in record:
        i = i.strip()  
        key, value = i.split(":") 
        padding = 1  
        padding_right = line_length - len(key) - len(value) - 5 - padding  
        print('|' + ' ' * padding + key + ': ' + value + ' ' * padding_right + '|')
    print("="*(line_length-1))
    print("|  Subject Name    |  Score  |  Grade |")
    r = []
    for i in data:
        subject, score, grade = i.split(', ')
        r.append(subject)
        r.append(score)
        r.append(grade)
    print(r)
    corr = []
    for i in r:
        i=i.split()
        corr.append(i[1])
    comp=[]
    for i in 
    for i in corr:
        subject,score,grade=i.split(', ')
        padding_subject = 1
        padding_score = 8 - len(score)
        padding_grade = 6 - len(grade)
        print('|' + ' ' * padding_subject + subject + ' ' * (12 - len(subject)) + '|' + ' ' * padding_score + score + ' ' * (7 - len(score)) + '|' + ' ' * padding_grade + grade + ' ' * (7 - len(grade)) + '|')

        

    
    
report()