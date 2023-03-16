
#Hardcoded Credentials

def verifyAdmin(pwd):
    if(pwd == 'pwd1234'):
        print("Admin Verified! Welcome.")
        return True
    print("Access Denied")
    return False

password="pwd1234"
verifyAdmin(password)