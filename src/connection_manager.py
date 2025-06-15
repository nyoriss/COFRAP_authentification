import encrypt_manager

def isMatching(user, password, token):
    return password == user.password and token == user.token and not user.isExpired()

def isMatchingEncrypted(user, password, token):
    return encrypt_manager.decryptString(password) == encrypt_manager.decryptString(user.getEncryptedPassword()) and encrypt_manager.decryptString(token) == encrypt_manager.decryptString(user.getEncryptedToken()) and not user.isExpired()