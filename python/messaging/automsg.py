from async_timeout import timeout
import pyautogui as auto
import time
import random

words = ["hi", "hey", "hola", "hello"]
for i in range(200):
    auto.write(random.choice(words))
    auto.write("\n")
    if i == 200:
        break;
    time.sleep(0.1)
            