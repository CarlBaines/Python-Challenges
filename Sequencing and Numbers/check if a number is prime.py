import time

def checkIfPrime(number):
    for x in range(2, number):
        if (number%x==0):
            time.sleep(1)
            print("This is a not a prime number")
            return False
        time.sleep(1)
        print("This is a prime number")
        return True
print(checkIfPrime(15))
    
