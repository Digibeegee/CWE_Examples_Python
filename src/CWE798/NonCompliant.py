
#Hardcoded Credentials

def verifyAdmin(pwd):
    if(pwd == 'pwd1234'):
        print("Admin Verified! Welcome.")
        return True
    print("Access Denied")
    return False

if __name__ == '__main__':
    password="pwd1234"
    verifyAdmin(password)