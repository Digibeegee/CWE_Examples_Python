
#Improper Authentication

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def getpassword(self):
        return self.password

    def validatePassword(self, pwd):
        return self.password == pwd

if __name__ == '__main__':
    admin = User("Admin", "passcode1234")
    pwd = input('Enter password')
    while not admin.validatePassword(pwd):
        pwd = input('Wrong Password. Try Again')
