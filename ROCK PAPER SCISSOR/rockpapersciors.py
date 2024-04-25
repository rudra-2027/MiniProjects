import random

while True:
    n = input("Enter your choice (R for Rock, P for Paper, and S for Scissors): ").capitalize()
    if n in ["Rock", "Paper", "Scissors", "R", "P", "S"]:
        pass
    else:
        print("Please enter correct format.")
        continue
    l = ["Rock", "Paper", "Scissors"]
    a = random.choice(l)
    print("Computer chose:", a)
    
    if (a == "Rock" and (n == "Paper" or n == "P")) or (a == "Paper" and (n == "Scissors" or n == "S")) \
        or (a == "Scissors" and (n == "Rock" or n == "R")):
        print("User Wins")
    elif ((n == "Rock"  or n == "R") and (a == "Paper")) or ((n == "Paper" or n == "P") and (a == "Scissors" )) \
        or ((n == "Scissors" or n == "S") and (a == "Rock" )):
        print("Computer Wins")
    else:
        print("It's a tie!")
    
    choice = input("Press 'e' to exit, press any other key to continue: ")
    if choice.lower() == "e":
        break
