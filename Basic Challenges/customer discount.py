amountspent = int(input("How much did you spend in pounds? "))
if amountspent <= 10:
    discount = 1.10
    print("Your discount is 10% off")
    finalprice1 = amountspent/1.1
    print("You need to pay £" + str(finalprice1))
else:
    discount = 1.20
    print("Your discount is 20% off")
    finalprice2 = amountspent/1.2
    print("You need to pay £" + str(finalprice2))
    
    
