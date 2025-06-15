import sys
sys.path.insert(0, '/managers')

import managers.password_manager as password_manager
import managers.mfa_manager as mfa_manager

def main():
    print(password_manager.generatePasswordFor("TestUser"))
    print(mfa_manager.generate2FAFor("TestUser"))

main()