import authentificator
import random


def generatePasswordFor(user):
    password = ""

    for i in range(24):
        randomInt = random.randint(1, 3)
        result = passwordSwitch(randomInt)

        if(result != "Invalid"):
            password = password + result
    authentificator.generateQRCodeFor(password, user + "_password")
    return password

def passwordSwitch(character):
    switch= {
        1: authentificator.getRandomAsciiLetter(),
        2: authentificator.getRandomDigit(),
        3: authentificator.getRandomPunctuation()
    }
    return switch.get(character, "Invalid")
