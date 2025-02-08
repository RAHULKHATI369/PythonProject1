import random


numbers_to_guess= random.randint(1,100)
while True:
    try:
        guess= int(input("Guess a number between 1 and 100: "))

        if guess < numbers_to_guess:
            print("Too low")
        elif guess > numbers_to_guess:
            print("Too high")
        else:
            print("Congratulations, you guessed the number")
            break
    except ValueError:
        print("Sorry, I didn't understand that.")

