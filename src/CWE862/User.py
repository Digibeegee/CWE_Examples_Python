class User:
    def __init__(self, username, password, permissions):
        self.username = username
        self.password = password
        self.permissions = permissions

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def getPermissions(self):
        return self.permissions