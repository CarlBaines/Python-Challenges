import time #imports

a = 0      #sets values
b = 1
count = 0
total = 0

x = int(input("Please enter the number of places you want to calculate the Fibonacci Sequence to "))     #takes a user input.

if x <= 10:  #ensures that the user input can only be up to 10 places.
    time.sleep(.5)
    q = -1          #helps in calculating the sum of the numbers in the sequence, later in the program
    print("\n" + "This is the Fibonacci Sequence up to " + str(x) + " places:")

    for i in range(x): #loops for the number of places inputted by the user.
        time.sleep(.4)
        print(a)
        count = a    #count is a temporary variable.
        a = b        #first step of the finobacci sequence.
        b = count + b #adds the total of the first number onto the second to get the next term.
        total = b
        total += q   #calculates the sum of the numbers in the seqeunce.

else:
    x = int(input("Please enter the number of places you want to calculate the Fibonacci Sequence to ")) #repeatedly asks for another user input until it meets the suitable condition.

print("The sum of the numbers in the sequence is: " + str(total))





