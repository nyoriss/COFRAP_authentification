import password_manager
import connection_manager
import mfa_manager
import user
from datetime import datetime

def main():
    user1 = user.User("user1")

    user1.setPassword(password_manager.generatePasswordFor("user1"), datetime.now())
    user1.setToken(mfa_manager.generate2FAFor("user1"), datetime.now())

    print(user1.printAll())

    print("Is matching ? : " + str(connection_manager.isMatching(user1, user1.password, user1.token)))

main()
