import password_manager
import mfa_manager

def main():
    print(password_manager.generatePasswordFor("Test"))
    print(mfa_manager.generate2FAFor("Test"))

main()
