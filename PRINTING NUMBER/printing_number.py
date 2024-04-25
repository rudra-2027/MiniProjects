print("=======================")
print("WELCOME TO MINI PROJECT")
print("=======================")

print(" \n 1. Click For Forward ") 
print(" 2. Click For Reverse ")

choice = input("\n Enter Your Chocie ")


if (choice.isdigit()):  
    choice=int(choice)
    if (choice == 1):
        start = input("\nEnter the number from which you want to start ")
        ending =  input("Enter the number at which you want to end ")
        updation = input("Enter the steps btw them ")
        if start.isdigit() and ending.isdigit() and updation.isdigit():
    
        
            print(" \n 1. To Print Output in Row ")
            print(" 2. To Print Output in Column ")

            option = input("\n Enter Your Above Choice ")
            
            start=int(start)
            ending=int(ending)
            updation=int(updation)
            
            if(option.isdigit()):
                option=int(option)
            
                if(start >  ending):
                
                    new = start
                    start = ending
                    ending = new
                    
                    if (option == 1):
                        for i in range(start,ending+1,updation):
                            print(i,end=" ")
                    elif (option == 2):
                        for i in range(start,ending+1,updation):
                            print(i)
                    else: 
                        print(" You Choose Wrong Option ")
                    
                    
                else:                    
                    if (option == 1):
                        for i in range(start,ending+1,updation):
                            print(i,end=" ")
                    elif (option == 2):
                        for i in range(start,ending+1,updation):
                            print(i)
                    else: 
                        print(" You Choose Wrong Option ")
            else:
                print("Your Input Is Not A Digit")
        else:
            print("Your Input Value Is Not Digit")
            
                        
    elif(choice == 2):
        start = input("\nEnter the number from which you want to start ")
        ending =  input("Enter the number at which you want to end ")
        updation = input("Enter the steps btw them ")
        if start.isdigit() and ending.isdigit() and updation.isdigit():
        
            print(" \n 1. To Print Output in Row ")
            print(" 2. To Print Output in Column ")

            option = input("\n Enter Your Above Choice ")
            
            start=int(start)
            ending=int(ending)
            updation=int(updation)
            
            if(option.isdigit()):
                option=int(option)

        
                if(start <  ending):
                    
                    new = start
                    start = ending
                    ending = new
                    
                    if (option == 1):
                        for i in range(start,ending-1,-updation):
                            print(i,end=" ")
                    elif (option == 2):
                        for i in range(start,ending-1,-updation):
                            print(i)
                    else: 
                        print(" You Choose Wrong Option ")
                    
                else:
                    
                    if (option == 1):
                        for i in range(start,ending-1,-updation):
                            print(i,end=" ")
                    elif (option == 2):
                        for i in range(start,ending-1,-updation):
                            print(i)
                    else: 
                        print(" You Choose Wrong Option ")
            else:
                print("Your Input Value Is Not A Digit")
        else:
            print("Your Input Value Is Not Digit")
    
    else:
        print(" You Choose Wrong Option ")
    
else:
    print("Your Input Value Is Not Digit")
             