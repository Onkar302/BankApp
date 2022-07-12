from accounts import Account

class Customer:
    customerID = -1
    customerList = []
    def __init__(self, fName, lName, uName):
        self.fName = fName
        self.lName = lName
        self.uName = uName
        self.customerID = Customer.customerID
        self.accountList = []
        self.totalBalance = 0

    @staticmethod
    def createNewCustomer(fName, lName, uName):
        isCustomerExist, customer = Customer.findUser(uName)
        if isCustomerExist:
            return False, "Customer already exists"
        Customer.customerID += 1
        newCustomer = Customer(fName, lName, uName)
        Customer.customerList.append(newCustomer)
        return True, newCustomer

    @staticmethod
    def findCustomer(uName):
        for customer in Customer.customerList:
            if customer.uName == uName:
                return True, customer
        return False, None

    def findAccount(self, bankAbbreviation):
        if(len(self.accountList) == 0):
            return False, None
        for account in self.accountList:
            if(account.isAccountExist(bankAbbreviation)):
                return True, account
        return False, None

    def createNewAccount(self, bankAbbreviation):
        isAccountExist, account = Account.createNewAccount(bankAbbreviation)
        if not isAccountExist:
            return False, "Account not created"
        self.accountList.append(account)
        self.updateTotalBalance()
        return True, "Account created successfully"

    def __updateTotalBalance(self):
        self.totalBalance = 0
        for account in self.accountList:
            self.totalBalance += account.balance

    def transferMoney(self, amount, receiverCustomerName, receiverBankAbbreviation, senderBankAbbreviation):
        isSenderAccountExist, account = self.findAccount(senderBankAbbreviation)
        if not isSenderAccountExist:
            return False, "No such account"
        isReceiverExist, receiver = Customer.findCustomer(receiverCustomerName)
        if not isReceiverExist:
            return False, "Receiver account not found"
        isWithdrawDone, msgWithdraw = self.withdraw(amount, senderBankAbbreviation)
        if not isWithdrawDone:
            return False, "Withdraw failed"
        else:
            isDepositDone, msgDeposit = receiver.deposit(amount, receiverBankAbbreviation)
            if not isDepositDone:
                self.deposit(amount, receiverBankAbbreviation)
                return False, "Deposit failed"
            else:
                return True, "Deposit successful"

    def selfTransfer(self, amount, receiverBankAbbreviation, senderBankAbbreviation):
        return self.transferMoney(amount, self.username, receiverBankAbbreviation, senderBankAbbreviation)


    def withdraw(self, amount, bankAbbreviation):
        isAccountExist, account = self.findAccount(bankAbbreviation)
        if not isAccountExist:
            return False, "No such account"
        if account.isSufficientBalance(amount):
            account.balance -= amount
            self.__updateTotalBalance()
            return True, "Withdrawn Successfully"
        else:
            return False, "Insufficient Funds"

    def deposit(self, amount, bankAbbreviation):
        isAccountExist, account = self.findAccount(bankAbbreviation)
        if not isAccountExist:
            return False, "No such account"
        account.balance += amount
        self.__updateTotalBalance()
        return True, "Amount Succesfully Deposited"

    def displayBalance(self):
        print("Total balance :", self.totalBalance)
        for account in self.accountList:
            account.displayBalance()

    
        
        
