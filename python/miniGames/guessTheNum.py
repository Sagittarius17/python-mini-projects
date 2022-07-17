import random
from colorama import Fore, init, Back

#number guessing
init()

while True:
    for i in range(10):
        num = random.randint(1, 10)
        user = int(input("Guess the number -->  "))
        if user == num:
            print(Fore.GREEN + f"Correct guess! it's {num}.")
        if user != num:
            print(Fore.RED + f"Incorrect guess! it's {num}." + Fore.RESET)
            continue;

        play_again = str(input("want to play again? 'y' or 'n'"))
        if play_again == "y":
            continue
        if play_again == user -- "n":
            break