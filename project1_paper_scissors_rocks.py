#wap for rock,paper, scissors
import random
user_choice = int(input("enter your choice : type 0 for rock , type 1 for paper, type 2 for scissors"))

if user_choice >=3 or user_choice < 0:
    print("not allowed")
else:
    computer_choice =random.randint(0,2)
    print("computer chose")
    print(computer_choice)


    if computer_choice == user_choice:
        print("It's A Draw")
    elif computer_choice == 0 and user_choice == 2:
        print("you lose")
    elif user_choice == 0 and computer_choice == 2:
        print("you win")
    elif computer_choice>user_choice:
        print("You Lose")
    else :
        print("you won")

