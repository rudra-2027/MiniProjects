BJP=0
CONG=0
NORMAL=0
NON=0
while True:
    user_input = input("Do you want to continue? (y/n): ")
    
    if (user_input == 'y' or user_input == 'Y'):
        name=input("Enter the Your name:- ")
        age=int(input("Enter Your Age:- "))
        
        if age>=18:
            print("\nYou Can Vote")    
            print("\n1. FOR BJP")
            print("2. FOR CONGRESS")
            print("3. FOR NORMAL")
            print("4. FOR NONE")
            choice = input("\nEnter Your Choice ")
            # choice=int(choice)
            if('0'<=choice<='9'):
                if(choice== '1'):
                    print("You Choose BJP")
                    BJP+=1
                elif(choice == '2'):
                    print("You Choose CONGRESS")
                    CONG+=1
                elif(choice == '3'):
                    print("You Choose NORMAL")
                    NORMAL+=1
                elif(choice == '4'):
                    print("You Choose NONE")
                    NON+=1
                else:
                    print("YOU CHOOSE WRONG OPTION")
            else:
                print("This Is Not A Valid Input")
        else:
            print("\nYou Cannot Vote ")
        print("Continuing...")
    elif (user_input == 'n' or user_input == 'N'):
        
        print("\nExiting loop.")
        print("\n TOTAL VOTE COUNTS")
        print("\nBJP = ", BJP)
        print("CONGRESS = ", CONG)
        print("NORMAL = ", NORMAL)
        print("NONE = ", NON)
        print()
         
        if(BJP>CONG and BJP>NORMAL and BJP>NON):
            print("BJP WINS")
        elif(CONG>BJP and CONG>NORMAL and CONG>NON):
            print("CONGRESS WINS")
        elif(NORMAL>BJP and NORMAL>CONG and NORMAL>NON):
            print("NORMAL WINS")
        elif(NON>BJP and NON>CONG and NON>NORMAL):
            print("NONE WINS")
        else:
            if(BJP == 0 and CONG == 0 and NORMAL == 0 and NON == 0):
                print("NO ONE GET VOTE ")
            elif (BJP == CONG and BJP == NORMAL and BJP == NON):
                print("THIS IS A TIE BETWEEN ALL PARTY") 
            
            elif(BJP==CONG !=0):
                print("ITS TIE BETWEEN BJP AND CONGRESS")
            elif(BJP == NORMAL !=0):
                print("ITS TIE BETWEEN BJP AND NORMAL")
            elif(BJP == NON !=0):
                print("ITS TIE BETWEEN BJP AND NON")
            elif(CONG == NORMAL !=0):
                print("ITS TIE BETWEEN CONGRESS AND NORMAL")
            elif(CONG == NON !=0):
                print("ITS TIE BETWEEN  CONGRESS AND NON")
            elif(NORMAL ==  NON !=0 ):
                print("ITS TIE BETWEEN NORMAL AND NON")
            else:
                print("Nothing Happen")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
