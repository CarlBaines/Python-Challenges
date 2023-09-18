from os import getcwd  #imports
import datetime
import time

global cwd     
cwd = getcwd() #gets current directory.

def addEntry(entryType): #function passes through user input from option number.
    if entryType == 'comment':
        time.sleep(.4)
        entry = input('Enter your comment: ')    #inputs.
        time.sleep(.4)
    elif entryType == 'diary':
        time.sleep(.4)
        entry = input('Enter your diary entry ')

    now = datetime.datetime.now()      #gets current date/time.
    timestamp = now.strftime('%Y-%m-%d %H:%M:%S')   #formats the date and time.

    with open('entries.txt', 'a') as file:         #opens text file and writes to it.
        file.write(f"{entryType} | {timestamp} | {entry}\n")
    
    print("You have submitted an entry to the diary")

def viewEntries():
    with open('entries.txt', 'r') as file:
        entries = file.readlines()      #reads lines within the text files.

        if not entries:
            print('No entries were found')
            return

        for entry in entries:
            print(entry)   #outputs any entries to the text file.
    
while True:   #main loop.
    print("Welcome to your diary, what would you like to do? ")
    time.sleep(.4)
    print("1. Add a comment to the diary")
    time.sleep(.4)
    print("2. Add a diary entry")
    time.sleep(.4)
    print("3. View all entries")
    time.sleep(.4)
    print("4. Exit")

    time.sleep(.4)
    
    option = input('Enter the option number (1-4): ')

    if option == '1':
        addEntry("comment")
    elif option == '2':
        addEntry("diary")
    elif option == '3':
        viewEntries()
    elif option == '4':
        break
