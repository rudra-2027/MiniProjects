import random
user=0
computer=0
while True:
    n=int(input("Enter the number (1,6) "))
    if 1<=n<=6:
        user+=n
    else:
        print("Pls Enter in range")
        continue
    a=random.randrange(1,7)
    computer+=a
    print('User Input ',n)
    print('Computer Input ',a)
    choice = input("press e for exit and press any key  for continue ")
    if choice.lower() == 'e':
        break
print("Total Of User ",user)
print("Total OF Computer ",computer)
if(user>computer):
    print("User Wins")
else:
    print("Computer Wins")