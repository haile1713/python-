import random

user_choice=int (input("whats your choice : 0 f0r Rock , 1 for paper and 2 for scissors"))
if user_choice >=3 or user_choice<0:
    print ("invalid number")
else:
    comp_choice = random.randint(0,2)
    print("computer chose:")
    print(comp_choice)
    if user_choice == comp_choice:
        print("Its a tie!!")
    elif user_choice==0 and comp_choice == 2:
        print("you win!!")
    elif user_choice==2 and comp_choice ==0:
        print("you lose!!")
    elif user_choice < comp_choice:
        print("you lose!!")
    elif user_choice > comp_choice:
        print("you win!!")
