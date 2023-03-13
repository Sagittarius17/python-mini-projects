import pyautogui as pg

while True:
    q1 = pg.confirm("1) Who was the 1st Prime Minister of India?", buttons = ["a : Subhash Chandra Bose", 
                                                                              "b : Jawaharlal Nehru", 
                                                                              "c : Mahatma Gandhi", 
                                                                              "d : Rabindranath Tagore"])
    q1_right = "b : Jawaharlal Nehru"
    if q1 != q1_right:
        print(pg.confirm('Wrong answer'))
    else:
        print(pg.confirm('Correct answer'))
        
    
    q2 = pg.confirm("2) Who created python programming language?", buttons = ["a : James Gosling",
                                                                              "b : Dennis MacAlistair Ritchie", 
                                                                              "c : Guido van Rossum", 
                                                                              "d : Linus Benedict Torvalds"])
    q2_right = "c : Guido van Rossum"
    if q2 != q2_right:
        print(pg.confirm('correct answer'))
    else:
        print(pg.confirm('Correct answer'))
        
        
    q3 = pg.confirm("3) Which one is a crypto currency build on blockchain?", buttons = ["a : Bitcoin", 
                                                                                                 "b : Ethereum", 
                                                                                                 "c : polygon", 
                                                                                                 "d : All above"])
    q3_right = "d : All above"
    if q3 != q3_right:
        print(pg.confirm('correct answer'))
    else:
        print(pg.confirm('Correct answer'))
        
        
    q4 = pg.confirm("4) CS:GO(first person shooter game) came out in which year?", buttons = ["a : 2012", 
                                                                                              "b : 2002",
                                                                                              "c : 2015", 
                                                                                              "d : 2010"])
    q4_right = "a : 2012"
    if q4 != q4_right:
        print(pg.confirm('correct answer'))
    else:
        print(pg.confirm('Correct answer'))
        
        
    q5 = pg.confirm("5) Which one is a redioactive element?", buttons = ["a : H2SO4",
                                                                         "b : NH3", 
                                                                         "c : Gold", 
                                                                         "d : Corium"])
    q5_right = "d : Corium"
    if q5 != q5_right:
        print(pg.confirm('correct answer'))
    else:
        print(pg.confirm('Correct answer'))
    break
        
