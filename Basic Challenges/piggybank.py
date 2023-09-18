pennies = int(input("How many pennies are in your piggy bank? "))
twop = int(input("How many two pences are in your piggy bank? "))
fivep = int(input("How many five pences are in your piggy bank? "))

ptotal = pennies
twototal = twop*2
fivetotal = fivep*5
total = ptotal + twototal + fivetotal
print("You have " + str(total) + "p in your piggy bank")

if total <5000: #£50 in pennies
    print("You need to save more")
else:
    print("You are doing well")


