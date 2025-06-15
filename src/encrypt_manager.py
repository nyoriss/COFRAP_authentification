import cryptocode

passkey = 'ThisIsAnEncryptKey'

def encryptString(stringToCrypt):
    cipher = cryptocode.encrypt(stringToCrypt, passkey)
    return cipher

def decryptString(stringToDecrypt):
    decipheredString = cryptocode.decrypt(stringToDecrypt, passkey)
    return decipheredString

#encrypted = encryptString("test")
#print(encrypted)
#encrypted = encryptString("test")
#print(encrypted)
#print(decryptString(encrypted))