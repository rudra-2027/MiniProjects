import random
def computer():
    while True:
        n=input("Enter the starting range for guessing the number ")
        n1=input("Enter the ending range for guessing the number ")
        if (n.isdigit() and n1.isdigit()):
            n=int(n)
            n1=int(n1)
            check=random.randint(n,n1)
            return check            
        else:
            print("Please Enter Numeric Value")
            continue
c = computer()
# print(c)
while True:
    user = input("Enter your number ")
    if user.isdigit():
        user = int(user)
        if user>c:
            print("Your Enter Value is Greater then Computer Choice Value")
        elif user<c:
            print("Your Enter Value is Smaller then Computer Choice Value")
        else:
            print("You Guess the Correct number")
            print(f"The number is {user}")
            break
    else:
        print("Pls Enter Numeric value")
        continue

