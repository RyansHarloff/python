class BankAccount:
    bank_name = " The best Bank"
    def __init__(self,name, int_rate, balance):
        self.name = name
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
        else:
            print("Insufficient Funds, Charging a $5 fee.")
        return self
    def display_account_info(self):
        print(self.balance)
        return self
    def yield_interest(self):
        print("yield_interest")
        return self
    @staticmethod
    def can_withdraw(balance,amount):
        if(balance - amount) <0:
            return False
        else:
            return True

Dave = BankAccount("Dave", .04, 0)
James = BankAccount("James",.02,0)

James.deposit(200).deposit(400).deposit(300).withdraw(50).display_account_info().yield_interest
Dave.deposit(300).deposit(20).withdraw(300).withdraw(50).withdraw(90).withdraw(100).display_account_info().yield_interest