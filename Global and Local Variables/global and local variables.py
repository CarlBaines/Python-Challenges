import time

global pr1 #global variable (outside function). Global variables can be called.
pr1 = input("Enter something ")
def printgl():
    print('\nInside the function')
    print(pr1 + ", this is a global variable")
    time.sleep(1)
    print('\nOutside the function')
    pr2 = input("Enter something ") #local variable (inside function)
    print(pr2 + ", this is a local variable")
printgl()

#The main differences between global and local variables is that global variables permenantly assign data to a variable whereas local variables only temporarily store data as they can be changed. Furthermore, global variables have to be called outside functions, whereas local variables have to be called inside the function.


