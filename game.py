import random

# Mapping choices to numerical values
yourdict = {"s": 1, "w": -1, "g": 0}
reversedict = {1: "snake", -1: "water", 0: "gun"}

print("Welcome to Snake-Water-Gun Game!")
print("Enter 's' for Snake, 'w' for Water, 'g' for Gun.")


while True:
    # User input
    youstr = input("Enter your choice: ").strip().lower()

    # Quit condition
    if youstr == "q":
        print("Thanks for playing! bye.")
        break  # Exit the loop

    # Check if user input is valid
    if youstr not in yourdict:
        print("Invalid input! Please enter 's', 'w', or 'g'.")
        continue  # Restart loop

    # Computer randomly selects a choice
    computer = random.choice([-1, 0, 1])
    you = yourdict[youstr]

    print(f"Your choice: {reversedict[you]}, Computer choice: {reversedict[computer]}")

    # Determine the winner
    if computer == you:
        print("Match draw!\n")
    elif (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
        print("You win!\n")
    else:
        print("You lose!\n")
