from datetime import datetime
from dateutil.relativedelta import relativedelta
import encrypt_manager

class User:

    username = ""
    password = ""
    expirationTime = relativedelta(months=6)

    def __init__(self, username, password = "", passwordDate = "", token = "", tokenDate = ""):
        self.username = username
        self.password = password
        self.encryptedPassword = ""
        self.passwordDate = passwordDate
        self.token = token
        self.encryptedToken = ""
        self.tokenDate = tokenDate

    def setPassword(self, password, passwordDate):
        self.password = password
        self.encryptedPassword = encrypt_manager.encryptString(password)
        self.passwordDate = passwordDate

    def setToken(self, token, tokenDate):
        self.token = token
        self.encryptedToken = encrypt_manager.encryptString(token)
        self.tokenDate = tokenDate

    def getEncryptedPassword(self):
        return self.encryptedPassword

    def getEncryptedToken(self):
        return self.encryptedToken

    def isExpired(self):
        return datetime.now() > self.passwordDate + self.expirationTime and datetime.now() > self.tokenDate + self.expirationTime


    def printAll(self):
        return "Username : " + self.username + " \nPassword : " + self.password  + "\nPassword GenDate : " + str(self.passwordDate) + "\nPassword ExpDate : " + str(self.passwordDate + self.expirationTime) + "\nToken :  " + self.token  + "\nToken GenDate : " + str(self.tokenDate) + "\nToken ExpDate : " + str(self.tokenDate + self.expirationTime)
      