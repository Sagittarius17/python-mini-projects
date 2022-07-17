import pyautogui as pg

while True:
    user = pg.confirm("Are you dumb?",  buttons = ["Yes", "No"])
    if user != "Yes":
        continue
    else:
        pg.confirm("I knew it...", buttons = ["close"])
        break