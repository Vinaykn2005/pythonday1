class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposite(self, amount):
        self.balance += amount
        print("The account holder is",self.account_holder)
        print("The amount",amount,"is succesfull deposite, The available balance is",self.balance)
       
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("The amount",amount,"is succesfully withdraw. The avalable balance is:",self.balance)
        else:
            print("Insuffient found:")

    def display_balance(self):
        print("Availabe balance:",self.balance)

class SavingAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        self.interest_rate = interest_rate
        super().__init__(account_holder, balance)
    def add_interst(self):
        interst = self.balance * self.interest_rate /100
        self.balance += interst
        print("amount after interst applied:",self.balance)

class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance, overdraft_limit):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withrawwith_overdraft(self,amount):
        if amount <= self.overdraft_limit:
            self.overdraft_limit -= amount
            print("The account holder name",self.account_holder)
            print("The overdraft amount is",self.overdraft_limit)
        else:
            print("overlimit exided")

ob1 = SavingAccount("vinay",10000,2)
ob2 = CurrentAccount("sharu",1000, 20000)
ob1.deposite(1000)
ob1.withdraw(500)
ob1.add_interst()
ob2.withrawwith_overdraft(500)
        