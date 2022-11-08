data = "hi"
def write():
    with open('./dump/data.txt','w') as file:
        file.write(data + '\n')
        file.close()
        print("You have written to a file")
write()
def read():
    with open('./dump/data.txt', 'r') as file:
        file.close()
read()
def append():
    with open('./dump/data.txt','a') as file:
        file.write(data + '\n')
        file.close()
append()

#the difference between write and append is writing overwrites a file, whereas append just adds new info to the file.
