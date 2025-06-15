import managers.password_manager as password_manager
import managers.connection_manager as connection_manager
import managers.encrypt_manager as encrypt_manager
import managers.mfa_manager as mfa_manager
import managers.user_manager as user_manager

from datetime import datetime
from datetime import timedelta


def main():
    print("-----------------Test OK :----------------- \n\n")

    test_connection_OK()

    print("----------Test KO by expiration :---------- \n\n")

    test_connection_KO_expired()

def test_connection_OK():
    userOK = user_manager.User("userOK")

    userOK.setPassword(password_manager.generatePasswordFor("userOK"), datetime.now())
    userOK.setToken(mfa_manager.generate2FAFor("userOK"), datetime.now())

    userOKEncryptedPassword = encrypt_manager.encryptString(userOK.password)
    userOKEncryptedToken = encrypt_manager.encryptString(userOK.token)

    print("All informations About the user : ")
    print(userOK.printAll())

    print("\n")

    print("This should return True : ")
    print(connection_manager.isMatchingEncrypted(userOK, userOKEncryptedPassword, userOKEncryptedToken))


def test_connection_KO_expired():
    userKO = user_manager.User("userKO")

    year = timedelta(days=365)

    userKO.setPassword(password_manager.generatePasswordFor("userKO"), datetime.now() - 1 * year)
    userKO.setToken(mfa_manager.generate2FAFor("userKO"), datetime.now() - 1 * year)

    userKOEncryptedPassword = encrypt_manager.encryptString(userKO.password)
    userKOEncryptedToken = encrypt_manager.encryptString(userKO.token)

    print("All informations About the user : ")
    print(userKO.printAll())

    print("\n")

    print("This should return False : ")
    print(connection_manager.isMatchingEncrypted(userKO, userKOEncryptedPassword, userKOEncryptedToken))

main()