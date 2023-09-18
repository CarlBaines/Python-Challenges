import time

member_details = []

def save_details():
    fields = ['Name | Age | Membership ID']
    rows = member_details
    with open('memberdetails.txt','a') as file:
        file.write(fields)
        file.write(rows)

print('----------------Rock Climbing Club System----------------')
time.sleep(.4)
option = input('Please choose from the following options: ' + '\n' + '1. Enter details ' + '\n' + '2. View Member Details ' + '\n' + '3. Exit ')

while True:
    if option == '1':
        name = input('Please enter your name ')
        member_details.append(name)
        age = input('Please enter your age ')
        member_details.append(age)
        membershipID = input('Please enter your Membership ID ')
        member_details.append(membershipID)
        time.sleep(.2)
        print('Your details: ')
        time.sleep(.2)
        print(member_details)

    if option == '2':
        found = False
        time.sleep(.2)
        search = input('Please enter your Membership ID ')

    if option == '3':
        break
        

    