import random
import time
import os

def clear_screen():
    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')

def play():
    while True:
        user = input("Make your move! [r = Rock | p = Paper | s = Scissors]: ").lower()

        if user in ['r', 'p', 's']:
            break
        else:
            print("Invalid input! Please enter r, p, or s.\n")
            clear_screen()

    print("\nRock...")
    time.sleep(0.7)
    print("Paper...")
    time.sleep(0.7)
    print("Scissors!")
    time.sleep(0.5)

    computer = random.choice(['r', 'p', 's'])

    print(f"\nYou chose: {convert(user)}")
    print(f"Computer chose: {convert(computer)}\n")

    if user == computer:
        return "It's a tie!"

    if is_win(user, computer):
        return "You won!"

    return "You lost!"

def is_win(player, opponent):
    return (
        (player == 'r' and opponent == 's') or
        (player == 's' and opponent == 'p') or
        (player == 'p' and opponent == 'r')
    )

def convert(choice):
    if choice == 'r':
        return "Rock"
    elif choice == 'p':
        return "Paper"
    else:
        return "Scissors"

while True:
    print(play())

    while True:
        again = input("\nDo you want to play again? (y/n): ").lower()

        if again == 'y':
            print()
            clear_screen()
            break
        elif again == 'n':
            print("\nThanks for playing! 👋")
            exit()
        else:
            print("Invalid input! Please enter y or n.")
            clear_screen()