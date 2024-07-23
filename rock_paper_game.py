import random

# Display the options
print("Rock, Paper, Scissors Game")
print("0: Rock")
print("1: Paper")
print("2: Scissors")

# Get user's choice
user_choice = int(input("Enter your choice (0, 1, or 2): "))

# Generate computer's choice
computer_choice = random.randint(0, 2)
print("Computer chose:", computer_choice)

# Determine the winner
if user_choice == computer_choice:
    print("It's a Draw!")
elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
    print("You Win!")
else:
    print("You Lose!")
