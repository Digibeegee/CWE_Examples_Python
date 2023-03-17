
#Missing Authentication for Critical Function

class BankAccount:
    def __init__(self, accountNumber, accountType, accountName, balance):
        self.accountNumber = accountNumber
        self.accountType = accountType
        self.accountName = accountName
        self.balance = balance

    def getOwner(self):
        print(self.accountName)

class Bank:
    def createAccount(accNo,accType,accName,bal):
        account=BankAccount(accNo,accType,accName,bal)
        return account

if __name__ == '__main__':
    user1=Bank.createAccount("9876" , "Savings" , "Owner" , "1000")
    user1.getOwner()
