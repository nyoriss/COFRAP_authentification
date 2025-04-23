import string
import random

import qr_code_manager

lettersList = string.ascii_letters
digitList = ["2", "3", "4", "5", "6", "7", "8", "9"]
punctuationList = ["!", "#", "%", "+", ":", "=", "?", "@"]
# 

def getRandomAsciiLetter():
    randomLetter = random.randint(0, len(lettersList)-1)
    return lettersList[randomLetter]

def getRandomDigit():
    randomDigit = random.randint(0, len(digitList)-1)
    return digitList[randomDigit]

def getRandomPunctuation():
    randomPunctuation = random.randint(0, len(punctuationList)-1)
    return punctuationList[randomPunctuation]

def generateQRCodeFor(password, name):
    qr_code_manager.generateQRCodeFor(password, name)
