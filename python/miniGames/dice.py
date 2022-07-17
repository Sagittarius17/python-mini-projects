import random
from colorama import Fore, init, Back

#roll dice
init()
while True:
    print( '1. Play       2. Exit')
    user = int(input("Type 1 and press enter to start \nTo exit type 2 and press enter \n"))
    if user == 1:
        num = random.randint(1, 6)
        print(Fore.YELLOW + 'It\'s a ===> ' + str(num) + Fore.RESET)
        continue;
    if user == 2:
        print(Fore.YELLOW + "see ya")
        break;
    else:
        break;
