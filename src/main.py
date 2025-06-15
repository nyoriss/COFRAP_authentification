import password_manager
import mfa_manager

def main():
    print(password_manager.generatePasswordFor("TestUser"))
    print(mfa_manager.generate2FAFor("TestUser"))

main()