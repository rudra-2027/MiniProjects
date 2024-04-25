a=eval(input())
b=eval(input())
operatrion = input("Enter +,-,*,/ ")
if operatrion == '+':
    print(a+b)
elif operatrion == '-':
    print(a-b)
elif operatrion == '*':
    print(a*b)
elif operatrion == '/':
    print(a/b)
else:
    print("Wrong operation")