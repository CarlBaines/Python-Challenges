import time
def welcome():
    name = input("Please enter your name ")
    print("Welcome " + name + ", to the spongebob decision tree!")
    time.sleep(1)
    print("Your first question is...")
welcome()

time.sleep(1)
q1 = input("Is your character a copepod? ")
if q1 == "yes" or q1 == "Yes" or q1 == "y":
    print("Your character is Plankton")
elif q1 == "no" or q1 == "No":
    q2 = input("Does your charater hate Spongebob? ")
elif q2 == "yes" or q2 == "Yes":
    print("Your character is Squidward")
elif q2 == "no" or q2 == "No":
    q3 = input("Does your character have an obsession with money? ")
elif q3 == "yes" or q3 == "Yes":
    print("Your character is Mr Krabs")
elif q3 == "no" or q3 == "No":
    q4 = input("Is your character a scientist? ")
elif q4 == "yes" or q4 == "Yes":
    print("Your character is Sandy")
elif q4 == "no" or q4 == "No":
    q5 = input("Is your character a sponge? ")
elif q5 == "yes" or q5 == "Yes":
        print("Your character is Spongebob")
elif q5 == "no" or q5 == "No":
        print("Your character is Patrick")
else:
    print("404 Error")
    
    

    



  
