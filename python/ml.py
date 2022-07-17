import matplotlib.pyplot as plt
import random

while True:
    for i in range(12):
        num = random.randrange(1, 100)
        print(num ++ 12)
        x = num
        y = num
        plt.scatter(x, y)
        plt.show()
