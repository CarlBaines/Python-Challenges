import time
num = 12

timestable = int(input("Which times table would you like? "))

for i in range(1,11):
    time.sleep(0.2)
    print(num, "x", i, "=", num*i)
