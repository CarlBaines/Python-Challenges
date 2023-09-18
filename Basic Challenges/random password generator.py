import time
import random
import string

def generate_password(length):
            # Define the character sets to use in the password
            lowercase = string.ascii_lowercase
            uppercase = string.ascii_uppercase
            numbers = string.digits
            symbols = string.punctuation

            # Combines the sets of characters into one.
            all_characters = lowercase + uppercase + numbers + symbols

            # Generate a random password by selecting characters from the combined set
            password = ''.join(random.choice(all_characters) for i in range(length))

            return password
            
#here is where you enter the password length which is passed into the function.
with open("passwords.txt","a") as file:
        password = generate_password(12)     
        file.write(password + "\n")      #writes password to file.

print(password)

