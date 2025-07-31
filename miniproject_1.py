# To guess a number between 1 to 100
import random 
target = random.randint(1,100)
print("Guess a number between 1 to 100")
while True: 
    user_choice = input("Enter your guess or write 'Quit' to exit game: ")
    if (user_choice.strip().lower() == "quit"):
        break 
    else: 
        user_choice = int(user_choice)
        if (user_choice == target):
            print("---SUCCESS!---")
            break
        elif (user_choice<target):
            print("Guess too Small. Guess Again!")
        else: 
            print("Guess too Big, Guess Again!")
print("-------GAME OVER-------")