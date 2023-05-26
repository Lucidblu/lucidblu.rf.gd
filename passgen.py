from itertools import repeat
import random
import string

complexityInput = input("Complexity: \n")
passNumberList = []
passLetterList = []
endPassList = []

for i in range(int(complexityInput)):
    passGenNumber = random.randrange(9)
    passGenLetter = random.choice(string.ascii_letters)
    passNumberList.append(passGenNumber)
    passLetterList.append(passGenLetter)

    endPassList.append(random.choice(str(passGenNumber) + passGenLetter))
endPassList = str(endPassList)
endPassList = endPassList.replace(',', '')
endPassList = endPassList.replace("'", '')
endPassList = endPassList.replace('[', '')
endPassList = endPassList.replace(']', '')
endPassList = endPassList.replace('"', '')
endPassList = endPassList.replace(' ', '')

print("Your generated password: " + endPassList)

askSave = input("Do you want to save this password? \n 1.yes \n 2.no \n")

if askSave == "1":
    usernameInput = input("What is the username associated with this password? \n")

    passwords = open('Password.txt', 'a')
    passwords.write("Username: " + usernameInput + "\n")
    passwords.write("Password: " + endPassList + "\n")
else:
    print("Exiting")
