import random
def sim():
    start = input("Do you want to roll the dice? ")
    if start == "yes" or start == "y":
        n = random.randint(1,100) 
        print ("You have rolled a " + str(n))
    else:
        print("Goodbye")
        quit()
    rollagain = input("Do you want to roll again? ")
    if rollagain == "yes" or rollagain == "y":
        sim()
    else:
        print("Goodbye")
        quit()
sim()
    

    

