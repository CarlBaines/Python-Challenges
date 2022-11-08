import time
def welcome():
  name = input("Please enter your name ")
  time.sleep(1)
  print("Welcome " + name + ", to the dinosaur decision tree! You need to run if the dinosaur identified is a carnivore!")
  time.sleep(1)
  print("Your first question is...")
welcome()

time.sleep(1)
q1 = input("Is your dinosaur a carnivore or a herbivore? ")
if q1 == "carnivore" or q1 == "c":
    q2c = input("Does your dinosaur have feathers? ")
elif q2c == "yes" or q2c == "y":
    print("Your dinosaur is a velociraptor, a carnivore, you need to run!")
elif q2c == "no" or q2c == "n":
    q3c = input("Does your dinosaur prey on velociraptors? ")
elif q3c == "yes" or q3c == "y":
    print("Your dinosaur is a T-Rex, a carnivore, you need to run!")
elif q3c == "no" or q3c == "n":
    q4c = input("Is your dinosaur a fast swimmer? ")
elif q4c == "yes" or q4c == "y":
    print("Your dinosaur is a spinosaurus, a carnivore, you need to run!")
elif q4c == "no" or q4c == "n":
    q5c = input("Does your dinosaur have a total of 33 teeth? ")
elif q5c == "yes" or q5c == "y":
    print("Your dinosaur is a dilophosaurus, a carnivore, you need to run!")
elif q5c == "no" or q5c == "n":
    print("I don't know what dinosaur that is")
elif q1 == "herbivore" or q1 == "h":
    q1h = input("Is your dinosaur a high feeder? ")
elif q1h == "yes" or q1h == "y":
    print("Your dinosaur is a brachiosaurus, you don't need to run.")
elif q1h == "no" or q1h == "n":
    q2h = input("Is your dinosaur the longest known one? ")
elif q2h == "yes" or q2h == "y":
    print("Your dinosaur is a diplodocus, you don't need to run!")
elif q2h == "no" or q2h == "n":
    print("I don't know what dinosaur that is")
else:
    print("I don't know what that dinosaur is")
    
        
                                                          
      

  