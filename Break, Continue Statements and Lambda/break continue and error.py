import time

option = input("What do you want to do? 1. Break 2. Continue 3. Error ")
if option == '1':
    a = 0
    for i in range(8):
        a = a + 2
        time.sleep(1)
        print("i = ", i,"a = ",a)
        if a == 10:
            break
if option == '2':
    s = 0
    for i in range(10):
        s = s + 2
        print("\ni = ", i, "s = ",s)
        time.sleep(1)
        if s == 28:
            continue
        time.sleep(1)
        print("this line will be skipped over if s is equal to 28")
if option == '3':
    try:
        answer = 24/0
        print(answer)
    except:
        print("\nAn error has occurred")


    
    
