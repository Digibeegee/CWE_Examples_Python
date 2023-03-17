
#Improper Authorization

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


class MessageBoard:
    def post(self, message, name):
        print(message+'\n:'+name)

    def read(self):
        print('Reading messages from bulletin.....')


if __name__ == '__main__':
    user1 = User('Prerona', 'pwd#1234', ('read',))
    if user1.username == user1.getUsername() and user1.password == user1.getPassword():
        print('User Verified')
        msg = MessageBoard()
        msg.read()
        msg.post('Attacker can exploit this weakness', user1.username)