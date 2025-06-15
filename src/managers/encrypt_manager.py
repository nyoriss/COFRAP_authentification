import cryptocode

passkey = 'ThisIsAnEncryptKey'

def encryptString(stringToCrypt):
    cipher = cryptocode.encrypt(stringToCrypt, passkey)
    return cipher

def decryptString(stringToDecrypt):
    decipheredString = cryptocode.decrypt(stringToDecrypt, passkey)
    return decipheredString

