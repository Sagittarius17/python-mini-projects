import random
import time

#an empty list to append randomly generated numbers
empty = []
while True:
    #checking range
    number = random.randrange(0, 99)
    if number not in empty:
        empty.append(number)
    else:
        pass
    #breaking the loop if the length of the numbers is 99
    if len(empty) == 99:
        break
print(f"final list --> {empty}")

