data1 = 'fortnite gamer'
data2 = '12345'
data3 = '#~@'
data4 = 'this is appended data'
def write():
    with open('./dump2/data2.txt','w') as file:
        file.write(data1 + '\n' + data2 + '\n' + data3 + '\n')
        print("You have written to a file")
write()

def read():
    open('./dump2/data2.txt','r')
read()
def append():
    with open('./dump2/data2.txt','a') as file:
        file.seek(0,0)
        file.write(data4 + '\n')
append()
