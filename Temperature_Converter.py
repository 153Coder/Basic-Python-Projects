import os
import time

def Introduction():
    print("🌡️🔥 WELCOME TO TEMPERATURE CONVERTER! 🔥🌡️")
    time.sleep(0.8)
    print("Convert temperatures between Fahrenheit and Celsius with ease.")
    time.sleep(0.8)
    print("Let's get started!\n")
    time.sleep(0.6)

def clear_screen():
    input("\nPress Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(0.5)


def convert_temperature(prompt, formula, unit_from, unit_to):
    clear_screen()
    while True:
        try:
            temp = float(input(prompt))
            break
        except ValueError:
            print("❌ Invalid input! Please enter a number.\n")
            clear_screen()
    
    print("\nConverting...")
    time.sleep(2)
    print("Conversion completed!")
    time.sleep(0.5)
    
    result = formula(temp)
    print(f"\n✅ {temp}° {unit_from} is {round(result, 2)}° {unit_to}")
    again()

        
def again():  
    while True:
        again_input = input("\nDo you want to convert another temperature? (y/n): ").strip().lower()
        if again_input == "y":
            clear_screen()
            return
        elif again_input == "n":
            print("\nExiting the Temperature Converter. Goodbye!")
            clear_screen() 
            exit()
        else:
            print("❌ Invalid input! Please enter y or n.")
            clear_screen()

while True:      
    Introduction()
    
    print("\nChoose the option to Convert Temperature:")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    print("3. Exit")
    
    choice = int(input("Enter your choice (1/2/3): "))
    if choice == 1:
        convert_temperature("Enter temperature in Fahrenheit: ",
        lambda f: (f - 32) * 5 / 9,"Fahrenheit","Celsius")
    elif choice == 2:
        convert_temperature("Enter temperature in Celsius: ",
        lambda c: (c * 9 / 5) + 32,"Celsius","Fahrenheit")
    elif choice == 3:
        print("Exiting the Temperature Converter. Goodbye!")
        break