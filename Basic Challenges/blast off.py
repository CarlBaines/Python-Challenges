import time
number = 5
count = 0
while number < 6:
    time.sleep(0.2)
    print (number) 
    number = number - 1
    count = count + 1
    while count == 5:
        print("Blast off")
        quit()

    
 
