#adding maximum attempt limit
from src.CWE287.User import User

if __name__ == '__main__':
    admin = User("Admin", "passcode1234")
    max_attempts=3
    attempt=1
    pwd = input('Enter password')
    while not admin.validatePassword(pwd) and attempt<max_attempts:
        pwd = input('Wrong Password. Try Again')
        attempt+=1
    if(attempt>max_attempts):
        print("Account Locked")
    else:
        print("Welcome "+admin.username)