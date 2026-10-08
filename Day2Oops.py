import datetime
class InsufficientBalanceError(Exception):
    pass

class Account:
    Transaction_counter=1
    def __init__(self,account_number,name,balance=0):
        self.account_number=account_number
        self.name=name
        self.__balance=balance
        self.__transactions=[]
    def _recordTransaction(self,Transaction_type,amount):
        TransactionId=Account.Transaction_counter
        Account.Transaction_counter+=1
        transaction=Transaction(TransactionId,Transaction_type,amount,datetime.datetime.now(),self.get_balance())
        self.add_transaction(transaction)
    def deposit(self,amount):
        Transaction_type="deposit"
        if amount<0:
            raise InsufficientBalanceError("Insufficient Balance")
        else:
            self.__balance=self.__balance+amount
            self._recordTransaction(Transaction_type,amount)
    def withdraw(self,amount):
        Transaction_type="withdraw"
        if amount > self.__balance or amount<0:
            raise InsufficientBalanceError("Insufficient balance")
        else:
            self.__balance=self.__balance-amount
            self._recordTransaction(Transaction_type,amount)
    def transfer(self,targetAccount,amount):
        self.withdraw(amount)
        targetAccount.deposit(amount)
    def get_balance(self):
        return self.__balance
    def set_balance(self,amount):
        self.__balance=amount
    def add_transaction(self,transaction):
        self.__transactions.append(transaction)
    def show_transactions(self):
        for transaction in self.__transactions:
            transaction.display_transaction()

class SavingAccount(Account):
    def __init__(self,interest_rate,minimum_balance,account_number,name,balance=0):
        super().__init__(account_number,name,balance)
        self.interest_rate=interest_rate
        self.minimum_balance=minimum_balance
    def withdraw(self, amount):
        bal=self.get_balance()
        if bal-amount<self.minimum_balance:
            raise InsufficientBalanceError("Low balance than minimum amount")
        else:
            return super().withdraw(amount)


    def calculate_interest(self):
        return self.get_balance() * self.interest_rate / 100

    def add_interest(self):
        amt=self.calculate_interest()
        self.deposit(amt)

class CurrentAccount(Account):
    def __init__(self,overdraft_limit,account_number,name):
        super().__init__(account_number,name)
        self.overdraft_limit=overdraft_limit
    def check_overdraft(self,amount):
        return self.get_balance()-amount>=-self.overdraft_limit
    def withdraw(self, amount):
        if self.check_overdraft(amount):
            self.set_balance(self.get_balance()-amount)
            self._recordTransaction("withdraw",amount)
        else:
            raise InsufficientBalanceError("less than overdraft")

class Bank():
    counter=1
    def __init__(self,BankName,Bankcode):
        self.BankName=BankName
        self.Bankcode=Bankcode
        self.accounts=[]
        self.customers=[]
    def createAccount(self):
        UserChoice=input("""Choose Account type 
                         1. SavingAccount
                         2. CurrentAccount : 
                         """)
        if UserChoice=='1':
            minimumLimit=int(input("Enter Minimum Limit : "))
            InterestRate=int(input("Enter Interest Rate : "))
            AccountNo=input("Enter Your Account Number : ")
            CustomerName=input("Enter Your Name : ")
            account=SavingAccount(InterestRate,minimumLimit,AccountNo,CustomerName,balance=0)
        elif UserChoice=='2':
            overdraftLimit=int(input("Enter Overdraft Limit : "))
            AccountNo=input("Enter Your Account Number : ")
            CustomerName=input("Enter Your Name : ")
            account=CurrentAccount(overdraftLimit,AccountNo,CustomerName)
        else :
            print("Invalid Selection")
            return
        phone=input("Enter Your phone : ")
        email=input("Enter Your email : ")
        address=input("Enter Your address : ")
        customer_id=Bank.counter
        customer=Customer(customer_id, CustomerName, phone, email, address)  
        Bank.counter+=1
        self.accounts.append(account)
        customer.add_account(account)
        self.customers.append(customer)
    def findAccount(self,account_number):
        for account in self.accounts:
            if account.account_number==account_number:
                return account
        else :
                return False
    def closeAccount(self,account_number):
        account=self.findAccount(account_number)
        if account:
            self.accounts.remove(account)
            for customer in self.customers:
                for custaccount in customer.accounts:
                    if custaccount.account_number==account_number:
                        customer.remove_account(custaccount)
            print("Account Removed Successfully")
        else :
            print("No Account Found")
    def findCustomer(self,CustomerID):
        for customer in self.customers:
            if customer.customer_id==CustomerID:
                return customer
        return False
    def transferMoney(self,FromAccount,ToAccount,Amount):
        if self.findAccount(FromAccount) and self.findAccount(ToAccount):
            source=self.findAccount(FromAccount)
            target=self.findAccount(ToAccount)
            source.transfer(target,Amount)
        else :
            print("Account not found")
    def details(self):
        for account in self.accounts:
            print(f"Account number : {account.account_number}\nName : {account.name}\nBalance :{account.get_balance()}\nAccount Type : {type(account).__name__}")

class Customer():
    def __init__(self,customer_id,name,phone,email,address):
        self.customer_id=customer_id
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address
        self.accounts=[]
    def add_account(self,account):
        self.accounts.append(account)

    def remove_account(self,account):
        self.accounts.remove(account)

    def get_accounts(self):
        return self.accounts

    def display_customer(self):
        if self.customer_id:
            print(f"customer id : {self.customer_id}\nCustomer Name: {self.name}\nPhone : {self.phone}\nEmail: {self.email}")
        else:
            return

class Transaction():
    def __init__(self,transaction_id,transaction_type,amount,date,balance_after):
        self.transaction_id=transaction_id
        self.transaction_type=transaction_type
        self.amount=amount
        self.date=date
        self.balance_after=balance_after
    def display_transaction(self):
        print(f"Transaction_id : {self.transaction_id}\nTransaction Type : {self.transaction_type}\nAmount : {self.amount}\nDate : {self.date}\nBalance remaining: {self.balance_after}")

class BankSystem():
    def __init__(self):
        self.bank=Bank("SBI","SBIN110012")
    def main_menu(self):
        while True:
            print("Welcome To The Main Menu")
            userInput=input("""
                            1. Customer Management
                            2. Account Management
                            3. Transaction Management
                            4. Bank Details
                            5. Exit""")
            if userInput=='1':
                self.customer_menu()
            elif userInput=='2':
                self.account_menu()
            elif userInput=='3':
                pass
            elif userInput=='4':
                pass
            elif userInput=='5':
                break
            else :
                print("Invalid Choice")
    def customer_menu(self):
        while True:
            print("welcome to Customer Menu")
            choice=input("""
                        1.Create Customer/Accoung
                        2. Find Customer Account
                        3 Main Menu
                        """)
            if choice=='1':
                self.bank.createAccount()
            elif choice=='2':
                id=int(input('Enter Customer id to Find the account'))
                c=self.bank.findCustomer(id)
                if c:
                    c.display_customer()
                else:
                    print("No customer from this id")
            elif choice=='3':
                break
            else :
                print("invalid")
    def account_menu(self):
        while True:
            print("Welcome to the account section Menu")
            acc_menu=input("""Choose the below options
            1:Find Account
            2. Close Account
            3. Show all Account
            4. Back To Main Menu""")
            if acc_menu=='1':
                a=input("Enter account_number : ")
                ac=self.bank.findAccount(a)
                if ac:
                    print(ac.name)
                else:
                    print("Account Not Found")
            elif acc_menu=='2':
                a=input("Enter account number : ")
                self.bank.closeAccount(a)
            elif acc_menu=='3':
                self.bank.details()
            elif acc_menu=='4':
                break
    def transaction_menu(self):
        pass
    def run(self) :
        pass

   
c=BankSystem()
c.main_menu()