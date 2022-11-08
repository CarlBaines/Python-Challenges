nums = 0
l = [1,2,3,4,5]
target = 5
tfound = False
for item in l:
    if item == target:
        tfound = True
        print("Target found: " + str(item))
    else:
        print("Target not found, the number was:" + str(item))
        item = item + 1
    


