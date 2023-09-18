import time
playerscore = 0

name = input("What is your name? ")

time.sleep(0.5)

print("Welcome to the football quiz, " + name)
q1 = input("Question One: Which football team has won the most premier leagues?\n A) Liverpool\n B) Arsenal\n C) Manchester United\n D) Manchester City ")

if q1 == "C" or q1 == "c":
    time.sleep(0.2)
    print("That is the correct answer! You got a point!")
    playerscore = playerscore + 1
else:
    print("That is the incorrect answer :(")
    
q2 = input("Question Two: Who scored the most goals in Premier League History?\n A) Alan Shearer\n B) Harry Kane\n C) Sergio Auguero\n D) Thierry Henry ")
if q2 == "a" or q2 == "A":
    time.sleep(0.2)
    print("That is the correct answer! You got a point!")
    playerscore = playerscore + 1
else:
    print("That is the incorrect answer :(")
    
q3 = input("Question Three: Who were the first club to win the Premier League?\n A) Blackburn\n B) Manchester United\n C) Liverpool\n D) Spurs ")
if q3 == "B" or q3 == "b":
    time.sleep(0.2)
    print("That is the correct answer! You got a point!")
    playerscore = playerscore + 1
else:
    print("That is the incorrect answer :(")
    
q4 = input("Question Four: Who scored the fastest ever Premier League goal?\n A) Wayne Rooney\n B) Teddy Sheringham\n C) Sadio Mane\n D) Shane Long ")
if q4 == "D" or q4 == "D":
    time.sleep(0.2)
    print("That is the correct answer! You got a point!")
    playerscore = playerscore + 1
else:
    print("That is the incorrect answer :(")
    
q5 = input("Question Five: Who has made the most appearances in the Premier League?\n A) Gareth Barry\n B) Frank Lampard\n C) James Milner\n D) Wayne Rooney ")
if q5 == "a" or q5 == "A":
    time.sleep(0.2)
    print("That is the correct answer! You got a point!")
    playerscore = playerscore + 1
else:
    print("That is the incorrect answer :(")

time.sleep(0.5)
print(str(name) + " scored " + str(playerscore) + " out of 5")
if playerscore > 3:
    print("Well Done!\nWell Done!\nWell Done!\nWell Done!\nWell Done!")

    
    
