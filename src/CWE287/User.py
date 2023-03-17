class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def getpassword(self):
        return self.password

    def validatePassword(self, pwd):
        return self.password == pwd