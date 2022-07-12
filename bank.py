class Bank:
    banksList = []
    bankID = -1
    def __init__(self, fullName, abbreviation):
        self.fullName = fullName
        self.abbreviation = abbreviation
        self.bankID = Bank.bankID

    @staticmethod
    def findBank(bankAbbreviation):
        for bank in Bank.bankList:
            if bank.abbreviation == bankAbbreviation:
                return True, bank
        return False, None
    
    @staticmethod
    def createNewBank(fullName, abbreviation):
        isBankExist, bank = Bank.findBank(abbreviation)
        if isBankExist:
            return False, None
        Bank.bankID += 1
        newBank = Bank(fullName, abbreviation)
        Bank.banksList.append(newBank)
        return True, newBank
        
    