tfound = False
num1 = int(input("Enter a number "))
num2 = int(input("Enter a number "))
num3 = int(input("Enter a number "))
target = int(input("Enter a target value "))
l = [num1, num2, num3]

options = ['tpc','small','large','sum','product','exit']
o = input("What do you want to check in the list? ").lower()
if o == options[0]:
    for item in l:
        if item == target:
            tfound = True
            print("Your target number ,"+str(target)+ ",is in the list.")
            break
    if tfound == False:
        print("Your target number isn't in the list.")
if o == options[1]:
    print(min(l))
if o == options[2]:
    print(max(l))
if o == options[3]:
    print(sum(l))
if o == options[4]:
    products = l[0]
    for item in l[1:]:
        products *=item
    print(products)



                  
        




