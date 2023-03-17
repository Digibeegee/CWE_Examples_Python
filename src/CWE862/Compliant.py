from src.CWE862.User import User


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
        #adding authorization check
        if 'write' in user1.getPermissions():
            msg.post('Attacker can exploit this weakness', user1.username)
        else:
            print('No post permission for user: ',user1.username)