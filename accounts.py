from operator import truediv
from bank import Bank
class Account: 
    accountID = -1
    
    def __init__(self, bank, balance):
        self.bank = bank
        self.balance = balance
        self.accountID = Account.accountID

    @staticmethod
    def createNewAccount(bankAbbreviation):
        isBank, bankObject = Bank.findBank(bankAbbreviation)
        if not isBank:
            return False, None
        Account.accountID += 1
        newAccount = Account(bankObject, 1000)
        return True, newAccount
    
    def isAccountExist(self, bankAbbreviation):
        if(self.bank.abbreviation == bankAbbreviation):
            return True
        else:
            return False

    def isSufficientBalance(self, amount):
        if(self.balance >= amount):
            return True
        else:
            return False

    def displayBalance(self):
        print("Account balance is :", self.balance)

    

    


