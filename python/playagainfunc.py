def PlayAgain():
    """ask if player wants to play again"""
    print("{:^40s}".format("Do you want to play again? y or n ?"))
    again = str(input("{:>20s}".format("")))
    again = again.lower()

    # when it is not the case that "y" XOR "n"
    while not ((again != "y" and again == "n") or (again == "y" and again != "n")):
        print("{:^40s}".format("Please enter y or n"))
        print("{:^40s}".format("Do you want to play again? y or n ?"))
        again = str(input("{:>20s}".format("")))
        again = again.lower()

    if again == "y":
        return True
    elif again == "n":
        return False 
    
PlayAgain()