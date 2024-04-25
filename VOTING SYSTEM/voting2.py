print("===========================================================")
print("|-------------------------Welcome-------------------------|")
print("===========================================================")
BJP=0
CONG=0
NORMAL=0
NON=0
while True:
    user_input = input("Do you want to continue? (y/n): ")
    
    if (user_input == 'y' or user_input == 'Y'):
        name=input("Enter the Your name:- ")
        age=input("Enter Your Age:- ")
        if(age.isdigit()):
            age=int(age)
            if age>=18:
                print("==============")
                print("|You Can Vote|")
                print("==============")

                print("--------------------")
                print("|YOU HAVE 3 ATTEMPT|")
                print("--------------------")
                
                print("=================")
                print("|1.    FOR BJP  |")
                print("|2. FOR CONGRESS|")
                print("|3.  FOR NORMAL |")
                print("|4.   FOR NONE  |")
                print("=================")
                
                choice = input("\nEnter Your Choice ")
                if(choice== '1'):
                    print("\n=============================")
                    print("|----Thank You For Voting----|")
                    print("==============================")
                    print("|-------You Choose BJP-------|")
                    print("==============================")
                    BJP+=1
                elif(choice == '2'):
                    print("\n=============================")
                    print("|----Thank You For Voting----|")
                    print("==============================")
                    print("|----You Choose CONGRESS-----|")
                    print("==============================")
                    CONG+=1
                elif(choice == '3'):
                    print("\n=============================")
                    print("|----Thank You For Voting----|")
                    print("==============================")
                    print("|-----You Choose NORMAL------|")
                    print("==============================")
                    NORMAL+=1
                elif(choice == '4'):
                    print("\n=============================")
                    print("|----Thank You For Voting----|")
                    print("=============================")
                    print("|-------You Choose NONE------|")
                    print("==============================")
                    NON+=1
                else:
                    print("==============")
                    print("|You Can Vote|")
                    print("==============")

                    print("--------------------")
                    print("|YOU HAVE 2 ATTEMPT|")
                    print("--------------------")
                    
                    print("=================")
                    print("|1.    FOR BJP  |")
                    print("|2. FOR CONGRESS|")
                    print("|3.  FOR NORMAL |")
                    print("|4.   FOR NONE  |")
                    print("=================")
                    choice = input("\nEnter Your Choice ")
                    
                    if('0'<=choice<='9'):
                        if (choice == '1'):
                            print("\n=============================")
                            print("|----Thank You For Voting----|")
                            print("==============================")
                            print("|-------You Choose BJP-------|")
                            print("==============================")
                            BJP+=1
                        elif(choice == '2'):
                            print("\n=============================")
                            print("|----Thank You For Voting----|")
                            print("==============================")
                            print("|----You Choose CONGRESS-----|")
                            print("==============================")
                            CONG+=1
                        elif(choice == '3'):
                            print("\n=============================")
                            print("|----Thank You For Voting----|")
                            print("==============================")
                            print("|-----You Choose NORMAL------|")
                            print("==============================")
                            NORMAL+=1
                        elif(choice == '4'):
                            print("\n=============================")
                            print("|----Thank You For Voting----|")
                            print("=============================")
                            print("|-------You Choose NONE------|")
                            print("==============================")
                            NON+=1
                        else:
                            print("==============")
                            print("|You Can Vote|")
                            print("==============")

                            print("--------------------")
                            print("|YOU HAVE 1 ATTEMPT|")
                            print("--------------------")
                            
                            print("=================")
                            print("|1.    FOR BJP  |")
                            print("|2. FOR CONGRESS|")
                            print("|3.  FOR NORMAL |")
                            print("|4.   FOR NONE  |")
                            print("=================")
                            choice = input("\nEnter Your Choice ")
                            
                            if('0'<=choice<='9'):
                                if (choice == '1'):
                                    print("\n=============================")
                                    print("|----Thank You For Voting----|")
                                    print("==============================")
                                    print("|-------You Choose BJP-------|")
                                    print("==============================")
                                    BJP+=1
                                elif(choice == '2'):
                                    print("\n=============================")
                                    print("|----Thank You For Voting----|")
                                    print("==============================")
                                    print("|----You Choose CONGRESS-----|")
                                    print("==============================")
                                    CONG+=1
                                elif(choice == '3'):
                                    print("\n=============================")
                                    print("|----Thank You For Voting----|")
                                    print("==============================")
                                    print("|-----You Choose NORMAL------|")
                                    print("==============================")
                                    NORMAL+=1
                                elif(choice == '4'):
                                    print("\n=============================")
                                    print("|----Thank You For Voting----|")
                                    print("=============================")
                                    print("|-------You Choose NONE------|")
                                    print("==============================")
                                    NON+=1
                                else:
                                    print("--------------------")
                                    print("|YOU HAVE 0 ATTEMPT|")
                                    print("--------------------")
                                    
                                    print("-------------------------")                                            
                                    print("| Sorry You Cannot Vote |")
                                    print("-------------------------")
            else:
                print("==================")
                print("|You Cannot Vote |")
                print("==================")
        else:
            print("-------------------------")
            print("|Your Input Is not valid|")
            print("-------------------------")
            
        print('\n------------')
        print("Continuing...")
    elif (user_input == 'n' or user_input == 'N'):
        
        print("\nExiting loop.")
        
        print("=========================")
        print("|   TOTAL VOTE COUNTS   |")
        print("-------------------------")
        print(f"|  BJP    |      {BJP}      |")
        print(f"|CONGRESS |      {CONG}      |")
        print(f"| NORMAL  |      {NORMAL}      |")
        print(f"|  NONE   |      {NON}      |")
        print("=========================")
         
        if(BJP>CONG and BJP>NORMAL and BJP>NON):
            print("\n         ==========")
            print("         |BJP WINS|")
            print("         ==========")
        elif(CONG>BJP and CONG>NORMAL and CONG>NON):
            print("\n      ===============")
            print("      |CONGRESS WINS|")
            print("      ===============")
        elif(NORMAL>BJP and NORMAL>CONG and NORMAL>NON):
            print("\n       =============")
            print("       |NORMAL WINS|")
            print("       =============")
        elif(NON>BJP and NON>CONG and NON>NORMAL):
            print("\n         ===========")
            print("         |NONE WINS|")
            print("         ===========")
        else:
            if(BJP == 0 and CONG == 0 and NORMAL == 0 and NON == 0):
                print("\n      =================")
                print("      |NO ONE GET VOTE|")
                print("      =================")
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
            elif(NORMAL ==  NON !=0):
                print("ITS TIE BETWEEN NORMAL AND NON")
            else:
                print("Nothing Happen")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
