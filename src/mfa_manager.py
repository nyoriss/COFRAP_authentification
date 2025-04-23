import authentificator
import random


digitList = authentificator.digitList
lettersList = authentificator.lettersList

def generate2FAFor(user):
    token = ""

    for i in range(24):
        randomInt = random.randint(1, 2)
        result = switch(randomInt)

        if(result != "Invalid"):
            token = token + result
    authentificator.generateQRCodeFor(token, user + "_token")
    return token

def switch(character):
    switch= {
        1: authentificator.getRandomAsciiLetter(),
        2: authentificator.getRandomDigit()
    }
    return switch.get(character, "Invalid")