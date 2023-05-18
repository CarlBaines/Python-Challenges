import time

def checkIfPrime(number):
    for x in range(2, number):
        if (number%x==0):
            time.sleep(1)
            return False
        time.sleep(1)
        return True

    
