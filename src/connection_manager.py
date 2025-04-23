
def isMatching(user, password, token):
    return password == user.password and token == user.token and not user.isExpired()
