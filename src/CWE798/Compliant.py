from src.CWE798 import Constant
#hardcoded values stored in seperate file/class
def verifyAdmin(pwd):
    if(pwd == Constant.admin_password):
        print("Admin Verified! Welcome.")
        return True
    print("Access Denied")
    return False

if __name__ == '__main__':
    password="pwd1234"
    verifyAdmin(password)