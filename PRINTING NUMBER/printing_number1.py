print("=======================")
print("WELCOME TO MINI PROJECT")
print("=======================")

print("\n1. Click For Forward ") 
print("2. Click For Reverse ")

choice = input("\nEnter Your Choice ")

if len(choice) == 1 and 48 <= ord(choice) <= 57:  # Check if the input is a single ASCII digit
    choice = int(choice)
    
    if choice == 1 or choice == 2:
        start = input("\nEnter the number from which you want to start: ")
        ending = input("Enter the number at which you want to end: ")
        updation = input("Enter the steps between them: ")
        
        if start.isdigit() and ending.isdigit() and updation.isdigit():
            print("\n1. To Print Output in Row ")
            print("2. To Print Output in Column ")

            option = input("\nEnter Your Choice for Output Format: ")
            
            if option.isdigit():
                option = int(option)
                
                if start > ending:
                    start, ending = ending, start  # Swap values

                if option == 1:
                    for i in range(start, ending + 1, updation):
                        print(i, end=" ")
                elif option == 2:
                    for i in range(start, ending + 1, updation):
                        print(i)
                else:
                    print("You Chose the Wrong Output Format")
            else:
                print("Your Input Value for Output Format is Not a Digit")
        else:
            print("Your Input Values are Not Digits")
    else:
        print("You Chose the Wrong Option")
else:
    print("Your Input Value is Not a Single Digit ASCII Character")
