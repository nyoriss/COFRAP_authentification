from datetime import datetime
from dateutil.relativedelta import relativedelta

class User:

    username = ""
    password = ""
    expirationTime = relativedelta(months=6)

    def __init__(self, username, password = "", passwordDate = "", token = "", tokenDate = ""):
        self.username = username
        self.password = password
        self.passwordDate = passwordDate
        self.token = token
        self.tokenDate = tokenDate

    def setPassword(self, password, passwordDate):
        self.password = password
        self.passwordDate = passwordDate

    def setToken(self, token, tokenDate):
        self.token = token
        self.tokenDate = tokenDate

    def isExpired(self):
        return datetime.now() > self.passwordDate + self.expirationTime and datetime.now() > self.tokenDate + self.expirationTime
        

    def printAll(self):
        return "Username : " + self.username + " \nPassword : " + self.password  + "\nPassword GenDate : " + str(self.passwordDate) + "\nPassword ExpDate : " + str(self.passwordDate + self.expirationTime) + "\nToken :  " + self.token  + "\nToken GenDate : " + str(self.tokenDate) + "\nToken ExpDate : " + str(self.tokenDate + self.expirationTime)
      