import random
import time
import os

def clear_screen():
    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')


def introduction():
    print("🎲🔥 WELCOME TO ROLL THE DICE! 🔥🎲")
    time.sleep(0.8)
    print("Two rivals enter the arena...")
    time.sleep(0.8)
    print("You 🧑 vs The Computer 🤖")
    time.sleep(0.8)
    print("\nEach of you will roll TWO dice.")
    time.sleep(0.7)
    print("The dice will decide your fate...")
    time.sleep(0.7)
    print("⚡ Higher total WINS the round! ⚡")
    time.sleep(0.8)
    print("\nBrace yourself.")
    time.sleep(0.6)
    print("Let the dice roll! 🎉🎲\n")


def roll_dice():
    while True:
        try:
            ask = input("Do you want to roll the dice? (y/n): ").lower()
            if ask == 'y':
                print("Rolling the dice...")
                time.sleep(1)
                dice1 = random.randint(1, 6)
                dice2 = random.randint(1, 6)
                total = dice1 + dice2
                print(f'You rolled a {dice1} and a {dice2}. \nTotal: {total}\n')
                time.sleep(1)
            elif ask == 'n':
                print("Maybe next time!")
                exit()
        except ValueError:
                print("Invalid input! Please enter y or n.\n")

        print("Computer is rolling the dice...")
        time.sleep(1)
        computer_dice1 = random.randint(1, 6)
        computer_dice2 = random.randint(1, 6)
        computer_total = computer_dice1 + computer_dice2
        print(f'Computer rolled a {computer_dice1} and a {computer_dice2}. \nTotal: {computer_total}\n')

        if total == computer_total:
            return "It's a tie!"
        time.sleep(0.5)

        if is_user_winner(total, computer_total):
            return "You won!"
        time.sleep(0.5)

        return "You lost!"
    time.sleep(0.5)

def is_user_winner(user_total, computer_total):
    return user_total > computer_total

while True:
    introduction()
    print(roll_dice())

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
            print("Invalid input! Please enter y or n.\n")
            clear_screen()