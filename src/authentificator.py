import string
import random
import qrcode

lettersList = string.ascii_letters
digitList = ["2", "3", "4", "5", "6", "7", "8", "9"]
punctuationList = ["!", "#", "%", "+", ":", "=", "?", "@"]
# 

def generatePassWordFor(user):
    password = ""

    for i in range(24):
        randomInt = random.randint(1, 3)
        result = switch(randomInt)

        if(result != "Invalid"):
            password = password + result
    
    return password

def switch(character):
    switch= {
        1: getRandomAsciiLetter(),
        2: getRandomDigit(),
        3: getRandomPunctuation()
    }
    return switch.get(character, "Invalid")


def getRandomAsciiLetter():
    randomLetter = random.randint(0, len(lettersList)-1)
    return lettersList[randomLetter]

def getRandomDigit():
    randomDigit = random.randint(0, len(digitList)-1)
    return digitList[randomDigit]

def getRandomPunctuation():
    randomPunctuation = random.randint(0, len(punctuationList)-1)
    return punctuationList[randomPunctuation]

def generateQRCodeFor(password):
    generatedQrcode = qrcode.make(password)
    generatedQrcode.save('assets\QRCode\QRcode.png')