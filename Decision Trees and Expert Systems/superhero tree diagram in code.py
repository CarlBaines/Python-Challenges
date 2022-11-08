import time
def welcome():
    name = input("Please enter your name ")
    print("Welcome " + name + ", to the superhero decision tree!")
    time.sleep(1)
    print("Your first question is...")
welcome()

time.sleep(1)
q1 = input("Does your superhero have an element of green in their costume? ")
if q1 == "yes" or q1 == "Yes" or q1 == "y":
    q2 = input("Does your superhero have superhuman strength? ")
    if q2 == "yes" or q2 == "Yes" or q2 == "y":
        print("Your superhero is She-Hulk")

elif q1 == "no" or q1 == "No" or q1 == "n":
    q3 = input("Is your superhero part of the DC Universe? ")
    if q3 == "yes" or q3 == "Yes" or q3 == "y":
        print("Your superhero is Batman")

elif q2 == "no" or q2 == "No" or q2 == "n":
    q4 = input("Does your superhero have a clown-like appearance? ")
    if q4 == "yes" or q4 == "Yes" or q4 == "y":
        print("Your superhero is the Joker")

elif q3 == "no" or q3 == "No" or q3 == "n":
    q5 = input("Does your superhero have a unibeam? ")
    if q5 == "yes" or q5 == "Yes" or q5 == "y":
        print("Your superhero is Tony Stark/Iron Man")

else:
    print("404 error")


