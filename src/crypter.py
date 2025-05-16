from simplecrypt import encrypt, decrypt

passkey = 'YAHAHA'

def encryptString(stringToCrypt):
    cipher = encrypt(passkey, stringToCrypt)
    return cipher

def decryptString(stringToDecrypt):
    decipheredString = encrypt(passkey, stringToDecrypt)
    return decipheredString

print(encryptString("test"))