import random
import os
import time

def game_intro():
    print("="*40)
    print("🎲 Welcome to the Number Guessing Game! 🎲")
    print("="*40)
    time.sleep(1)
    print("\nInstructions:")
    print("1. I will pick a random number between 1 and 100.")
    print("2. Your job is to guess the number.")
    print("3. After each guess, I'll tell you if your guess is too high or too low.")
    print("4. Try to guess it in as few attempts as possible!\n")
    print("="*40)
    input("Press Enter to start the game...")
    os.system('cls' if os.name == 'nt' else 'clear')

def clear_screen():

    if os.name == 'nt':  
        input("Press Enter to continue...") 
        os.system('cls')  

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    attempts = 0

    while guess != random_number:
        
        try:
            guess = int(input(f"Guess a Number between 1 and {x}: "))
            attempts += 1

            if guess < random_number:
                print("Sorry guess again. Too low!")
            elif guess > random_number:
                print("Sorry guess again. Too high!")
        except ValueError: 
            print("Please choose a number!")

    print(f"Yay, you've guessed the number {random_number} correctly in {attempts} attempts!. Congratulations!")

game_intro()

while True:
    guess(10)  

    while True:

        play = input("Do you want to play again? (Y/N): ").lower()
        if play == "y":
            clear_screen()
            break

        elif play == "n":
            print("Thank you for Playing! Have a Nice Day!")
            exit() 
        else:
            print("Invalid input! Please type Y or N only.")
            clear_screen()
            continue