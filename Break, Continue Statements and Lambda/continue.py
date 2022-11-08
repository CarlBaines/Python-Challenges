import time
s = 0
for i in range(5):
    s = s + 2
    print("\ni = ", i, "s = ",s)
    time.sleep(1)
    if s == 8:
        continue
    time.sleep(1)
    print("this line will be skipped over if s is equal to 8")
