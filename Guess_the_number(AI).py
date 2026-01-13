import random
import os
import time

def game_intro():
    print("="*40)
    print("🎲 Welcome to the Number Guessing Game! 🎲")
    print("="*40)
    time.sleep(1)
    print("\nInstructions:")
    print("1. You, the player, will pick a random number between 1 and 100.")
    print("2. Computer's job is to guess the number.")
    print("3. After each guess, You will tell if the Computer's guess is too high or too low.")
    print("4. Let them try to guess it in as many attempts as possible!\n")
    print("="*40)
    input("Press Enter to start the game...")
    os.system('cls' if os.name == 'nt' else 'clear')

def clear_screen():
    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    attempts = 0

    while feedback != "c":
        if low > high:
            print("Something went wrong. Please be honest with your answers!")
            return

        guess = random.randint(low, high)
        attempts += 1

        feedback = input(
            f"Is {guess} too high (H), too low (L), or correct (C)? "
        ).lower()

        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        elif feedback == "c":
            pass
        else:
            print("Invalid input. Please enter H, L, or C.")

    print(f"\nComputer guessed the number {guess} correctly in {attempts} attempts!")

game_intro()

while True:
    computer_guess(100)

    while True:
        play = input("\nDo you want to play again? (Y/N): ").lower()

        if play == "y":
            clear_screen()
            break
        elif play == "n":
            print("Thank you for Playing! Have a Nice Day!")
            exit()
        else:
            print("Invalid input! Please type Y or N only.")
