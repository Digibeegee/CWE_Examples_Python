import re

from src.CWE306.NonCompliant import BankAccount
#add authentication by PAN ID before bank account creation
class Bank:
    def validPan(pan):
        regex= "[A-Z]{5}[0-9]{4}[A-Z]{1}"
        if(len(pan)==10 and re.match(regex,pan)):
            return True
        return False

    def createAccount(accNo,accType,accName,bal,panID):
        if not Bank.validPan(panID):
            print("Cannot create Account")
            return None
        account=BankAccount(accNo,accType,accName,bal)
        return account

if __name__ == '__main__':
    user1=Bank.createAccount("9876" , "Savings" , "Owner" , "1000","BNZAA2318J")
    if user1 != None:
        user1.getOwner()