
#Improper Authentication
from src.CWE287.User import User

if __name__ == '__main__':
    admin = User("Admin", "passcode1234")
    pwd = input('Enter password')
    while not admin.validatePassword(pwd):
        pwd = input('Wrong Password. Try Again')
