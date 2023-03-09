from random import choice, randint, sample      #imports
import time

numbers = ['0','1','2','3','4','5','6','7','8','9']  #array used to generate random numbers from.

num1 = choice(numbers)

num2 = choice(numbers)         #generates four random numbers

num3 = choice(numbers)

num4 = choice(numbers)

time.sleep(.5)
print("The numbers in the pin code are: " + num1, num2, num3, num4)    #outputs the numbers that make up the pin code.
print("-------------------------------------------")

pinnumbers = [num1, num2, num3, num4]   #puts the numbers in a seperate array.

sequence = sample(pinnumbers, len(pinnumbers))     #makes a sequence out of the numbers to make the 'real' pin code.
time.sleep(.5)
print("The actual pin code is " + str(sequence))



